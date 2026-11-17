from cta import cta, cs, Y
DUR = 30.4
base = [(40,48,38,46),(46,58,44,50),(50,56,46,54)]
L = base + [(54,70,50,52),(52,53,36,38),(38,40,30,32)]
R = base + [(54,72,53,70),(70,71,61,62),(62,80,61,78)]
EL = [dict(k="divider", x=540, y1=650, y2=1460, a=0.2, b=21.94),
      dict(k="label", text="ENDING A", x=290, y=690, size=30, col="red", a=1.2, b=21.94),
      dict(k="label", text="ENDING B", x=790, y=690, size=30, col="green", a=1.3, b=21.94),
      dict(k="hline", p=60, x1=90, x2=510, col="gray", a=0.3, b=21.94), dict(k="hline", p=60, x1=570, x2=1010, col="gray", a=0.3, b=21.94)]
for j, c in enumerate(L): EL.append(dict(k="candle", ohlc=c, x=120+j*65, w=42, a=[0.2,0.3,0.4,3.5,7.9,8.3][j], b=21.94, g=0.3))
for j, c in enumerate(R): EL.append(dict(k="candle", ohlc=c, x=620+j*65, w=42, a=[0.2,0.3,0.4,10.3,12.7,13.6][j], b=21.94, g=0.3))
EL += [dict(k="pill", text="WICK ABOVE", col="gold", fg=(20,20,22), x=315, y=Y(78), a=4.1, b=6.2),
       dict(k="pill", text="LIQUIDITY SWEEP", col="red", x=300, y=Y(80), a=6.26, b=21.94),
       dict(k="arrow", x1=470, y1=Y(50), x2=470, y2=Y(24), col="red", a=7.94, b=21.94),
       dict(k="pill", text="CLOSED ABOVE", col="green", x=815, y=Y(82), a=11.3, b=14.6),
       dict(k="ring", x=880, y=Y(61), r=30, col="gold", a=12.8, b=21.94),
       dict(k="pill", text="REAL BREAKOUT", col="green", x=800, y=Y(90), a=14.66, b=21.94),
       dict(k="ring", x=315, y=Y(54), r=30, col="red", a=16.6, b=21.94), dict(k="ring", x=815, y=Y(70), r=30, col="green", a=16.7, b=21.94)]
HEAD = [(0, "XAU/USD", "SAME MOVE", "white"), (1.14, "TWO DIFFERENT", "ENDINGS", "orange"),
        (2.68, "ON THE LEFT", "BREAKS, CLOSES BACK BELOW", "red"), (6.26, "THAT'S A", "LIQUIDITY SWEEP", "red"),
        (9.38, "ON THE RIGHT", "CLOSES ABOVE THE HIGH", "green"), (12.62, "THEN IT", "RETESTS AND HOLDS", "green"), (14.66, "THAT'S A", "REAL BREAKOUT", "green"),
        (16.48, "THE DIFFERENCE IS", "THE CLOSE", "orange"), (18.38, "WICK ABOVE =", "SWEEP", "red"), (20.14, "BODY ABOVE =", "BREAKOUT", "green")]
BG = [(0, "orange"), (2.68, "red"), (9.38, "green"), (16.48, "orange"), (18.38, "red"), (20.14, "green")]
ZOOM = []
SFX = [("whoosh", t) for t in (1.14, 2.68, 9.38, 16.48, 18.38, 20.14)] + [("pop", t) for t in (1.2, 1.3, 4.1, 6.26, 11.3, 14.66, 16.6, 16.7)] + [("impact", t) for t in (3.5, 7.94, 10.3)]
e, h, b, s = cta(21.94, 23.36, 23.84, 25.42, 27.94, DUR); EL += e; HEAD += h; BG += b; SFX += s
