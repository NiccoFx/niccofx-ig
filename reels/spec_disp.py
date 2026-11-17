from cta import cta, cs, Y
DUR = 28.5
EL = cs([(50,58,44,52),(52,60,45,49),(49,57,43,53)], 300, 120, 0.0, 1.86, stag=0.1)
EL += [dict(k="candle", ohlc=(53,90,52,88), x=660, w=90, a=0.9, b=1.86, g=0.4)]
EL += [dict(k="divider", x=540, y1=600, y2=1460, a=3.3, b=17.76),
       dict(k="label", text="NORMAL", x=290, y=640, size=32, col="gray", a=3.4, b=17.76),
       dict(k="label", text="DISPLACEMENT", x=790, y=640, size=32, col="green", a=8.0, b=17.76)]
for j, c in enumerate([(50,64,38,53),(53,66,42,50),(50,63,40,54),(54,65,44,51)]):
    EL.append(dict(k="candle", ohlc=c, x=150+j*95, w=50, a=3.5+j*0.15, b=17.76, g=0.3))
EL += [dict(k="label", text="BODY", x=100, y=1360, size=24, col="gray", anchor="lm", a=4.3, b=17.76),
       dict(k="bar", x=100, y=1385, w=380, h=24, frac=0.25, col="gray", a=4.3, b=17.76),
       dict(k="label", text="25%", x=480, y=1360, size=24, col="gray", anchor="rm", a=4.5, b=17.76),
       dict(k="pill", text="LONG WICKS", col="orange", x=290, y=Y(74), a=5.2, b=6.6),
       dict(k="pill", text="UNDECIDED", col="orange", x=290, y=Y(74), a=6.66, b=17.76),
       dict(k="candle", ohlc=(40,42,34,38), x=650, w=60, a=8.0, b=17.76, g=0.25),
       dict(k="candle", ohlc=(38,96,37,94), x=760, w=100, a=8.3, b=17.76, g=0.6),
       dict(k="candle", ohlc=(94,99,90,97), x=880, w=60, a=12.9, b=17.76, g=0.25),
       dict(k="label", text="BODY", x=600, y=1360, size=24, col="green", anchor="lm", a=9.3, b=17.76),
       dict(k="bar", x=600, y=1385, w=380, h=24, frac=0.95, col="green", a=9.3, b=17.76),
       dict(k="label", text="95%", x=980, y=1360, size=24, col="green", anchor="rm", a=9.6, b=17.76),
       dict(k="pill", text="CLOSES NEAR THE HIGH", col="green", x=760, y=Y(103), a=11.4, b=13.2),
       dict(k="box", x1=650, x2=1010, p1=42, p2=90, col="gold", fill=0.16, a=13.5, b=17.76),
       dict(k="pill", text="FAIR VALUE GAP", col="gold", fg=(20,20,22), x=900, y=Y(66), a=13.6, b=17.76),
       dict(k="arrow", x1=1010, y1=Y(70), x2=1010, y2=Y(100), col="green", a=17.9, b=20.76),
       dict(k="pill", text="NOT AGAINST IT", col="red", x=290, y=Y(28), a=19.62, b=20.76)]
HEAD = [(0, "WANT TO SEE WHERE", "BIG MONEY IS?", "gold"), (1.86, "LOOK FOR", "DISPLACEMENT", "green"),
        (3.38, "A NORMAL CANDLE", "SMALL BODY, LONG WICKS", "orange"), (6.28, "PRICE IS", "UNDECIDED", "orange"),
        (7.98, "A DISPLACEMENT CANDLE", "HUGE, ALMOST NO WICKS", "green"), (11.36, "IT CLOSES", "NEAR ITS HIGH", "green"),
        (12.94, "AND LEAVES A", "FAIR VALUE GAP", "gold"), (15.16, "THAT'S INSTITUTIONS", "MOVING PRICE FAST", "green"),
        (17.76, "TRADE WITH", "DISPLACEMENT", "green")]
BG = [(0, "orange"), (1.86, "green"), (3.38, "orange"), (7.98, "green"), (12.94, "orange"), (15.16, "green")]
ZOOM = [(8.0, 1.25, 790, Y(66)), (15.16, 1.0, 540, 960), (20.76, 1.0, 540, 960)]
SFX = [("whoosh", t) for t in (1.86, 3.38, 7.98, 12.94, 15.16, 17.76)] + [("pop", t) for t in (3.4, 5.2, 6.66, 11.4, 13.6, 19.62)] + [("impact", t) for t in (0.9, 8.3, 13.5)]
e, h, b, s = cta(20.76, 22.22, 22.58, 23.98, 26.1, DUR); EL += e; HEAD += h; BG += b; SFX += s
