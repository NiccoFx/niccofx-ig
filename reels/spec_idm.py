from cta import cta, cs, Y
DUR = 28.0
C = [(20,24,18,22),(22,40,21,38),(38,50,37,48),(48,49,42,44),(44,56,43,54),(54,58,50,52),(52,53,36,38),(38,39,22,25),(25,45,24,43),(43,62,42,60)]
EL = cs(C, 140, 92, 0.1, 19.94, stag=0.08, extra={3:(3.9,0.3),4:(6.0,0.3),5:(10.2,0.25),6:(10.5,0.35),7:(12.5,0.35),8:(14.5,0.35),9:(15.0,0.3)})
EL += [dict(k="pill", text="SMALL PULLBACK", col="orange", x=416, y=Y(32), a=4.6, b=8.1),
       dict(k="pill", text="TRADERS BUY", col="green", x=508, y=Y(64), a=6.6, b=10.2),
       dict(k="hline", p=41, x1=380, x2=1000, col="red", a=8.2, b=12.4),
       dict(k="dots", col="red", pts=[(450,39),(520,38.5),(590,39.5),(660,38),(730,39),(800,38.5)], a=8.4, b=11.4),
       dict(k="label", text="THEIR STOPS", x=900, y=Y(41)+30, size=24, col="red", a=8.5, b=11.4),
       dict(k="ring", x=692, y=Y(37), r=36, col="red", a=11.34, b=13.5),
       dict(k="pill", text="INDUCEMENT SWEPT", col="red", x=600, y=Y(30), a=11.5, b=13.5),
       dict(k="box", x1=100, x2=1000, p1=18, p2=26, col="green", fill=0.18, a=12.5, b=19.94),
       dict(k="label", text="REAL ZONE", x=900, y=Y(22), size=26, col="green", a=12.6, b=19.94),
       dict(k="arrow", x1=1000, y1=Y(44), x2=1000, y2=Y(76), col="green", a=15.0, b=19.94),
       dict(k="ring", x=416, y=Y(43), r=34, col="red", a=16.5, b=19.94),
       dict(k="pill", text="NOT THIS ONE", col="red", x=416, y=Y(56), a=16.6, b=19.94)]
HEAD = [(0, "XAU/USD", "THE FIRST PULLBACK", "orange"), (1.72, "IS USUALLY", "A TRAP", "red"), (2.56, "IT'S CALLED", "INDUCEMENT", "orange"),
        (5.98, "TRADERS THINK", "IT'S THE ENTRY", "green"), (8.2, "THEIR STOPS", "SIT RIGHT BELOW", "red"), (10.3, "PRICE DROPS", "TAKES THOSE STOPS", "red"),
        (12.5, "THEN TAPS", "THE REAL ZONE", "green"), (14.46, "THAT'S WHERE", "THE REAL MOVE STARTS", "green"),
        (16.42, "DON'T TAKE", "THE FIRST PULLBACK", "red"), (17.92, "WAIT FOR INDUCEMENT", "TO BE SWEPT", "green")]
BG = [(0, "orange"), (1.72, "red"), (2.56, "orange"), (5.98, "green"), (8.2, "red"), (12.5, "green"), (16.42, "red"), (17.92, "green")]
SFX = [("whoosh", t) for t in (1.72, 2.56, 5.98, 8.2, 10.3, 12.5, 16.42, 17.92)] + [("pop", t) for t in (4.6, 6.6, 8.5, 11.5, 12.6, 16.6)] + [("impact", t) for t in (1.72, 11.34, 14.5)]
e, h, b, s = cta(19.94, 21.36, 21.74, 23.18, 25.6, DUR); EL += e; HEAD += h; BG += b; SFX += s
