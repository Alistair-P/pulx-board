#!/usr/bin/env python3
"""pulxsim.py: a labelled-photon study of region and weighting methods for a weighted Z^2_1 search.

Every simulated photon carries a label: 0 = target, j >= 1 = neighbour j, -1 = flat background,
-2 = diffuse emission. A method turns the photons into per-photon weights w_i (0 outside its region).
The weighted statistic is Z^2_w = (2 / sum w^2) |sum w exp(i phi)|^2. Under no signal it is
asymptotically chi^2_2. If the target pulses with rate proportional to 1 + a cos(phi), then
E[sum w exp(i phi)] = (a/2) sum_{target} w, so Z^2_w is noncentral chi^2_2 with
    lambda = a^2 K / 2,   K = (sum_{label 0} w)^2 / sum w^2   ("effective target counts").
So with labels, each realisation's detectability follows exactly from its weights, with no phases
drawn. check() confirms this against direct phase draws, and confirms the null.

Positions are in arcsec, the target's catalogue position is (0, 0), counts are per observation.
The PSF is a King-profile stand-in (rc 5.5", alpha 1.5, roughly pn at 1.5 keV), optionally stretched
for off-axis sources. It is not the XMM calibration PSF.
"""
import json
import sys
import numpy as np
from scipy.stats import ncx2, chi2
from scipy.optimize import brentq
from scipy.ndimage import gaussian_filter

THR = chi2.isf(1e-9, 2)          # single-trial p = 1e-9  ->  Z^2 = 41.45
RF = 125.0                        # simulated field radius
RFIT = 90.0                       # joint-fit radius
PIX = 0.5                         # integration grid
EMIN, EMAX = 0.5, 7.0


class King:
    def __init__(self, rc=5.5, alpha=1.5, sx=1.0, sy=1.0, theta=0.0):
        self.rc, self.al, self.sx, self.sy = rc, alpha, sx, sy
        self.c, self.s = np.cos(np.deg2rad(theta)), np.sin(np.deg2rad(theta))

    def density(self, dx, dy):    # per arcsec^2, integrates to 1 over the plane
        xp = (self.c * dx + self.s * dy) / self.sx
        yp = (-self.s * dx + self.c * dy) / self.sy
        u = 1 + (xp * xp + yp * yp) / self.rc ** 2
        return (self.al - 1) / (np.pi * self.rc ** 2 * self.sx * self.sy) * u ** (-self.al)

    def sample(self, n, rng):
        u = (1 - rng.random(n)) ** (-1 / (self.al - 1))
        r = self.rc * np.sqrt(u - 1)
        ph = rng.random(n) * 2 * np.pi
        xp, yp = r * np.cos(ph) * self.sx, r * np.sin(ph) * self.sy
        return self.c * xp - self.s * yp, self.s * xp + self.c * yp


# Observed-spectrum stand-ins on 0.5-7 keV (gamma shapes): a ULX, flat particle background, soft gas.
SPEC = {"hard": (2.5, 0.8), "flat": None, "soft": (3.0, 0.33)}


def spec_pdf(kind, E):
    if SPEC[kind] is None:
        return np.full_like(E, 1 / (EMAX - EMIN))
    k, th = SPEC[kind]
    g = np.linspace(EMIN, EMAX, 4001)
    norm = np.trapezoid(g ** (k - 1) * np.exp(-g / th), g)
    return E ** (k - 1) * np.exp(-E / th) / norm


def spec_sample(kind, n, rng):
    if SPEC[kind] is None:
        return rng.uniform(EMIN, EMAX, n)
    k, th = SPEC[kind]
    out = np.empty(0)
    while out.size < n:
        e = rng.gamma(k, th, 2 * (n - out.size) + 10)
        out = np.concatenate([out, e[(e >= EMIN) & (e <= EMAX)]])
    return out[:n]


class Scenario:
    """nbrs: list of (x, y, counts). planes: exposed where nx*x + ny*y <= c for every (nx, ny, c).
    diffuse: dict(x, y, rb, beta, at_src) with at_src the diffuse density at the target."""

    def __init__(self, name, Nt, beta, nbrs=(), planes=(), diffuse=None, psf_true=None,
                 energy=False, bkg_annulus=(60.0, 120.0), mask_r=10.0, tgt_off=(0.0, 0.0), nbr_off=None):
        # nbrs are catalogue positions; tgt_off and nbr_off shift the TRUE positions (astrometric error)
        self.name, self.Nt, self.beta, self.nbrs = name, Nt, beta, list(nbrs)
        self.tgt_off = tgt_off
        self.nbr_off = list(nbr_off) if nbr_off else [(0.0, 0.0)] * len(self.nbrs)
        self.planes, self.diffuse, self.energy = list(planes), diffuse, energy
        self.psf_true = psf_true or King()
        self.psf_on = King()
        self.bkg_annulus, self.mask_r = bkg_annulus, mask_r
        if diffuse:
            d = diffuse
            r2 = d["x"] ** 2 + d["y"] ** 2
            self.D0 = d["at_src"] / (1 + r2 / d["rb"] ** 2) ** (-3 * d["beta"] + 0.5)
        g = np.arange(-RF + PIX / 2, RF, PIX)
        self.GX, self.GY = np.meshgrid(g, g)
        self.GR = np.hypot(self.GX, self.GY)
        self.Gexp = self.exposed(self.GX, self.GY) & (self.GR <= RF)
        # masks used by the aperture-style methods: radius mask_r, capped so it stays >= 10" from the target
        self.masks = []
        for (x, y, N) in self.nbrs:
            d = np.hypot(x, y)
            r = min(mask_r, d - 10.0)
            if r >= 3.0:
                self.masks.append((x, y, r))

    def exposed(self, x, y):
        ok = np.ones(np.shape(x), bool)
        for nx, ny, c in self.planes:
            ok &= nx * x + ny * y <= c
        return ok

    def diffuse_density(self, x, y):
        d = self.diffuse
        return self.D0 * (1 + ((x - d["x"]) ** 2 + (y - d["y"]) ** 2) / d["rb"] ** 2) ** (-3 * d["beta"] + 0.5)

    def in_masks(self, x, y):
        m = np.zeros(np.shape(x), bool)
        for (mx, my, r) in self.masks:
            m |= (x - mx) ** 2 + (y - my) ** 2 < r * r
        return m

    def simulate(self, rng):
        xs, ys, ls, es = [], [], [], []
        def add(x, y, lab, kind):
            xs.append(x); ys.append(y); ls.append(np.full(x.size, lab)); es.append(spec_sample(kind, x.size, rng))
        x, y = self.psf_true.sample(rng.poisson(self.Nt), rng)
        add(x + self.tgt_off[0], y + self.tgt_off[1], 0, "hard")
        for j, (nx, ny, N) in enumerate(self.nbrs, 1):
            x, y = self.psf_true.sample(rng.poisson(N), rng)
            ox, oy = self.nbr_off[j - 1]
            add(x + nx + ox, y + ny + oy, j, "hard")
        n = rng.poisson(self.beta * np.pi * RF ** 2)
        r, ph = RF * np.sqrt(rng.random(n)), rng.random(n) * 2 * np.pi
        add(r * np.cos(ph), r * np.sin(ph), -1, "flat")
        if self.diffuse:
            dg = self.diffuse_density(self.GX, self.GY) * (self.GR <= RF)
            total, dmax = dg.sum() * PIX ** 2, dg.max()
            n = rng.poisson(total)
            out_x, out_y = np.empty(0), np.empty(0)
            while out_x.size < n:
                m = 4 * (n - out_x.size) + 100
                r, ph = RF * np.sqrt(rng.random(m)), rng.random(m) * 2 * np.pi
                cx, cy = r * np.cos(ph), r * np.sin(ph)
                keep = rng.random(m) < self.diffuse_density(cx, cy) / dmax
                out_x, out_y = np.concatenate([out_x, cx[keep]]), np.concatenate([out_y, cy[keep]])
            add(out_x[:n], out_y[:n], -2, "soft")
        x, y, lab, E = (np.concatenate(a) for a in (xs, ys, ls, es))
        keep = (np.hypot(x, y) <= RF) & self.exposed(x, y)
        return x[keep], y[keep], lab[keep], E[keep]


# ---------------------------------------------------------------- methods
def grid_int(sc, f, region):
    return (f * (region & sc.Gexp)).sum() * PIX ** 2


def cached(sc, key, fn):
    c = sc.__dict__.setdefault("_cache", {})
    if key not in c:
        c[key] = fn()
    return c[key]


def aperture_weights(sc, ev, R, weighted, psf=None, aware=True):
    """Aperture-style: circle R minus capped masks; background from an annulus (flat); target counts
    from aperture photometry; weights p = s/(s+b) with s from the assumed PSF."""
    x, y, lab, E = ev
    psf = psf or sc.psf_on
    r = np.hypot(x, y)
    reg = (r < R) & ~sc.in_masks(x, y)
    w = np.zeros(x.size)
    if not weighted:
        w[reg] = 1.0
        return w
    a1, a2 = sc.bkg_annulus
    excl = lambda X, Y: np.any([(X - nx) ** 2 + (Y - ny) ** 2 < 900 for nx, ny, _ in sc.nbrs], axis=0) \
        if sc.nbrs else np.zeros(np.shape(X), bool)
    ann = (r >= a1) & (r < a2) & ~excl(x, y)
    def geom():
        Gann = (sc.GR >= a1) & (sc.GR < a2) & ~excl(sc.GX, sc.GY)
        Greg = (sc.GR < R) & ~sc.in_masks(sc.GX, sc.GY)
        fG = psf.density(sc.GX, sc.GY)
        if aware:
            return grid_int(sc, 1.0, Gann), grid_int(sc, 1.0, Greg), grid_int(sc, fG, Greg)
        # ignores the exposure mask, as a full-circle area scaling would
        return grid_int(sc, 1.0, Gann), Greg.sum() * PIX ** 2, (fG * Greg).sum() * PIX ** 2
    Aann, A, eef = cached(sc, ("ap", R, id(psf), aware), geom)
    b = ann.sum() / Aann
    Nt = max((reg.sum() - b * A) / eef, 1.0)
    s = Nt * psf.density(x[reg], y[reg])
    w[reg] = s / (s + b)
    return w


def em(dens, n_iter=500, tol=1e-8):
    K = dens.shape[0]
    pi = np.full(K, 1.0 / K)
    for _ in range(n_iter):
        num = pi[:, None] * dens
        resp = num / num.sum(0)
        new = resp.mean(1)
        if np.max(np.abs(new - pi)) < tol:
            pi = new
            break
        pi = new
    num = pi[:, None] * dens
    return pi, num / num.sum(0)


def smooth_map(sc, ev, sigma=15.0, hole=30.0, step=2.0):
    """Background map from the photons more than `hole` from every source, smoothed by
    normalised convolution (counts and exposure both smoothed), like a spline background map."""
    x, y, lab, E = ev
    srcs = [(0.0, 0.0)] + [(nx, ny) for nx, ny, _ in sc.nbrs]
    far = np.all([(x - a) ** 2 + (y - b) ** 2 > hole ** 2 for a, b in srcs], axis=0)
    edges = np.arange(-RF, RF + step, step)
    H, _, _ = np.histogram2d(y[far], x[far], bins=[edges, edges])
    c = (edges[:-1] + edges[1:]) / 2
    CX, CY = np.meshgrid(c, c)
    expo = (sc.exposed(CX, CY) & (np.hypot(CX, CY) <= RF)
            & np.all([(CX - a) ** 2 + (CY - b) ** 2 > hole ** 2 for a, b in srcs], axis=0)).astype(float)
    num = gaussian_filter(H, sigma / step)
    den = gaussian_filter(expo, sigma / step)
    M = num / np.maximum(den, 1e-9) / step ** 2           # counts per arcsec^2
    def at(px, py):
        i = np.clip(((py + RF) / step).astype(int), 0, c.size - 1)
        j = np.clip(((px + RF) / step).astype(int), 0, c.size - 1)
        return M[i, j]
    return at


def fit_weights(sc, ev, R=60.0, psf=None, bkg="flat", energy=False):
    """Joint fit (EM on fixed shapes): target + every neighbour + background, amplitudes free.
    Returns the target's responsibilities as weights inside R, and each neighbour's."""
    x, y, lab, E = ev
    psf = psf or sc.psf_on
    r = np.hypot(x, y)
    inf = r < RFIT
    Gfit = sc.GR < RFIT
    comps, gcomps = [], []
    srcs = [(0.0, 0.0)] + [(nx, ny) for nx, ny, _ in sc.nbrs if np.hypot(nx, ny) < RFIT + 40]
    for (a, b) in srcs:
        nrm = cached(sc, ("psf", a, b, id(psf)), lambda: grid_int(sc, psf.density(sc.GX - a, sc.GY - b), Gfit))
        f = psf.density(x[inf] - a, y[inf] - b) / nrm
        if energy:
            f = f * spec_pdf("hard", E[inf])
        comps.append(f)
    Afit = cached(sc, ("Afit",), lambda: grid_int(sc, 1.0, Gfit))
    if bkg == "flat":
        f = np.full(inf.sum(), 1.0 / Afit)
        if energy:
            f = f * spec_pdf("flat", E[inf])
        comps.append(f)
    elif bkg == "map":
        at = smooth_map(sc, ev)
        comps.append(at(x[inf], y[inf]) / grid_int(sc, at(sc.GX, sc.GY), Gfit))
    elif bkg == "model+flat":   # flat + the diffuse model's shape, amplitudes free
        comps.append(np.full(inf.sum(), 1.0 / Afit) * (spec_pdf("flat", E[inf]) if energy else 1))
        nd = cached(sc, ("dif",), lambda: grid_int(sc, sc.diffuse_density(sc.GX, sc.GY), Gfit))
        comps.append(sc.diffuse_density(x[inf], y[inf]) / nd * (spec_pdf("soft", E[inf]) if energy else 1))
    pi, resp = em(np.array(comps))
    w = np.zeros(x.size)
    sel = inf & (r < R)
    w[sel] = resp[0][(r[inf] < R)]
    wn = []
    for k in range(1, len(srcs)):
        v = np.zeros(x.size)
        v[inf] = resp[k]
        wn.append(v)
    return w, wn, pi * inf.sum()


def oracle_weights(sc, ev, use_energy):
    """True probabilities from the true model (true PSF, counts, background and diffuse)."""
    x, y, lab, E = ev
    inf = np.hypot(x, y) < RFIT
    def spec(kind):
        return spec_pdf(kind, E) if use_energy else 1.0
    tx, ty = sc.tgt_off
    dens = [sc.Nt * sc.psf_true.density(x - tx, y - ty) * spec("hard")]
    for (nx, ny, N), (ox, oy) in zip(sc.nbrs, sc.nbr_off):
        dens.append(N * sc.psf_true.density(x - nx - ox, y - ny - oy) * spec("hard"))
    bk = sc.beta * spec("flat")
    if sc.diffuse:
        bk = bk + sc.diffuse_density(x, y) * spec("soft")
    tot = np.sum(dens, axis=0) + bk
    w = np.where(inf, dens[0] / tot, 0.0)
    wn = [np.where(inf, d / tot, 0.0) for d in dens[1:]]
    return w, wn


def methods_for(sc, extra=()):
    m = {
        "hard 20\"": lambda ev: (aperture_weights(sc, ev, 20, False), None),
        "weighted 20\"": lambda ev: (aperture_weights(sc, ev, 20, True), None),
        "weighted 60\"": lambda ev: (aperture_weights(sc, ev, 60, True), None),
        "joint fit 60\"": lambda ev: fit_weights(sc, ev)[:2],
        "oracle": lambda ev: oracle_weights(sc, ev, sc.energy),
    }
    for e in extra:
        m.update(e)
    return m


# ---------------------------------------------------------------- metrics
def K_of(w, lab, j=0):
    s2 = (w * w).sum()
    return (w[lab == j].sum()) ** 2 / s2 if s2 > 0 else 0.0


def a_at(Ks, p):
    Ks = np.asarray(Ks)
    f = lambda a: np.mean(ncx2.sf(THR, 2, a * a * Ks / 2)) - p
    if f(1.0) < 0:
        return None      # undetectable even at 100% amplitude
    return brentq(f, 1e-4, 1.0)


def run(sc, nreal, rng, extra=(), leak=True):
    meth = methods_for(sc, extra)
    res = {k: {"K": [], "Nreg": [], "leak": [[] for _ in sc.nbrs]} for k in meth}
    own = [[] for _ in sc.nbrs]
    for _ in range(nreal):
        ev = sc.simulate(rng)
        lab = ev[2]
        wo, wno = oracle_weights(sc, ev, sc.energy)
        for j in range(len(sc.nbrs)):
            own[j].append(K_of(wno[j], lab, j + 1))
        for k, fn in meth.items():
            w, _ = fn(ev)
            res[k]["K"].append(K_of(w, lab, 0))
            res[k]["Nreg"].append(float(((w > 0) & (lab == 0)).sum()))
            for j in range(len(sc.nbrs)):
                res[k]["leak"][j].append(K_of(w, lab, j + 1))
    out = {"scenario": sc.name, "nreal": nreal, "threshold": THR, "methods": {}}
    base = None
    for k in meth:
        Ks = np.array(res[k]["K"])
        a50, a95 = a_at(Ks, 0.5), a_at(Ks, 0.95)
        d = {"K_mean": float(Ks.mean()), "K_sd": float(Ks.std()), "a50": a50, "a95": a95,
             "target_photons_in_region": float(np.mean(res[k]["Nreg"]))}
        if sc.nbrs:
            d["leak_fraction"] = [float(np.mean(res[k]["leak"][j]) / np.mean(own[j])) for j in range(len(sc.nbrs))]
        out["methods"][k] = d
    if sc.nbrs:
        out["neighbour_own_K"] = [float(np.mean(o)) for o in own]
    return out
