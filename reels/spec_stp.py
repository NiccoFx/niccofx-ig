from cta import cta, cs, Y
DUR = 31.7
EL = cs([(66,70,60,62),(62,64,55,57),(57,59,52,54),(54,55,46,48),(48,50,40,42),(42,44,35,37),(37,39,28,30)], 150, 110, 0.2, 5.22, stag=0.08, extra={3:(1.2,0.3),4:(2.0,0.3),5:(3.0,0.3),6:(4.0,0.3)})
EL += [dict(k="hline", p=62, x1=120, x2=1000, col="gold", dash=False, a=0.2, b=7.64), dict(k="label", text="ENTRY", x=950, y=Y(62)-26, size=24, col="gold", a=0.3, b=7.64),
       dict(k="hline", p=50, x1=120, x2=1000, col="red", a=0.4, b=2.54), dict(k="label", text="STOP", x=960, y=Y(50)+26, size=24, col="red", a=0.5, b=2.54),
       dict(k="hline", p=40, x1=120, x2=1000, col="red", a=2.54, b=3.56), dict(k="label", text="STOP (MOVED)", x=910, y=Y(40)+26, size=24, col="red", a=2.6, b=3.56),
       dict(k="hline", p=26, x1=120, x2=1000, col="red", a=3.56, b=7.64), dict(k="label", text="STOP (MOVED AGAIN)", x=880, y=Y(26)+26, size=24, col="red", a=3.6, b=7.64),
       dict(k="bar", x=140, y=1440, w=800, h=28, frac=0.25, col="red", a=0.5, b=2.54),
       dict(k="bar", x=140, y=1440, w=800, h=28, frac=0.55, col="red", a=2.54, b=3.56),
       dict(k="bar", x=140, y=1440, w=800, h=28, frac=0.95, col="red", a=3.56, b=7.64),
       dict(k="label", text="YOUR LOSS", x=140, y=1410, size=24, col="red", anchor="lm", a=0.5, b=7.64),
       dict(k="big", text="-1R → -3R", col="red", size=150, x=540, y=760, a=5.4, b=7.64),
       dict(k="nums", x0=290, dx=250, y=960, a=7.9, b=9.54)]
EL += cs([(50,58,48,56),(56,60,52,53),(53,55,40,42),(42,58,41,56),(56,64,54,62),(62,66,58,60)], 180, 120, 9.6, 14.56, stag=0.1)
EL += [dict(k="hline", p=37, x1=120, x2=1000, col="green", dash=False, a=10.9, b=14.56), dict(k="label", text="IDEA IS WRONG HERE", x=760, y=Y(37)+28, size=24, col="green", a=11.0, b=14.56),
       dict(k="hline", p=53, x1=500, x2=1000, col="red", a=12.6, b=14.56), dict(k="label", text="PAIN STARTS HERE", x=800, y=Y(53)+28, size=24, col="red", a=12.7, b=14.56),
       dict(k="pill", text="STOP GOES HERE", col="green", x=420, y=Y(28), a=11.3, b=14.56),
       dict(k="ui", ui="card", x=540, y=930, a=15.3, b=19.52, border="green", lines=[["SIZE FROM THE STOP", 44, "white"], ["$100 risk ÷ $10 stop", 38, "gray"], ["= 0.1 LOTS", 100, "green"]]),
       dict(k="pill", text="LOSS IS ALREADY OK", col="green", size=40, x=540, y=1230, a=18.32, b=19.52),
       dict(k="big", text="SET IT.", col="white", size=170, x=540, y=830, a=20.22, b=23.58),
       dict(k="big", text="WALK AWAY.", col="green", size=170, x=540, y=1050, a=21.04, b=23.58),
       dict(k="pill", text="DON'T WATCH EVERY CANDLE", col="red", size=40, x=540, y=1280, a=22.04, b=23.58)]
HEAD = [(0, "YOU SET YOUR STOP", "PRICE GETS CLOSE", "orange"), (2.54, "YOU", "MOVE IT", "red"), (3.56, "THEN YOU", "MOVE IT AGAIN", "red"),
        (5.22, "NOW A SMALL LOSS", "IS A BIG ONE", "red"), (7.64, "HERE'S HOW I", "STOPPED DOING THAT", "orange"),
        (9.54, "RULE 1", "STOP = WHERE YOU'RE WRONG", "green"), (14.56, "RULE 2", "SIZE FROM THE STOP", "green"),
        (19.52, "RULE 3", "SET IT AND WALK AWAY", "green")]
BG = [(0, "orange"), (2.54, "red"), (7.64, "orange"), (9.54, "green")]
ZOOM = [(0.0, 1.0, 540, 960), (2.54, 1.15, 540, Y(44)), (5.22, 1.0, 540, 960)]
SFX = [("whoosh", t) for t in (2.54, 3.56, 5.22, 7.64, 9.54, 14.56, 19.52)] + [("pop", t) for t in (7.9, 8.15, 8.4, 11.3, 15.3, 18.32, 22.04)] + [("impact", t) for t in (2.54, 3.56, 5.4, 20.22, 21.04)]
e, h, b, s = cta(23.58, 25.1, 25.46, 26.3, 29.26, DUR); EL += e; HEAD += h; BG += b; SFX += s
