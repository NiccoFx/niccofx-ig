from cta import cta, cs, Y
DUR = 28.0
EL = cs([(40,52,38,50),(50,64,48,62),(62,76,60,74),(74,86,72,84),(84,85,55,58)], 250, 110, 0.0, 2.12, stag=0.1, extra={4:(1.2,0.35)})
EL += [dict(k="pill", text="YOU BUY HERE", col="red", x=580, y=Y(94), a=0.5, b=2.12),
       dict(k="ring", x=580, y=Y(84), r=30, col="red", a=0.6, b=2.12),
       dict(k="big", text="50%", col="gold", size=380, x=540, y=960, a=2.3, b=3.96)]
C = [(30,40,22,38),(38,55,36,52),(52,70,50,68),(68,82,66,78),(78,79,62,64),(64,66,50,52),(52,54,38,40),(40,48,36,46),(46,62,44,60),(60,74,58,72)]
EL += cs(C, 150, 82, 4.0, 19.76, stag=0.1, extra={4:(5.0,0.25),5:(5.2,0.25),6:(6.5,0.3),7:(6.8,0.25),8:(14.6,0.3),9:(15.0,0.3)})
EL += [dict(k="hline", p=82, x1=120, x2=1000, col="gray", a=4.3, b=19.76), dict(k="label", text="SWING HIGH", x=900, y=Y(82)-26, size=24, col="gray", a=4.4, b=19.76),
       dict(k="hline", p=22, x1=120, x2=1000, col="gray", a=5.3, b=19.76), dict(k="label", text="SWING LOW", x=900, y=Y(22)+28, size=24, col="gray", a=5.4, b=19.76),
       dict(k="hline", p=52, x1=120, x2=1000, col="gold", dash=False, a=6.5, b=19.76), dict(k="label", text="50%", x=990, y=Y(52)-26, size=28, col="gold", a=6.6, b=19.76),
       dict(k="box", x1=120, x2=1000, p1=52, p2=82, col="red", fill=0.16, a=7.8, b=19.76), dict(k="label", text="PREMIUM", x=230, y=Y(77), size=30, col="red", a=7.9, b=19.76),
       dict(k="pill", text="SMART MONEY SELLS", col="red", x=560, y=Y(88), a=9.4, b=10.96),
       dict(k="box", x1=120, x2=1000, p1=22, p2=52, col="green", fill=0.16, a=10.96, b=19.76), dict(k="label", text="DISCOUNT", x=235, y=Y(27), size=30, col="green", a=11.0, b=19.76),
       dict(k="pill", text="SMART MONEY BUYS", col="green", x=560, y=Y(14), a=12.7, b=14.4),
       dict(k="ring", x=642, y=Y(40), r=34, col="green", a=15.3, b=16.9), dict(k="arrow", x1=700, y1=Y(42), x2=880, y2=Y(76), col="green", a=15.4, b=16.9),
       dict(k="pill", text="BUY HERE", col="green", x=642, y=Y(14), a=15.5, b=16.9),
       dict(k="ring", x=396, y=Y(78), r=34, col="red", a=17.8, b=19.76), dict(k="arrow", x1=440, y1=Y(74), x2=560, y2=Y(46), col="red", a=17.9, b=19.76),
       dict(k="pill", text="SELL HERE", col="red", x=396, y=Y(90), a=18.0, b=19.76)]
HEAD = [(0, "XAU/USD", "STOP BUYING AT THE TOP", "red"), (2.12, "HERE'S THE", "50% RULE", "gold"),
        (3.96, "STEP 1", "MARK HIGH & LOW", "white"), (6.4, "STEP 2", "SPLIT THE RANGE IN HALF", "gold"),
        (7.8, "TOP HALF =", "PREMIUM", "red"), (10.96, "BOTTOM HALF =", "DISCOUNT", "green"),
        (14.4, "IN AN UPTREND", "ONLY BUY IN DISCOUNT", "green"), (16.9, "IN A DOWNTREND", "ONLY SELL IN PREMIUM", "red")]
BG = [(0, "red"), (2.12, "orange"), (3.96, "orange"), (7.8, "red"), (10.96, "green"), (16.9, "red")]
ZOOM = [(7.9, 1.12, 540, Y(60)), (10.96, 1.12, 540, Y(44)), (14.4, 1.0, 540, 960), (19.76, 1.0, 540, 960)]
SFX = [("whoosh", t) for t in (2.12, 3.96, 6.4, 7.8, 10.96, 14.4, 16.9)] + [("pop", t) for t in (0.5, 4.4, 5.4, 6.6, 9.4, 12.7, 15.5, 18.0)] + [("impact", t) for t in (1.2, 2.3, 6.5)]
e, h, b, s = cta(19.76, 21.24, 21.62, 22.48, 25.44, DUR); EL += e; HEAD += h; BG += b; SFX += s
