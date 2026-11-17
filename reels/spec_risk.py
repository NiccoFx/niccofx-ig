from cta import cta, cs, Y
DUR = 31.5
EL = cs([(50,58,48,56),(56,64,54,62),(62,68,60,66),(66,67,20,22)], 330, 140, 0.0, 2.58, stag=0.08, extra={3:(0.8,0.5)})
EL += [dict(k="pill", text="ACCOUNT BLOWN", col="red", size=44, x=540, y=Y(14), a=1.4, b=2.58),
       dict(k="big", text="1%", col="gold", size=360, x=540, y=960, a=3.42, b=4.9),
       dict(k="big", text="$10,000", col="white", size=200, x=540, y=960, a=6.82, b=8.34),
       dict(k="label", text="your account", x=540, y=1110, size=36, col="gray", a=7.0, b=8.34),
       dict(k="big", text="$100", col="green", size=260, x=540, y=960, a=10.46, b=12.52),
       dict(k="label", text="1% of $10,000 = max risk per trade", x=540, y=1130, size=34, col="gray", a=10.6, b=12.52),
       dict(k="big", text="$100 ÷ $10 STOP", col="white", size=100, x=540, y=760, a=15.06, b=19.74),
       dict(k="big", text="= 10 OZ", col="gold", size=130, x=540, y=960, a=16.6, b=19.74),
       dict(k="big", text="= 0.1 LOTS", col="green", size=150, x=540, y=1180, a=18.02, b=19.74),
       dict(k="chips", items=["L","L","L","L","L"], x0=160, dx=190, y=800, a=19.8, st=0.12, b=22.86),
       dict(k="big", text="≈ -10%", col="green", size=220, x=540, y=1120, a=21.0, b=22.86),
       dict(k="label", text="$10,000 → $9,044 after 10 losses at 1%", x=540, y=1290, size=32, col="gray", a=21.3, b=22.86)]
HEAD = [(0, "DON'T LET", "ONE BAD TRADE END IT", "red"), (2.58, "THAT'S WHY I USE", "THE 1% RULE", "gold"),
        (4.9, "STEP 1", "TAKE YOUR ACCOUNT", "white"), (8.34, "STEP 2", "RISK 1%", "green"), (12.52, "STEP 3", "DIVIDE BY YOUR STOP", "orange"),
        (19.74, "10 LOSSES IN A ROW?", "STILL ONLY ~10% DOWN", "green")]
BG = [(0, "red"), (2.58, "orange"), (4.9, "green"), (12.52, "orange"), (19.74, "green")]
SFX = [("whoosh", t) for t in (2.58, 4.9, 8.34, 12.52, 19.74)] + [("pop", t) for t in (1.4, 7.0, 15.06, 16.6, 19.8, 19.92, 20.04, 20.16, 20.28)] + \
      [("impact", t) for t in (0.8, 3.42, 6.82, 10.46, 18.02, 21.0)]
e, h, b, s = cta(22.86, 24.66, 25.12, 26.48, 29.08, DUR); EL += e; HEAD += h; BG += b; SFX += s
