from cta import cs, Y
DUR = 50.2
EL, SFX = [], []
FOOT = "Education only · Not financial advice"

def quiz(q, c0, ans, A, B, good, end, qx=880, qy=Y(60)):
    """q: question time, c0: countdown start, ans: answer time; A/B labels; good=0/1"""
    out = [dict(k="pill", text=A, col="green", size=52, x=300, y=1460, a=q, b=ans if good else end),
           dict(k="pill", text=B, col="red", size=52, x=780, y=1460, a=q + 0.15, b=end if good else ans),
           dict(k="big", text="?", col="white", size=260, x=qx, y=qy, a=q, b=c0),
           dict(k="bar", x=140, y=1550, w=800, h=22, frac=1.0, col="gold", countdown=True, dur=1.8, a=c0, b=c0 + 1.8)]
    for i, n in enumerate("321"):
        out.append(dict(k="big", text=n, col="gold", size=300, x=qx, y=qy, a=c0 + i * 0.6, b=c0 + i * 0.6 + 0.6))
    gx = 780 if good else 300
    out += [dict(k="pill", text=(B if good else A), col=("red" if good else "green"), size=52, s=1.25, x=gx, y=1460, a=ans, b=end),
            dict(k="ring", x=gx, y=1460, r=150, col="gold", a=ans, b=ans + 1.2)]
    s = [("whoosh", q), ("pop", q), ("pop", q + 0.15)] + [("pop", c0 + i * 0.6) for i in range(3)] + [("impact", ans), ("ding", ans + 0.05)]
    return out, s

# ---------- hook ----------
EL += [dict(k="nums", x0=290, dx=250, y=980, a=0.3, b=6.36, col="gold"),
       dict(k="big", text="?", col="white", size=220, x=290, y=1240, a=1.5, b=6.36),
       dict(k="big", text="?", col="white", size=220, x=540, y=1240, a=1.65, b=6.36),
       dict(k="big", text="?", col="white", size=220, x=790, y=1240, a=1.8, b=6.36)]
SFX += [("pop", 0.3), ("pop", 0.55), ("pop", 0.8), ("whoosh", 2.9)]

# ---------- round 1: sweep of the low ----------
R1 = [(72,74,64,66),(66,68,58,60),(60,62,46,48),(48,56,47,54),(54,57,50,52),(52,53,40,49)]
EL += cs(R1, 150, 80, 6.4, 16.84, stag=0.1, extra={5: (7.6, 0.6)})
EL += cs([(49,60,48,58),(58,70,57,68),(68,78,66,76)], 630, 80, 13.0, 16.84, stag=0.25)
EL += [dict(k="hline", p=46, x1=280, x2=1000, col="gray", a=7.3, b=16.84), dict(k="label", text="OLD LOW", x=930, y=Y(46)+26, size=24, col="gray", a=7.4, b=16.84),
       dict(k="ring", x=550, y=Y(41), r=34, col="red", a=8.0, b=16.84),
       dict(k="pill", text="STOPS TAKEN", col="red", x=500, y=Y(32), a=13.56, b=16.84),
       dict(k="arrow", x1=640, y1=Y(52), x2=830, y2=Y(80), col="green", a=15.5, b=16.84)]
e, s = quiz(9.92, 10.91, 12.98, "▲ UP", "▼ DOWN", 0, 16.84); EL += e; SFX += s + [("impact", 7.6), ("pop", 13.56)]

# ---------- round 2: the gap ----------
R2 = [(40,44,38,42),(42,46,40,43),(43,78,42,76),(76,82,74,80),(80,81,66,68),(68,69,58,60)]
EL += cs(R2, 150, 80, 16.9, 27.98, stag=0.1, extra={2: (17.64, 0.5), 3: (18.2, 0.3), 4: (19.76, 0.3), 5: (20.2, 0.3)})
EL += cs([(60,72,58,70),(70,88,69,86),(86,96,84,94)], 630, 80, 24.1, 27.98, stag=0.25)
EL += [dict(k="box", x1=230, x2=1000, p1=46, p2=74, col="gold", fill=0.16, a=19.0, b=27.98),
       dict(k="label", text="GAP", x=960, y=Y(60), size=30, col="gold", a=19.1, b=27.98),
       dict(k="pill", text="FAIR VALUE GAP", col="gold", fg=(20, 20, 22), x=420, y=Y(30), a=24.58, b=27.98),
       dict(k="arrow", x1=640, y1=Y(64), x2=830, y2=Y(98), col="green", a=26.14, b=27.98)]
e, s = quiz(20.98, 21.97, 24.06, "BUY", "SELL", 0, 27.98); EL += e; SFX += s + [("impact", 17.64), ("pop", 24.58)]

# ---------- round 3: the trap ----------
R3 = [(40,48,38,46),(46,58,44,56),(56,70,54,60),(60,64,52,54),(54,62,52,60),(60,76,59,64)]
EL += cs(R3, 150, 80, 28.0, 38.64, stag=0.1, extra={5: (30.6, 0.6)})
EL += cs([(64,65,50,52),(52,53,40,42),(42,44,30,32)], 630, 80, 37.62, 38.64, stag=0.2)
EL += [dict(k="hline", p=70, x1=280, x2=1000, col="gray", a=28.4, b=38.64), dict(k="label", text="OLD HIGH", x=930, y=Y(70)-26, size=24, col="gray", a=28.5, b=38.64),
       dict(k="ring", x=550, y=Y(74), r=34, col="gold", a=31.9, b=38.64),
       dict(k="pill", text="ONLY A WICK", col="gold", fg=(20, 20, 22), x=470, y=Y(84), a=31.9, b=36.12),
       dict(k="pill", text="WICK ABOVE = SWEEP", col="red", x=470, y=Y(84), a=36.12, b=38.64)]
e, s = quiz(32.54, 33.39, 35.54, "YES, BUY", "NO", 1, 38.64, qy=Y(48)); EL += e; SFX += s + [("impact", 30.6), ("impact", 37.62), ("pop", 31.9), ("pop", 36.12)]

# ---------- score + book + CTA ----------
EL += [dict(k="ui", ui="card", x=540, y=930, a=38.7, b=41.14, border="gold",
            lines=[["YOUR SCORE", 40, "gray"], ["3 / 3 ?", 170, "gold"], ["SAVE IT · SEND IT TO A FRIEND", 38, "white"]]),
       dict(k="pill", text="SAVE", col="gold", fg=(20, 20, 22), size=48, x=330, y=1290, a=39.5, b=41.14),
       dict(k="pill", text="SEND", col="blue", size=48, x=750, y=1290, a=40.14, b=41.14),
       dict(k="ui", ui="card", x=540, y=930, a=41.2, b=45.3, border="gold",
            lines=[["THE ULTIMATE COMPLETE", 48, "white"], ["TRADING A TO Z", 110, "gold"], ["320 pages · 15 parts · 250 chapters", 34, "gray"]]),
       dict(k="pill", text="ALL 3 SETUPS INSIDE", col="green", size=44, x=540, y=1260, a=42.1, b=45.3),
       dict(k="ui", ui="profile", x=540, y=1010, a=45.3, b=DUR),
       dict(k="ui", ui="comment", x=540, y=1170, a=45.4, b=DUR, type="TRADING")]
SFX += [("pop", 39.5), ("pop", 40.14), ("whoosh", 41.14), ("impact", 41.3), ("pop", 42.1), ("whoosh", 45.3), ("pop", 45.7), ("ding", 47.4)]

HEAD = [(0, "GOLD CHART TEST", "GUESS THE NEXT MOVE", "gold"), (2.9, "GET ALL 3 RIGHT", "YOU GET SMART MONEY", "orange"),
        (6.36, "ROUND 1 / 3", "PRICE SWEEPS THE LOW", "blue"), (9.92, "ROUND 1 / 3", "UP OR DOWN?", "white"),
        (12.98, "ANSWER", "UP. BUYERS TAKE OVER", "green"),
        (16.84, "ROUND 2 / 3", "PRICE LEAVES A GAP", "blue"), (20.98, "ROUND 2 / 3", "BUY OR SELL?", "white"),
        (24.06, "ANSWER", "BUY. THE GAP GETS FILLED", "green"),
        (27.98, "ROUND 3 / 3", "THIS ONE IS A TRAP", "red"), (32.54, "ROUND 3 / 3", "BUY THE BREAKOUT?", "white"),
        (35.54, "ANSWER", "NO. IT'S A SWEEP", "red"),
        (38.64, "3 OUT OF 3?", "SAVE THIS & TEST A FRIEND", "gold"),
        (41.14, "EVERY SETUP HERE IS", "A CHAPTER IN MY BOOK", "orange"),
        (45.3, "WANT THE LINK? COMMENT", '"TRADING"', "orange"), (47.36, "FOLLOW FOR", "TOMORROW'S TEST", "green")]
BG = [(0, "orange"), (6.36, "blue"), (9.92, "orange"), (12.98, "green"), (16.84, "blue"), (20.98, "orange"), (24.06, "green"),
      (27.98, "red"), (32.54, "orange"), (35.54, "red"), (38.64, "orange"), (47.36, "green")]
ZOOM = []
