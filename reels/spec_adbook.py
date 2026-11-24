DUR = 21.2
MUSIC = "/home/user/repo/w/pat/music.mp3"
MUSIC_VOL = 0.24
COVER = "/home/user/repo/w/ads/cover.png"
EL, SFX = [], []
for txt, x, y, rot, a in [("RANDOM YOUTUBE VIDEO", 330, 760, 6, 0.1), ("TIKTOK TIP #47", 720, 900, -7, 0.35), ("FREE PDF FROM A STRANGER", 400, 1060, -4, 0.6), ("ANOTHER INDICATOR", 700, 1220, 5, 0.85)]:
    EL.append(dict(k="pill", text=txt, col="gray", size=40, rot=rot, x=x, y=y, a=a, b=2.84)); SFX.append(("pop", a))
EL += [dict(k="big", text="✕", col="red", size=420, x=540, y=1000, a=1.68, b=2.84)]
EL += [dict(k="img", src=COVER, w=560, x=540, y=1000, a=2.9, b=DUR)]
for i, (txt, a) in enumerate([("250 CHAPTERS", 5.92), ("15 PARTS", 7.5), ("320 PAGES", 8.72)]):
    EL.append(dict(k="pill", text=txt, col="gold", fg=(20, 20, 22), size=46, x=540, y=1420 + i * 90, a=a, b=10.42)); SFX.append(("pop", a))
for txt, x, y, rot, a in [("MARKET STRUCTURE", 250, 760, -6, 10.42), ("LIQUIDITY", 830, 860, 6, 11.4), ("ORDER BLOCKS", 240, 1180, 5, 12.2), ("FAIR VALUE GAPS", 820, 1260, -5, 13.2), ("RISK", 540, 1450, 0, 14.1)]:
    EL.append(dict(k="pill", text=txt, col="green", size=40, rot=rot, x=x, y=y, a=a, b=16.08)); SFX.append(("pop", a))
EL += [dict(k="pill", text="USE CODE FVG AT CHECKOUT", col="gold", fg=(20, 20, 22), size=42, x=540, y=1450, a=16.6, b=18.96),
       dict(k="pill", text="GET THE BOOK →", col="green", size=60, x=540, y=1450, a=18.96, b=DUR),
       dict(k="label", text="niccofx.gumroad.com/l/blueprint", x=540, y=1545, size=32, col="gray", a=19.1, b=DUR)]
SFX += [("impact", 1.68), ("whoosh", 2.84), ("impact", 2.95), ("whoosh", 10.42), ("whoosh", 16.08), ("pop", 16.6), ("whoosh", 18.96), ("ding", 19.1)]
HEAD = [(0, "STOP LEARNING FROM", "RANDOM VIDEOS", "red"), (2.84, "EVERYTHING I KNOW ABOUT GOLD", "IN ONE BOOK", "gold"),
        (10.42, "STEP BY STEP", "EVERY CORE CONCEPT", "green"), (16.08, "THE ULTIMATE COMPLETE", "TRADING A TO Z", "gold"), (18.96, "TAP BELOW", "GET YOUR COPY", "green")]
BG = [(0, "red"), (2.84, "orange"), (10.42, "green"), (16.08, "orange"), (18.96, "green")]
ZOOM = []
