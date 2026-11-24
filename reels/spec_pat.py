from cta import Y
DUR = 47.8
MUSIC = "/home/user/repo/w/pat/music.mp3"
MUSIC_VOL = 0.26
YS, OY = 11, 12
def YY(p): return 1560 - p * YS + OY
EL, SFX = [], []

def seq(pts, per=2):
    """candles walking through waypoints; returns list of (o,h,l,c)"""
    cl = [pts[0]]
    for a, b in zip(pts, pts[1:]):
        for k in range(1, per + 1):
            cl.append(a + (b - a) * k / per)
    out = []
    for i in range(1, len(cl)):
        o, c = cl[i - 1], cl[i]
        wig = 1.4 + (i % 3) * 0.5
        out.append((o, max(o, c) + wig, min(o, c) - wig, c))
    return out

def place(cs, a0, b, span=4.0, x0=170, x1=910, grow=0.25):
    n = len(cs); dx = (x1 - x0) / max(1, n - 1); w = min(46, dx * 0.62)
    xs = [x0 + i * dx for i in range(n)]
    for i, o in enumerate(cs):
        EL.append(dict(k="candle", ohlc=o, x=xs[i], a=a0 + span * i / n, b=b, w=w, ys=YS, oy=OY, g=grow))
    return xs

def name(text, col, a, b):
    EL.append(dict(k="pill", text=text, col=col, size=50, x=540, y=1580, a=a, b=b))
    SFX.extend([("whoosh", a), ("pop", a + 0.05)])

# 1 head & shoulders  0 - 7.88
cs = seq([30, 55, 45, 75, 45, 60, 45, 25], 2); xs = place(cs, 0.0, 7.88, span=4.6)
EL += [dict(k="label", text="LEFT SHOULDER", x=xs[1], y=YY(62), size=22, col="white", a=1.3, b=7.88),
       dict(k="label", text="HEAD", x=xs[5], y=YY(82), size=26, col="white", a=2.4, b=7.88),
       dict(k="label", text="RIGHT SHOULDER", x=xs[9], y=YY(67), size=22, col="white", a=2.9, b=7.88),
       dict(k="hline", p=45, x1=150, x2=1000, col="gold", a=4.08, b=7.88, ys=YS, oy=OY),
       dict(k="label", text="NECKLINE", x=930, y=YY(45) - 24, size=24, col="gold", a=4.2, b=7.88),
       dict(k="arrow", x1=xs[-3] + 10, y1=YY(42), x2=xs[-1] + 60, y2=YY(18), col="red", a=5.84, b=7.88)]
name("HEAD AND SHOULDERS", "red", 0.0, 7.88); SFX += [("pop", 4.08), ("impact", 5.84)]
# 2 double top  7.88 - 14.42
cs = seq([35, 70, 52, 70, 52, 28], 2); xs = place(cs, 7.9, 14.42, span=3.2)
EL += [dict(k="hline", p=70.5, x1=150, x2=1000, col="red", a=9.64, b=14.42, ys=YS, oy=OY),
       dict(k="label", text="SAME HIGH × 2", x=900, y=YY(70) - 26, size=24, col="red", a=9.7, b=14.42),
       dict(k="hline", p=52, x1=150, x2=1000, col="gold", a=11.36, b=14.42, ys=YS, oy=OY),
       dict(k="label", text="LOW BETWEEN", x=910, y=YY(52) + 28, size=24, col="gold", a=11.4, b=14.42),
       dict(k="arrow", x1=xs[-2], y1=YY(46), x2=xs[-1] + 60, y2=YY(20), col="red", a=13.0, b=14.42)]
name("DOUBLE TOP", "red", 7.88, 14.42); SFX += [("pop", 9.64), ("pop", 11.36), ("impact", 13.0)]
# 3 double bottom  14.42 - 20.58
cs = seq([65, 30, 48, 30, 48, 72], 2); xs = place(cs, 14.45, 20.58, span=3.2)
EL += [dict(k="hline", p=29.5, x1=150, x2=1000, col="green", a=16.1, b=20.58, ys=YS, oy=OY),
       dict(k="label", text="SAME LOW × 2", x=900, y=YY(30) + 28, size=24, col="green", a=16.2, b=20.58),
       dict(k="hline", p=48, x1=150, x2=1000, col="gold", a=17.72, b=20.58, ys=YS, oy=OY),
       dict(k="label", text="HIGH BETWEEN", x=905, y=YY(48) - 24, size=24, col="gold", a=17.8, b=20.58),
       dict(k="arrow", x1=xs[-2], y1=YY(54), x2=xs[-1] + 60, y2=YY(82), col="green", a=19.0, b=20.58)]
name("DOUBLE BOTTOM", "green", 14.42, 20.58); SFX += [("pop", 16.1), ("pop", 17.72), ("impact", 19.0)]
# 4 bull flag  20.58 - 26.47
pole = seq([22, 70], 3); flag = seq([70, 62, 66, 58, 62, 55], 1); brk = seq([55, 84], 2)
xs = place(pole + flag + brk, 20.6, 26.47, span=4.2)
EL += [dict(k="seg", x1=xs[3], x2=xs[8], p1=72, p2=64, col="gold", dash=True, a=23.1, b=26.47, ys=YS, oy=OY),
       dict(k="seg", x1=xs[3], x2=xs[8], p1=60, p2=52, col="gold", dash=True, a=23.2, b=26.47, ys=YS, oy=OY),
       dict(k="label", text="POLE", x=xs[1] + 75, y=YY(46), size=24, col="green", a=21.5, b=26.47),
       dict(k="label", text="FLAG", x=xs[6], y=YY(76), size=24, col="gold", a=23.1, b=26.47),
       dict(k="arrow", x1=xs[-2] - 20, y1=YY(62), x2=xs[-1] + 50, y2=YY(90), col="green", a=24.92, b=26.47)]
name("BULL FLAG", "green", 20.58, 26.47); SFX += [("impact", 21.0), ("pop", 23.1), ("impact", 24.92)]
# 5 bear flag  26.47 - 32.56
pole = seq([80, 32], 3); flag = seq([32, 40, 36, 44, 40, 46], 1); brk = seq([46, 16], 2)
xs = place(pole + flag + brk, 26.5, 32.56, span=4.2)
EL += [dict(k="seg", x1=xs[3], x2=xs[8], p1=42, p2=50, col="gold", dash=True, a=29.04, b=32.56, ys=YS, oy=OY),
       dict(k="seg", x1=xs[3], x2=xs[8], p1=30, p2=38, col="gold", dash=True, a=29.1, b=32.56, ys=YS, oy=OY),
       dict(k="label", text="POLE", x=xs[1] + 75, y=YY(58), size=24, col="red", a=27.4, b=32.56),
       dict(k="label", text="FLAG", x=xs[6], y=YY(55), size=24, col="gold", a=29.0, b=32.56),
       dict(k="arrow", x1=xs[-2] - 20, y1=YY(40), x2=xs[-1] + 50, y2=YY(10), col="red", a=30.86, b=32.56)]
name("BEAR FLAG", "red", 26.47, 32.56); SFX += [("impact", 26.9), ("pop", 29.04), ("impact", 30.86)]
# 6 ascending triangle  32.56 - 38.94
cs = seq([30, 65, 42, 65, 50, 65, 57, 65, 84], 1); xs = place(cs, 32.6, 38.94, span=4.4)
EL += [dict(k="hline", p=66.5, x1=150, x2=1000, col="red", a=33.98, b=38.94, ys=YS, oy=OY),
       dict(k="label", text="FLAT HIGHS", x=910, y=YY(66) - 26, size=24, col="red", a=34.0, b=38.94),
       dict(k="seg", x1=xs[1], x2=xs[5], p1=40.5, p2=55.5, col="green", a=34.52, b=38.94, ys=YS, oy=OY),
       dict(k="label", text="RISING LOWS", x=xs[4] + 70, y=YY(40), size=24, col="green", a=34.6, b=38.94),
       dict(k="arrow", x1=xs[-2], y1=YY(70), x2=xs[-1] + 50, y2=YY(92), col="green", a=37.4, b=38.94)]
name("ASCENDING TRIANGLE", "green", 32.56, 38.94); SFX += [("pop", 33.98), ("pop", 34.52), ("impact", 37.4)]
# CTA: book + comment TRADING
EL += [dict(k="ui", ui="card", x=540, y=900, a=38.94, b=43.12, border="gold",
            lines=[["THE ULTIMATE COMPLETE", 48, "white"], ["TRADING A TO Z", 110, "gold"], ["320 pages · 15 parts · 250 chapters", 34, "gray"]]),
       dict(k="pill", text="ALL 6 PATTERNS INSIDE", col="green", size=44, x=540, y=1230, a=39.6, b=43.12),
       dict(k="ui", ui="profile", x=540, y=1010, a=43.12, b=DUR),
       dict(k="ui", ui="comment", x=540, y=1170, a=43.2, b=DUR, type="TRADING")]
SFX += [("whoosh", 38.94), ("impact", 39.0), ("pop", 39.6), ("whoosh", 43.12), ("pop", 43.6), ("ding", 44.7)]
HEAD = [(0, "PATTERN 1 / 6", "HEAD & SHOULDERS", "red"), (7.88, "PATTERN 2 / 6", "DOUBLE TOP", "red"), (14.42, "PATTERN 3 / 6", "DOUBLE BOTTOM", "green"),
        (20.58, "PATTERN 4 / 6", "BULL FLAG", "green"), (26.47, "PATTERN 5 / 6", "BEAR FLAG", "red"), (32.56, "PATTERN 6 / 6", "ASCENDING TRIANGLE", "green"),
        (38.94, "ALL 6 ARE IN", "MY BOOK", "orange"), (43.12, "WANT THE LINK? COMMENT", '"TRADING"', "orange"), (44.64, "FOLLOW SO IT", "REACHES YOUR DMS", "green")]
BG = [(0, "red"), (14.42, "green"), (26.47, "red"), (32.56, "green"), (38.94, "orange"), (44.64, "green")]
ZOOM = []
