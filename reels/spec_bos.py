from cta import cta, cs, Y
DUR = 31.3
EL = [dict(k="pill", text="BOS", col="green", size=90, x=320, y=960, a=0.2, b=4.22),
      dict(k="pill", text="CHOCH", col="red", size=90, x=760, y=960, a=0.98, b=4.22),
      dict(k="label", text="vs", x=540, y=960, size=44, col="gray", a=0.6, b=4.22),
      dict(k="big", text="30 SEC", col="gold", size=220, x=540, y=960, a=4.4, b=6.54)]
C = [(20,26,18,25),(25,36,24,35),(35,36,28,30),(30,44,29,43),(43,48,42,46),(46,47,36,38),(38,58,37,56),(56,62,54,60),(60,61,40,42),(42,44,30,32)]
EL += cs(C, 150, 88, 6.6, 19.28, extra={3:(7.84,0.25),4:(8.0,0.25),5:(8.6,0.25),6:(9.4,0.3),7:(9.7,0.25),8:(13.6,0.3),9:(14.3,0.3)})
EL += [dict(k="hline", p=36, x1=230, x2=520, col="green", a=9.3, b=19.28),
       dict(k="pill", text="BOS", col="green", x=420, y=Y(42), a=10.84, b=19.28),
       dict(k="hline", p=48, x1=500, x2=700, col="green", a=12.1, b=19.28),
       dict(k="pill", text="BOS", col="green", x=620, y=Y(54), a=12.2, b=19.28),
       dict(k="hline", p=36, x1=590, x2=1000, col="red", a=13.9, b=19.28),
       dict(k="label", text="LAST HIGHER LOW", x=720, y=Y(36)+30, size=24, col="red", a=14.0, b=19.28),
       dict(k="pill", text="CHOCH", col="red", size=44, x=880, y=Y(22), a=16.14, b=19.28),
       dict(k="arrow", x1=990, y1=Y(40), x2=990, y2=Y(12), col="red", a=17.5, b=19.28),
       dict(k="ui", ui="card", x=540, y=820, a=19.3, b=23.36, border="green", lines=[["BOS", 110, "green"], ["= TREND CONTINUES", 40, "white"]]),
       dict(k="ui", ui="card", x=540, y=1180, a=21.32, b=23.36, border="red", lines=[["CHOCH", 110, "red"], ["= WARNING, MAY TURN", 40, "white"]])]
HEAD = [(0, "XAU/USD", "BOS OR CHOCH?", "orange"), (2.68, "MOST TRADERS", "MIX THEM UP", "red"), (4.22, "THE DIFFERENCE IN", "30 SECONDS", "orange"),
        (6.54, "IN AN UPTREND", "HIGHER HIGHS", "green"), (9.22, "BREAKS THE LAST HIGH", "BREAK OF STRUCTURE", "green"), (12.12, "BOS =", "TREND CONTINUES", "green"),
        (13.56, "BREAKS THE LAST HIGHER LOW", "CHANGE OF CHARACTER", "red"), (17.5, "CHOCH =", "TREND MAY BE TURNING", "red"),
        (19.28, "REMEMBER", "BOS VS CHOCH", "orange")]
BG = [(0, "orange"), (2.68, "red"), (4.22, "orange"), (6.54, "green"), (13.56, "red"), (19.28, "orange")]
SFX = [("whoosh", t) for t in (2.68, 4.22, 6.54, 13.56, 19.28)] + [("pop", t) for t in (0.2, 0.98, 10.84, 12.2, 16.14, 19.3, 21.32)] + [("impact", t) for t in (4.4, 14.3, 16.14)]
e, h, b, s = cta(23.36, 24.62, 25.08, 26.36, 28.86, DUR); EL += e; HEAD += h; BG += b; SFX += s
