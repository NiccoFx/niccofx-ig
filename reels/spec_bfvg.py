from cta import cta, Y
DUR = 47.6
EL, SFX = [], []
def C(o, x, a, b, w=96, ys=12, oy=160, g=0.35): return dict(k="candle", ohlc=o, x=x, a=a, b=b, w=w, ys=ys, oy=oy, g=g)
def YY(p, ys=12, oy=160): return 1560 - p * ys + oy
c1, c2 = (76, 82, 74, 80), (80, 81, 48, 52)
# hook: three mini setups
mini = [[c1, c2, (52, 62, 47, 50)], [c1, c2, (52, 56, 30, 32)], [c1, c2, (52, 68, 51, 66)]]
for g, cx in enumerate((220, 540, 860)):
    for j, o in enumerate(mini[g]):
        EL.append(C(o, cx - 52 + j * 52, 0.15 + g * 0.35 + j * 0.08, 9.16, w=36, ys=5, oy=-210, g=0.25))
EL += [dict(k="nums", x0=220, dx=320, y=820, a=0.2, b=9.16, col="red"),
       dict(k="big", text="30 SEC", col="gold", size=200, x=540, y=1400, a=6.86, b=9.16)]
SFX += [("pop", 0.2), ("pop", 0.45), ("pop", 0.7), ("whoosh", 4.18), ("impact", 6.86)]
# type 1: closes inside the wick
X6 = [300, 420, 540, 660, 780, 900]
T1 = [c1, c2, (52, 62, 47, 50), (50, 68, 49, 66), (66, 67, 40, 42), (42, 44, 34, 36)]
for j, o in enumerate(T1):
    a = [9.2, 9.4, 10.3, 14.0, 16.7, 17.1][j]
    EL.append(C(o, X6[j], a, 18.94, w=90))
EL += [dict(k="box", x1=360, x2=1000, p1=62, p2=74, col="red", fill=0.16, a=12.8, b=18.94, ys=12, oy=160),
       dict(k="label", text="FVG", x=950, y=YY(68), size=30, col="red", a=12.9, b=18.94),
       dict(k="ring", x=420, y=YY(49), r=34, col="gold", a=11.84, b=14.0),
       dict(k="pill", text="CLOSES INSIDE THE WICK", col="gold", fg=(20, 20, 22), x=540, y=YY(40), a=11.0, b=13.7),
       dict(k="hline", p=68, x1=360, x2=1000, col="gold", a=13.7, b=18.94, ys=12, oy=160),
       dict(k="pill", text="50%", col="gold", fg=(20, 20, 22), x=880, y=YY(68) - 50, a=14.6, b=16.66),
       dict(k="arrow", x1=700, y1=YY(64), x2=930, y2=YY(30), col="red", a=16.7, b=18.94)]
SFX += [("whoosh", 9.16), ("pop", 11.0), ("pop", 12.9), ("pop", 14.6), ("impact", 16.7)]
# type 2: breakaway gap
T2 = [c1, c2, (52, 56, 30, 32), (32, 34, 24, 26)]
for j, o in enumerate(T2):
    EL.append(C(o, [340, 470, 600, 730][j], [19.0, 19.2, 20.4, 24.1][j], 26.9, w=96, oy=100))
EL += [dict(k="box", x1=410, x2=1000, p1=56, p2=74, col="orange", fill=0.18, a=21.9, b=26.9, ys=12, oy=100),
       dict(k="pill", text="CLOSES FAR BELOW", col="red", x=600, y=YY(20, oy=100), a=20.9, b=22.58),
       dict(k="pill", text="NO PULLBACK", col="red", x=760, y=YY(64, oy=100), a=24.04, b=25.02),
       dict(k="pill", text="BREAKAWAY GAP", col="white", fg=(20, 20, 22), size=46, rot=-6, x=640, y=YY(65, oy=100), a=25.02, b=26.9),
       dict(k="arrow", x1=780, y1=YY(40, oy=100), x2=930, y2=YY(14, oy=100), col="red", a=24.1, b=26.9)]
SFX += [("whoosh", 18.94), ("pop", 20.9), ("pop", 24.04), ("impact", 25.02)]
# type 3: inverse FVG
T3 = [c1, c2, (52, 68, 51, 66), (66, 80, 65, 78), (78, 90, 76, 88)]
for j, o in enumerate(T3):
    EL.append(C(o, [320, 450, 580, 710, 840][j], [27.0, 27.2, 28.2, 32.6, 33.0][j], 37.06, w=96))
EL += [dict(k="box", x1=380, x2=1000, p1=56, p2=74, col="red", fill=0.14, a=27.6, b=37.06, ys=12, oy=160),
       dict(k="pill", text="GREEN 3RD CANDLE", col="green", x=580, y=YY(44), a=28.3, b=30.34),
       dict(k="pill", text="CLOSES INSIDE THE GAP", col="green", x=600, y=YY(44), a=30.34, b=32.58),
       dict(k="arrow", x1=640, y1=YY(60), x2=900, y2=YY(94), col="green", a=32.6, b=37.06),
       dict(k="pill", text="INVERSE FVG", col="white", fg=(20, 20, 22), size=46, rot=-6, x=600, y=YY(40), a=34.7, b=37.06)]
SFX += [("whoosh", 26.9), ("pop", 28.3), ("pop", 30.34), ("impact", 32.6), ("impact", 34.7)]
HEAD = [(0, "GOLD · XAU/USD", "3 BEARISH FVG", "red"), (4.18, "MOST TRADERS TAKE", "YEARS TO SEE IT", "orange"), (6.86, "YOU'LL LEARN IT IN", "30 SECONDS", "gold"),
        (9.16, "TYPE 1", "CLOSES INSIDE THE WICK", "red"), (13.7, "FIRST", "PULLBACK TO 50%", "gold"), (16.66, "THEN", "THE MOVE DOWN CONTINUES", "red"),
        (18.94, "TYPE 2", "CLOSES FAR BELOW", "red"), (22.58, "SELLERS ARE", "STRONG", "red"), (25.02, "THIS IS A", "BREAKAWAY GAP", "orange"),
        (26.9, "TYPE 3", "GREEN CANDLE IN THE GAP", "green"), (30.98, "BUYERS ARE", "STRONG", "green"), (32.58, "PRICE", "FILLS & REVERSES", "green"), (34.7, "THIS IS AN", "INVERSE FVG", "orange")]
BG = [(0, "red"), (4.18, "orange"), (9.16, "red"), (13.7, "orange"), (16.66, "red"), (25.02, "orange"), (26.9, "green"), (34.7, "orange")]
ZOOM = []
e, h, b, s = cta(37.06, 38.5, 39.04, 40.72, 43.96, DUR); EL += e; HEAD += h; BG += b; SFX += s
