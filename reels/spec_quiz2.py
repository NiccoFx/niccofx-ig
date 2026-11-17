from cta import cs, Y
DUR = 52.4
MUSIC = "/home/user/repo/w/quiz2/music_a.mp3"
MUSIC_VOL = 0.32
EL, SFX = [], []

def quiz(q, c0, ans, A, B, good, end, qx=880, qy=Y(60)):
    out = [dict(k="pill", text=A, col="green", size=52, x=300, y=1460, a=q, b=ans if good else end),
           dict(k="pill", text=B, col="red", size=52, x=780, y=1460, a=q + 0.15, b=end if good else ans),
           dict(k="big", text="?", col="white", size=260, x=qx, y=qy, a=q, b=c0),
           dict(k="bar", x=140, y=1550, w=800, h=22, frac=1.0, col="gold", countdown=True, dur=1.8, a=c0, b=c0 + 1.8)]
    for i, n in enumerate("321"):
        out.append(dict(k="big", text=n, col="gold", size=300, x=qx, y=qy, a=c0 + i * 0.6, b=c0 + i * 0.6 + 0.6))
    gx = 780 if good else 300
    out += [dict(k="pill", text=(B if good else A), col=("red" if good else "green"), size=52, s=1.25, x=gx, y=1460, a=ans, b=end),
            dict(k="ring", x=gx, y=1460, r=150, col="gold", a=ans, b=ans + 1.2)]
    s = [("whoosh", q), ("pop", q), ("pop", q + 0.15), ("tick", c0), ("impact", ans), ("ding", ans + 0.05)]
    return out, s

# hook: TEST #2 badge + 3 cards
EL += [dict(k="big", text="TEST #2", col="gold", size=200, x=540, y=900, a=0.1, b=3.42),
       dict(k="nums", x0=290, dx=250, y=1180, a=2.06, b=5.98, col="gold"),
       dict(k="pill", text="ROUND 3 = THE TRAP", col="red", size=46, x=540, y=1380, a=3.6, b=5.98)]
SFX += [("impact", 0.1), ("pop", 2.06), ("pop", 2.31), ("pop", 2.56), ("pop", 3.6), ("whoosh", 3.42)]

# R1 equal highs
R1 = [(40,50,38,48),(48,70,46,66),(66,67,54,56),(56,70,55,64),(64,66,56,58),(58,66,57,65)]
EL += cs(R1, 150, 80, 6.0, 17.76, stag=0.12)
EL += cs([(65,78,64,66),(66,67,52,54),(54,55,40,42)], 630, 80, 12.6, 17.76, stag=0.3, extra={0: (12.6, 0.5)})
EL += [dict(k="hline", p=70, x1=200, x2=1000, col="gold", a=7.0, b=17.76), dict(k="label", text="EQUAL HIGHS", x=600, y=Y(70)-30, size=24, col="gold", a=7.1, b=17.76),
       dict(k="dots", pts=[(230, 70), (390, 70)], col="gold", a=7.2, b=17.76),
       dict(k="pill", text="STOPS SIT HERE", col="gold", fg=(20, 20, 22), x=330, y=Y(82), a=13.86, b=17.76),
       dict(k="ring", x=630, y=Y(76), r=34, col="red", a=13.0, b=17.76),
       dict(k="arrow", x1=720, y1=Y(60), x2=820, y2=Y(36), col="red", a=15.7, b=17.76)]
e, s = quiz(9.3, 10.53, 12.58, "BREAKOUT", "SWEEP", 1, 17.76); EL += e; SFX += s + [("pop", 7.2), ("pop", 13.86)]

# R2 order block in discount
R2 = [(36,38,30,32),(32,50,31,48),(48,72,47,70),(70,71,58,60),(60,61,46,48),(48,49,38,40)]
EL += cs(R2, 150, 80, 17.8, 29.82, stag=0.1, extra={3: (19.5, 0.3), 4: (19.8, 0.3), 5: (20.1, 0.3)})
EL += cs([(40,56,39,54),(54,70,53,68),(68,84,67,82)], 630, 80, 25.4, 29.82, stag=0.25)
EL += [dict(k="box", x1=110, x2=1000, p1=30, p2=38, col="blue", fill=0.22, a=21.0, b=29.82),
       dict(k="label", text="ORDER BLOCK", x=900, y=Y(34), size=26, col="blue", a=21.1, b=29.82),
       dict(k="hline", p=51, x1=110, x2=1000, col="gold", dash=False, a=20.1, b=29.82), dict(k="label", text="50%", x=975, y=Y(51)-24, size=26, col="gold", a=20.2, b=29.82),
       dict(k="label", text="DISCOUNT", x=930, y=Y(44), size=26, col="green", a=20.3, b=29.82),
       dict(k="pill", text="DISCOUNT + OB + UPTREND", col="green", size=40, x=470, y=Y(18), a=25.98, b=29.82),
       dict(k="arrow", x1=640, y1=Y(46), x2=830, y2=Y(88), col="green", a=28.9, b=29.82)]
e, s = quiz(22.26, 23.29, 25.34, "BUY", "WAIT", 0, 29.82); EL += e; SFX += s + [("pop", 21.0), ("pop", 25.98)]

# R3 change of character
R3 = [(40,50,38,48),(48,60,46,56),(56,58,48,50),(50,66,49,64),(64,70,62,68),(68,69,40,42)]
EL += cs(R3, 150, 80, 29.9, 41.8, stag=0.1, extra={5: (31.36, 0.6)})
EL += cs([(42,50,41,48),(48,49,32,34),(34,36,22,24)], 630, 80, 39.4, 41.8, stag=0.25)
EL += [dict(k="hline", p=48, x1=300, x2=1000, col="gray", a=30.5, b=41.8), dict(k="label", text="LAST HIGHER LOW", x=880, y=Y(48)-26, size=24, col="gray", a=30.6, b=41.8),
       dict(k="ring", x=550, y=Y(44), r=36, col="red", a=31.9, b=41.8),
       dict(k="pill", text="LOOKS CHEAP...", col="gold", fg=(20, 20, 22), x=560, y=Y(80), a=33.64, b=37.36),
       dict(k="pill", text="CHANGE OF CHARACTER", col="red", x=500, y=Y(80), a=37.86, b=41.8),
       dict(k="arrow", x1=720, y1=Y(52), x2=820, y2=Y(26), col="red", a=39.4, b=41.8)]
e, s = quiz(34.76, 35.31, 37.36, "YES, BUY", "NO", 1, 41.8, qy=Y(66)); EL += e; SFX += s + [("impact", 31.36), ("pop", 33.64), ("pop", 37.86)]

# score + book + CTA
EL += [dict(k="ui", ui="card", x=540, y=930, a=41.85, b=44.06, border="gold",
            lines=[["YOUR SCORE?", 44, "gray"], ["_ / 3", 170, "gold"], ["COMMENT IT BELOW", 40, "white"]]),
       dict(k="ui", ui="card", x=540, y=930, a=44.1, b=47.88, border="gold",
            lines=[["THE ULTIMATE COMPLETE", 48, "white"], ["TRADING A TO Z", 110, "gold"], ["320 pages · 15 parts · 250 chapters", 34, "gray"]]),
       dict(k="pill", text="ALL OF THIS IS INSIDE", col="green", size=44, x=540, y=1260, a=44.9, b=47.88),
       dict(k="ui", ui="profile", x=540, y=1010, a=47.88, b=DUR),
       dict(k="ui", ui="comment", x=540, y=1170, a=47.95, b=DUR, type="TRADING")]
SFX += [("whoosh", 41.8), ("pop", 42.9), ("whoosh", 44.06), ("impact", 44.2), ("pop", 44.9), ("whoosh", 47.88), ("pop", 48.3), ("ding", 49.3)]

HEAD = [(0, "GOLD CHART TEST", "3 NEW CHARTS", "gold"), (3.42, "CAREFUL", "ROUND 3 IS A TRAP", "red"),
        (5.98, "ROUND 1 / 3", "TWO EQUAL HIGHS", "blue"), (9.3, "ROUND 1 / 3", "BREAKOUT OR SWEEP?", "white"),
        (12.58, "ANSWER", "SWEEP. STOPS GRABBED", "red"),
        (17.76, "ROUND 2 / 3", "PULLBACK INTO DISCOUNT", "blue"), (22.26, "ROUND 2 / 3", "BUY OR WAIT?", "white"),
        (25.34, "ANSWER", "BUY. THAT'S THE ZONE", "green"),
        (29.82, "ROUND 3 / 3", "THE TRAP", "red"), (34.76, "ROUND 3 / 3", "BUY THE DIP?", "white"),
        (37.36, "ANSWER", "NO. THE TREND FLIPPED", "red"),
        (41.8, "HOW MANY DID YOU GET?", "COMMENT YOUR SCORE", "gold"),
        (44.06, "ALL OF THIS IS IN", "MY BOOK", "orange"),
        (47.88, "WANT THE LINK? COMMENT", '"TRADING"', "orange"), (49.24, "FOLLOW FOR", "TEST #3", "green")]
BG = [(0, "orange"), (3.42, "red"), (5.98, "blue"), (9.3, "orange"), (12.58, "red"), (17.76, "blue"), (22.26, "orange"), (25.34, "green"),
      (29.82, "red"), (34.76, "orange"), (37.36, "red"), (41.8, "orange"), (49.24, "green")]
ZOOM = []
