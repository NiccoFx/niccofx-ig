"""NiccoFX reel engine v4 (Claude Code style). Usage: SPEC=<module> python3 eng.py out.mp4 [--preview t1,t2,...]"""
import math, sys, os, subprocess, importlib
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
S = importlib.import_module(os.environ.get("SPEC", "spec"))

GREEN = (34, 197, 94); RED = (239, 68, 68); ORANGE = (249, 146, 32); GOLD = (250, 204, 21)
BLUE = (59, 130, 246); WHITE = (245, 246, 248); GRAY = (150, 156, 168); DIM = (90, 96, 108)
COL = dict(green=GREEN, red=RED, orange=ORANGE, gold=GOLD, blue=BLUE, white=WHITE, gray=GRAY)


def c(x):
    return COL[x] if isinstance(x, str) else tuple(x)


_fc = {}


def F(name, size, var=None):
    k = (name, size, var)
    if k not in _fc:
        f = ImageFont.truetype(f"{HERE}/fonts/{name}.ttf", size)
        if var:
            try:
                f.set_variation_by_name(var)
            except Exception:
                pass
        _fc[k] = f
    return _fc[k]


def cl(x): return max(0.0, min(1.0, x))
def ease(x): x = cl(x); return 1 - (1 - x) ** 3


def back(x):
    x = cl(x); s = 1.7; x -= 1
    return x * x * ((s + 1) * x + s) + 1


def win(t, a, b, fi=0.15, fo=0.15):
    if t < a or t > b:
        return 0.0
    return min(cl((t - a) / fi) if fi > 0 else 1, cl((b - t) / fo) if fo > 0 else 1)


def Y(p): return 1560 - p * 10


# ---------- background ----------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
G = np.exp(-(((xx - W / 2) / 820) ** 2 + ((yy - 760) / 900) ** 2) * 1.6)[..., None]
VIG = (1 - 0.55 * np.clip((((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2) * 2.2, 0, 1))[..., None]
BASE = np.array([7, 9, 12], np.float32)


def bg_color(t):
    seq = S.BG; cur = c(seq[0][1])
    for i, (t0, col) in enumerate(seq):
        if t >= t0:
            prev = c(seq[i - 1][1]) if i else c(col); k = ease((t - t0) / 0.45)
            cur = tuple(prev[j] + (c(col)[j] - prev[j]) * k for j in range(3))
    return cur


_bgc = {}


def background(t):
    col = tuple(int(v) for v in bg_color(t)); key = tuple(v // 3 for v in col)
    if key not in _bgc:
        arr = (BASE + G * np.array(col, np.float32) * 0.30) * VIG
        _bgc[key] = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
        if len(_bgc) > 400:
            _bgc.clear()
    return _bgc[key].copy()


# ---------- tiles ----------
_tc = {}


def tile(text, font, col, glow=22, ga=0.75):
    k = (text, font.path, font.size, col, glow, ga)
    if k in _tc:
        return _tc[k]
    bb = font.getbbox(text); w = bb[2] - bb[0] + glow * 4; h = bb[3] - bb[1] + glow * 4
    t = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.text((glow * 2 - bb[0], glow * 2 - bb[1]), text, font=font, fill=col + (255,))
    g = t.filter(ImageFilter.GaussianBlur(glow)); a = np.array(g); a[..., 3] = (a[..., 3] * ga).astype(np.uint8)
    out = Image.alpha_composite(Image.fromarray(a), t)
    _tc[k] = out
    return out


def paste(img, t, cx, cy, scale=1.0, alpha=1.0, rot=0):
    if alpha <= 0.01:
        return
    if scale != 1.0:
        t = t.resize((max(1, int(t.width * scale)), max(1, int(t.height * scale))), Image.BILINEAR)
    if rot:
        t = t.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1:
        a = np.array(t); a[..., 3] = (a[..., 3] * alpha).astype(np.uint8); t = Image.fromarray(a)
    img.alpha_composite(t, (int(cx - t.width / 2), int(cy - t.height / 2)))


_pc = {}


def pill_tile(text, col, size=34, fg=(255, 255, 255), pad=(26, 14)):
    k = (text, col, size, fg)
    if k in _pc:
        return _pc[k]
    f = F("Inter", size, "ExtraBold"); bb = f.getbbox(text); tw = bb[2] - bb[0]; th = bb[3] - bb[1]
    w = tw + pad[0] * 2; h = th + pad[1] * 2; m = 30
    t = Image.new("RGBA", (w + m * 2, h + m * 2), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.rounded_rectangle([m, m, m + w, m + h], radius=h // 2 if size < 50 else 18, fill=col + (255,))
    g = t.filter(ImageFilter.GaussianBlur(14)); a = np.array(g); a[..., 3] = (a[..., 3] * 0.65).astype(np.uint8)
    t = Image.alpha_composite(Image.fromarray(a), t); d = ImageDraw.Draw(t)
    d.text((m + pad[0] - bb[0], m + pad[1] - bb[1]), text, font=f, fill=fg)
    _pc[k] = t
    return t


_LOGO = {}


def logo(size):
    if size not in _LOGO:
        im = Image.open(f"{HERE}/logo_tile.png").convert("RGBA"); im.thumbnail((size, size), Image.LANCZOS); _LOGO[size] = im
    return _LOGO[size]


# ---------- chart ----------
def draw_candle(d, e, t):
    k = ease((t - e["a"]) / e.get("g", 0.25))
    if k <= 0:
        return
    o, h, l, cc = e["ohlc"]; x = e["x"]; w = e.get("w", 70)
    col = GREEN if cc >= o else RED
    cur = o + (cc - o) * k
    hi = max(o, cur) + (h - max(o, cc)) * k if h > max(o, cc) else max(o, cur)
    lo = min(o, cur) - (min(o, cc) - l) * k
    al = int(255 * e.get("op", 1))
    d.line([x, Y(hi), x, Y(lo)], fill=col + (al,), width=7)
    y1, y2 = sorted([Y(o), Y(cur)])
    d.rectangle([x - w / 2, y1, x + w / 2, max(y2, y1 + 4)], fill=col + (al,))


def dashed(d, x1, y, x2, col, al=255, w=4, dash=22, gap=14):
    x = x1
    while x < x2:
        d.line([x, y, min(x + dash, x2), y], fill=col + (al,), width=w); x += dash + gap


CHART_KINDS = ("candle", "hline", "box", "ring", "bracket", "arrow", "dots")


def draw_chart(img, t, els):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); any_ = False
    for e in els:
        k = e["k"]; A = win(t, e["a"], e["b"])
        if A <= 0:
            continue
        any_ = True; al = int(255 * A)
        if k == "candle":
            ee = dict(e); ee["op"] = A * e.get("op", 1); draw_candle(d, ee, t)
        elif k == "hline":
            g = ease((t - e["a"]) / 0.35); x2 = e["x1"] + (e["x2"] - e["x1"]) * g; col = c(e["col"])
            if e.get("dash", True):
                dashed(d, e["x1"], Y(e["p"]), x2, col, int(al * 0.9))
            else:
                d.line([e["x1"], Y(e["p"]), x2, Y(e["p"])], fill=col + (al,), width=4)
        elif k == "box":
            col = c(e["col"]); y1, y2 = sorted([Y(e["p1"]), Y(e["p2"])])
            d.rectangle([e["x1"], y1, e["x2"], y2], fill=col + (int(al * e.get("fill", 0.14)),), outline=col + (int(al * 0.7),), width=3)
        elif k == "ring":
            r = e.get("r", 34) * (0.6 + 0.4 * back((t - e["a"]) / 0.3)); col = c(e["col"])
            d.ellipse([e["x"] - r, e["y"] - r, e["x"] + r, e["y"] + r], outline=col + (al,), width=6)
        elif k == "bracket":
            col = c(e["col"]); g = ease((t - e["a"]) / 0.3); x = e["x"]
            y1, y2 = sorted([Y(e["p1"]), Y(e["p2"])]); m = (y1 + y2) / 2; hh = (y2 - y1) / 2 * g
            d.line([x, m - hh, x, m + hh], fill=col + (al,), width=5)
            d.line([x - 14, m - hh, x, m - hh], fill=col + (al,), width=5); d.line([x - 14, m + hh, x, m + hh], fill=col + (al,), width=5)
        elif k == "arrow":
            col = c(e["col"]); g = ease((t - e["a"]) / 0.4); x1, y1, x2, y2 = e["x1"], e["y1"], e["x2"], e["y2"]
            xe, ye = x1 + (x2 - x1) * g, y1 + (y2 - y1) * g; d.line([x1, y1, xe, ye], fill=col + (al,), width=8)
            ang = math.atan2(ye - y1, xe - x1)
            for s in (-1, 1):
                d.line([xe, ye, xe - 34 * math.cos(ang + s * 0.5), ye - 34 * math.sin(ang + s * 0.5)], fill=col + (al,), width=8)
        elif k == "dots":
            col = c(e["col"])
            for j, (x, p) in enumerate(e["pts"]):
                aa = int(al * cl((t - e["a"] - j * 0.05) / 0.15)); d.ellipse([x - 9, Y(p) - 9, x + 9, Y(p) + 9], fill=col + (aa,))
    if not any_:
        return
    small = lay.resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(7)).resize((W, H), Image.BILINEAR)
    a = np.array(small); a[..., 3] = np.clip(a[..., 3].astype(np.float32) * 1.1, 0, 255).astype(np.uint8)
    img.alpha_composite(Image.fromarray(a)); img.alpha_composite(lay)


# ---------- UI mockups ----------
_uc = {}


def rr(d, box, r, fill, outline=None, w=3): d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=w)


def ui_pdf(t, e):
    if "pdf" in _uc:
        return _uc["pdf"]
    w, h = 420, 540; m = 40; im = Image.new("RGBA", (w + 2 * m, h + 2 * m), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [m, m, m + w, m + h], 24, (246, 246, 244, 255))
    g = im.filter(ImageFilter.GaussianBlur(18)); a = np.array(g); a[..., :3] = np.array(ORANGE); a[..., 3] = (a[..., 3] * 0.45).astype(np.uint8)
    im = Image.alpha_composite(Image.fromarray(a), im); d = ImageDraw.Draw(im)
    rr(d, [m + 30, m + 30, m + 120, m + 76], 10, RED + (255,)); d.text((m + 75, m + 53), "PDF", font=F("Inter", 28, "ExtraBold"), fill=(255, 255, 255), anchor="mm")
    y = m + 110
    for line in ["SMART", "MONEY", "ACTION"]:
        d.text((m + 30, y), line, font=F("Anton", 74), fill=(20, 22, 26)); y += 78
    d.text((m + 32, y + 12), "FREE 15-PAGE GOLD PLAYBOOK", font=F("Inter", 22, "ExtraBold"), fill=ORANGE)
    for k in range(3):
        rr(d, [m + 30, y + 60 + k * 30, m + w - 30 - (k * 60), y + 74 + k * 30], 7, (214, 216, 220, 255), None)
    rr(d, [m + 30, m + h - 70, m + w - 30, m + h - 30], 12, GREEN + (255,))
    _uc["pdf"] = im
    return im


def ui_profile(t, e):
    if "prof" in _uc:
        return _uc["prof"]
    w, h = 680, 150; im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    im.alpha_composite(logo(100), (10, 25)); d = ImageDraw.Draw(im)
    d.text((135, 52), "NiccoFX", font=F("Inter", 40, "ExtraBold"), fill=WHITE, anchor="lm")
    d.text((135, 100), "Gold trading, made simple", font=F("Inter", 26, "Medium"), fill=GRAY, anchor="lm")
    rr(d, [w - 200, 45, w - 10, 105], 16, BLUE + (255,)); d.text((w - 105, 75), "Follow", font=F("Inter", 32, "ExtraBold"), fill=(255, 255, 255), anchor="mm")
    _uc["prof"] = im
    return im


def ui_comment(t, e):
    txt = e.get("type", "SMA"); n = int(cl((t - e["a"] - 0.2) / 0.5) * len(txt) + 0.0001); k = ("cm", txt, n)
    if k in _uc:
        return _uc[k]
    w, h = 800, 110; im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [0, 0, w - 1, h - 1], 55, (24, 27, 34, 255), (64, 70, 82, 255), 3)
    d.ellipse([20, 22, 86, 88], fill=(44, 48, 58, 255)); d.text((53, 55), "YOU", font=F("Inter", 18, "ExtraBold"), fill=GRAY, anchor="mm")
    d.text((110, 55), txt[:n] if n else "Add a comment...", font=F("Inter", 38, "ExtraBold" if n else "Medium"), fill=WHITE if n else DIM, anchor="lm")
    d.ellipse([w - 92, 18, w - 18, 92], fill=BLUE + (255,)); d.text((w - 55, 55), ">", font=F("Inter", 40, "ExtraBold"), fill=(255, 255, 255), anchor="mm")
    _uc[k] = im
    return im


def ui_dm(t, e):
    ok = e.get("ok", False); k = ("dm", ok)
    if k in _uc:
        return _uc[k]
    w, h = 780, 430; m = 40; im = Image.new("RGBA", (w + 2 * m, h + 2 * m), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [m, m, m + w, m + h], 30, (20, 23, 29, 255), (GREEN if ok else (60, 65, 76)) + (255,), 4 if ok else 3)
    if ok:
        g = im.filter(ImageFilter.GaussianBlur(20)); a = np.array(g); a[..., 3] = (a[..., 3] * 0.35).astype(np.uint8)
        im = Image.alpha_composite(Image.fromarray(a), im); d = ImageDraw.Draw(im)
    d.text((m + w / 2, m + 40), "Messages", font=F("Inter", 26, "Bold"), fill=GRAY, anchor="mm")
    im.alpha_composite(logo(80), (m + 30, m + 75)); d = ImageDraw.Draw(im)
    d.text((m + 130, m + 97), "NiccoFX", font=F("Inter", 34, "ExtraBold"), fill=WHITE, anchor="lm")
    d.text((m + 130, m + 135), "@niccofx", font=F("Inter", 24, "Medium"), fill=GRAY, anchor="lm")
    if ok:
        rr(d, [m + w - 220, m + 88, m + w - 30, m + 142], 14, (44, 48, 58, 255)); d.text((m + w - 125, m + 115), "Following", font=F("Inter", 28, "Bold"), fill=WHITE, anchor="mm")
    else:
        rr(d, [m + w - 200, m + 88, m + w - 30, m + 142], 14, BLUE + (255,)); d.text((m + w - 115, m + 115), "Follow", font=F("Inter", 28, "ExtraBold"), fill=(255, 255, 255), anchor="mm")
    bx = [m + 30, m + 185, m + w - 150, m + 335]; rr(d, bx, 22, (32, 36, 44, 255), (GREEN if ok else (60, 65, 76)) + (255,), 3)
    rr(d, [bx[0] + 24, bx[1] + 28, bx[0] + 104, bx[1] + 122], 10, (240, 240, 238, 255)); rr(d, [bx[0] + 24, bx[1] + 28, bx[0] + 70, bx[1] + 52], 6, RED + (255,))
    d.text((bx[0] + 130, bx[1] + 55), "Smart_Money_Action.pdf", font=F("Inter", 30, "ExtraBold"), fill=WHITE, anchor="lm")
    d.text((bx[0] + 130, bx[1] + 98), "PDF · free guide", font=F("Inter", 24, "Medium"), fill=GRAY, anchor="lm")
    d.text((m + 34, m + 380), "Delivered ✓" if ok else "Not delivered", font=F("Inter", 28, "ExtraBold"), fill=GREEN if ok else RED, anchor="lm")
    _uc[k] = im
    return im


def ui_card(t, e):
    """Generic big number/stat card: e['lines']=[(text,size,col),...]"""
    k = ("card", tuple(map(tuple, e["lines"])), e.get("border", "gray"))
    if k in _uc:
        return _uc[k]
    w = e.get("w", 760); hs = [ln[1] * 1.25 for ln in e["lines"]]; h = int(sum(hs) + 80); m = 40
    im = Image.new("RGBA", (w + 2 * m, h + 2 * m), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    rr(d, [m, m, m + w, m + h], 28, (18, 21, 28, 240), c(e.get("border", "gray")) + (255,), 3)
    y = m + 40
    for (txt, sz, col), hh in zip(e["lines"], hs):
        f = F("Anton", sz) if sz >= 60 else F("Inter", sz, "ExtraBold")
        d.text((m + w / 2, y + hh / 2), txt, font=f, fill=c(col), anchor="mm"); y += hh
    _uc[k] = im
    return im


UI = dict(pdf=ui_pdf, profile=ui_profile, comment=ui_comment, dm=ui_dm, card=ui_card)

_ct = {}


def chip_tile(lab):
    if lab in _ct:
        return _ct[lab]
    w, h = 150, 170; t = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.rounded_rectangle([20, 20, 20 + w, 20 + h], radius=22, fill=(245, 245, 247, 255))
    d.rounded_rectangle([20, 20, 20 + w, 62], radius=22, fill=RED + (255,)); d.rectangle([20, 45, 20 + w, 62], fill=RED + (255,))
    d.text((20 + w / 2, 20 + h / 2 + 22), lab, font=F("Inter", 40, "ExtraBold"), fill=(20, 22, 26), anchor="mm")
    _ct[lab] = t
    return t


_nt = {}


def num_tile(n, col=ORANGE):
    k = (n, col)
    if k in _nt:
        return _nt[k]
    t = Image.new("RGBA", (220, 220), (0, 0, 0, 0)); d = ImageDraw.Draw(t)
    d.ellipse([30, 30, 190, 190], fill=col + (255,)); g = t.filter(ImageFilter.GaussianBlur(16)); t = Image.alpha_composite(g, t); d = ImageDraw.Draw(t)
    d.text((110, 112), str(n), font=F("Anton", 100), fill=(16, 16, 18), anchor="mm"); _nt[k] = t
    return t


UI_KINDS = ("pill", "label", "chips", "nums", "ui", "big")


def draw_ui_layer(img, t, els):
    for e in els:  # mockups first, so pills/stamps sit on top
        if e["k"] != "ui":
            continue
        A = win(t, e["a"], e["b"])
        if A > 0:
            g = back((t - e["a"]) / 0.35); paste(img, UI[e["ui"]](t, e), e["x"], e["y"], e.get("s", 1) * (0.75 + 0.25 * g), A, e.get("rot", 0))
    d = ImageDraw.Draw(img)
    for e in els:
        k = e["k"]
        if k == "ui":
            continue
        A = win(t, e["a"], e["b"])
        if A <= 0:
            continue
        if k == "pill":
            s = e.get("s", 1.0) * (0.5 + 0.5 * back((t - e["a"]) / 0.28))
            paste(img, pill_tile(e["text"], c(e["col"]), e.get("size", 34), tuple(e.get("fg", (255, 255, 255)))), e["x"], e["y"], s, A, e.get("rot", 0))
        elif k == "label":
            d.text((e["x"], e["y"]), e["text"], font=F("Inter", e.get("size", 28), "Bold"), fill=c(e.get("col", "gray")) + (int(255 * A),), anchor=e.get("anchor", "mm"))
        elif k == "big":
            s = 0.6 + 0.4 * back((t - e["a"]) / 0.3)
            paste(img, tile(e["text"], F("Anton", e.get("size", 200)), c(e["col"]), glow=30, ga=0.8), e["x"], e["y"], s, A)
        elif k == "chips":
            for j, lab in enumerate(e["items"]):
                tj = e["a"] + j * e.get("st", 0.22)
                if t >= tj:
                    paste(img, chip_tile(lab), e["x0"] + j * e["dx"], e["y"], 0.4 + 0.6 * back((t - tj) / 0.3), A)
        elif k == "nums":
            for j in range(e.get("n", 3)):
                tj = e["a"] + j * 0.25
                if t >= tj:
                    paste(img, num_tile(j + 1, c(e.get("col", "orange"))), e["x0"] + j * e["dx"], e["y"], 0.3 + 0.7 * back((t - tj) / 0.3), A)


# ---------- headline / chrome ----------
def draw_head(img, t):
    cur = None
    for i, h in enumerate(S.HEAD):
        if t >= h[0]:
            cur = (i, h)
    if not cur:
        return
    i, (t0, kick, text, col) = cur
    t1 = S.HEAD[i + 1][0] if i + 1 < len(S.HEAD) else 999
    A = win(t, t0, t1, 0.12, 0.08)
    if not text:
        return
    d = ImageDraw.Draw(img)
    if kick:
        f = F("Inter", 30, "Bold"); sp = " ".join(kick.upper()); tw = d.textlength(sp, font=f); ka = int(255 * A * 0.9); y = 300
        d.text((W / 2, y), sp, font=f, fill=(200, 204, 212, ka), anchor="mm")
        d.line([W / 2 - tw / 2 - 90, y, W / 2 - tw / 2 - 24, y], fill=(200, 204, 212, ka), width=3)
        d.line([W / 2 + tw / 2 + 24, y, W / 2 + tw / 2 + 90, y], fill=(200, 204, 212, ka), width=3)
    size = 118; f = F("Anton", size)
    while f.getlength(text) > 960 and size > 60:
        size -= 4; f = F("Anton", size)
    s = 1.0 + 0.10 * (1 - ease((t - t0) / 0.22))
    paste(img, tile(text, f, c(col)), W / 2, 400, s, A)


def draw_top(img):
    d = ImageDraw.Draw(img); f = F("Inter", 30, "Bold")
    tw = d.textlength("@niccofx", font=f); L = logo(46); x0 = W / 2 - (tw + 56) / 2
    img.alpha_composite(L, (int(x0), int(88 - L.height / 2)))
    ImageDraw.Draw(img).text((x0 + 56, 88), "@niccofx", font=f, fill=(190, 196, 206, 230), anchor="lm")


def frame(t):
    img = background(t).convert("RGBA")
    draw_top(img)
    draw_chart(img, t, [e for e in S.EL if e["k"] in CHART_KINDS])
    draw_ui_layer(img, t, [e for e in S.EL if e["k"] in UI_KINDS])
    draw_head(img, t)
    foot = getattr(S, "FOOT", "Education only · Not financial advice")
    if foot:
        ImageDraw.Draw(img).text((W / 2, 1840), foot, font=F("Inter", 22, "Medium"), fill=(110, 116, 128, 200), anchor="mm")
    return img.convert("RGB")


def _r(k): return frame(k / FPS).tobytes()


if __name__ == "__main__":
    out = sys.argv[1]
    if "--preview" in sys.argv:
        ts = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
        for i, t in enumerate(ts):
            frame(t).save(f"pv_{i}.png")
        sys.exit()
    n = int(S.DUR * FPS)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", out], stdin=subprocess.PIPE)
    from multiprocessing import Pool
    with Pool(os.cpu_count()) as pool:
        for b in pool.imap(_r, range(n), chunksize=4):
            p.stdin.write(b)
    p.stdin.close(); p.wait(); print("done", out, n / FPS)
