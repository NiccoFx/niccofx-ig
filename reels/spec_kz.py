from cta import cta, cs, Y
DUR = 27.9
B1, B2 = Y(98), Y(36)
EL = [dict(k="nums", x0=290, dx=250, y=960, a=0.3, b=2.68, col="gold"),
      dict(k="band", x1=110, x2=370, y1=B1, y2=B2, col="blue", fill=0.12, a=2.9, b=19.94),
      dict(k="band", x1=395, x2=655, y1=B1, y2=B2, col="gold", fill=0.12, a=3.1, b=19.94),
      dict(k="band", x1=680, x2=940, y1=B1, y2=B2, col="green", fill=0.12, a=3.3, b=19.94),
      dict(k="label", text="ASIA", x=240, y=B1+30, size=30, col="blue", a=2.95, b=19.94),
      dict(k="label", text="LONDON", x=525, y=B1+30, size=30, col="gold", a=3.15, b=19.94),
      dict(k="label", text="NEW YORK", x=810, y=B1+30, size=30, col="green", a=3.35, b=19.94),
      dict(k="label", text="8PM–12AM", x=240, y=B2+30, size=22, col="gray", a=4.6, b=19.94),
      dict(k="label", text="2–5AM", x=525, y=B2+30, size=22, col="gray", a=8.9, b=19.94),
      dict(k="label", text="7–10AM", x=810, y=B2+30, size=22, col="gray", a=13.6, b=19.94),
      dict(k="label", text="New York time", x=540, y=B2+70, size=22, col="gray", a=4.6, b=19.94)]
asia = [(50,54,48,52),(52,55,49,50),(50,53,48,52),(52,55,50,51),(51,54,49,52)]
for j, c in enumerate(asia): EL.append(dict(k="candle", ohlc=c, x=140+j*50, w=30, a=4.6+j*0.12, b=19.94))
EL += [dict(k="box", x1=120, x2=650, p1=48, p2=55, col="blue", fill=0.14, a=7.3, b=19.94), dict(k="pill", text="RANGE", col="blue", x=240, y=Y(62), a=7.4, b=8.72)]
lon = [(52,53,42,44),(44,58,43,57),(57,66,55,65),(65,70,63,69),(69,72,66,70)]
for j, c in enumerate(lon): EL.append(dict(k="candle", ohlc=c, x=420+j*50, w=30, a=(10.5 if j == 0 else 11.5+j*0.15), b=19.94, g=0.3))
EL += [dict(k="pill", text="SWEPT", col="red", x=430, y=Y(34), a=10.8, b=13.46), dict(k="arrow", x1=470, y1=Y(52), x2=640, y2=Y(76), col="green", a=11.8, b=13.46),
       dict(k="pill", text="REAL MOVE", col="green", x=560, y=Y(84), a=12.0, b=13.46)]
ny = [(70,74,64,66),(66,84,65,82),(82,90,80,88),(88,92,84,86),(86,94,85,92)]
for j, c in enumerate(ny): EL.append(dict(k="candle", ohlc=c, x=705+j*50, w=30, a=14.0+j*0.18, b=19.94, g=0.3))
EL += [dict(k="pill", text="BIGGEST VOLUME", col="green", x=810, y=Y(30), a=15.4, b=17.22),
       dict(k="pill", text="OUTSIDE THESE WINDOWS: NO TRADE", col="red", x=540, y=Y(16), a=17.6, b=19.94)]
HEAD = [(0, "GOLD MOVES THE MOST IN", "3 WINDOWS", "gold"), (2.68, "THESE ARE THE", "KILLZONES", "orange"),
        (4.44, "KILLZONE 1", "ASIA: BUILDS THE RANGE", "blue"), (8.72, "KILLZONE 2", "LONDON: THE SWEEP", "gold"),
        (13.46, "KILLZONE 3", "NEW YORK: BIG VOLUME", "green"), (17.22, "OUTSIDE THESE WINDOWS", "I USUALLY DON'T TRADE", "red")]
BG = [(0, "orange"), (4.44, "blue"), (8.72, "orange"), (13.46, "green"), (17.22, "red")]
ZOOM = [(4.6, 1.55, 250, Y(60)), (8.8, 1.55, 525, Y(62)), (13.5, 1.55, 810, Y(70)), (17.22, 1.0, 540, 960), (19.94, 1.0, 540, 960)]
SFX = [("whoosh", t) for t in (2.68, 4.44, 8.72, 13.46, 17.22)] + [("pop", t) for t in (0.3, 0.55, 0.8, 2.95, 3.15, 3.35, 7.4, 10.8, 12.0, 15.4, 17.6)] + [("impact", t) for t in (10.5, 14.2)]
e, h, b, s = cta(19.94, 21.34, 21.68, 23.06, 25.4, DUR); EL += e; HEAD += h; BG += b; SFX += s
