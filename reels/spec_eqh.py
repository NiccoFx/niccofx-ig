from cta import cta, cs, Y
DUR = 26.4
C = [(40,52,38,50),(50,70,48,62),(62,64,52,55),(55,70,54,66),(66,67,56,58),(58,70,57,64),(64,65,55,57),(57,66,56,64),(64,80,58,60),(60,61,38,40)]
EL = cs(C, 150, 90, 0.0, 18.06, stag=0.07, extra={7:(10.8,0.25),8:(11.8,0.35),9:(12.78,0.4)})
EL += [dict(k="hline", p=70, x1=180, x2=1000, col="gold", a=0.4, b=18.06),
       dict(k="label", text="EQUAL HIGHS", x=900, y=Y(70)+28, size=24, col="gold", a=0.5, b=18.06),
       dict(k="pill", text="NOT RESISTANCE", col="red", x=540, y=Y(90), a=1.7, b=3.0),
       dict(k="pill", text="MAGNET", col="gold", fg=(20,20,22), size=46, x=540, y=Y(90), a=3.1, b=4.3),
       dict(k="dots", col="red", pts=[(220,73),(300,75),(360,72),(430,76),(500,73),(560,75),(630,72),(700,76),(760,73)], a=5.2, b=12.1),
       dict(k="label", text="STOPS", x=470, y=Y(80), size=26, col="red", a=5.3, b=6.8),
       dict(k="box", x1=180, x2=1000, p1=70, p2=78, col="gold", fill=0.14, a=6.9, b=12.1),
       dict(k="pill", text="LIQUIDITY POOL", col="gold", fg=(20,20,22), x=540, y=Y(86), a=7.2, b=12.1),
       dict(k="ring", x=870, y=Y(80), r=36, col="red", a=12.0, b=18.06),
       dict(k="pill", text="STOPS TAKEN", col="red", x=760, y=Y(88), a=12.2, b=18.06),
       dict(k="arrow", x1=1010, y1=Y(62), x2=1010, y2=Y(34), col="red", a=13.0, b=18.06),
       dict(k="pill", text="DON'T SELL HERE", col="red", x=420, y=Y(44), a=15.6, b=18.06),
       dict(k="pill", text="SELL AFTER THE SWEEP", col="green", x=760, y=Y(28), a=17.0, b=18.06)]
HEAD = [(0, "XAU/USD", "SEE THESE EQUAL HIGHS?", "orange"), (1.64, "THAT'S NOT", "RESISTANCE", "red"), (3.0, "IT'S A", "MAGNET", "orange"),
        (4.3, "EVERY TRADER'S STOP", "SITS ABOVE THEM", "red"), (6.68, "THAT'S A POOL OF", "LIQUIDITY", "orange"), (8.44, "SMART MONEY NEEDS IT", "TO SELL", "red"),
        (10.7, "PRICE RUNS UP", "TAKES THE STOPS", "red"), (12.78, "AND", "REVERSES", "red"), (13.96, "NEXT TIME", "DON'T SELL UNDER THEM", "red"),
        (16.88, "WAIT FOR", "THE SWEEP", "green")]
BG = [(0, "orange"), (1.64, "red"), (3.0, "orange"), (4.3, "red"), (6.68, "orange"), (8.44, "red"), (16.88, "green")]
SFX = [("whoosh", t) for t in (1.64, 3.0, 4.3, 6.68, 10.7, 13.96, 16.88)] + [("pop", t) for t in (0.5, 1.7, 3.1, 5.3, 7.2, 12.2, 15.6, 17.0)] + [("impact", t) for t in (11.9, 12.78)]
e, h, b, s = cta(18.06, 19.82, 19.96, 21.52, 23.92, DUR); EL += e; HEAD += h; BG += b; SFX += s
