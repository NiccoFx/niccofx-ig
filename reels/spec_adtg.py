from cta import cs, Y
DUR = 16.4
FOOT = "Education only · Not financial advice"
EL, SFX = [], []
chaos = [(50,58,44,46),(46,60,42,58),(58,62,40,42),(42,57,41,55),(55,56,38,40),(40,61,39,60),(60,64,45,47),(47,52,36,38)]
EL += cs(chaos, 220, 92, 0.0, 2.3, stag=0.07)
EL += [dict(k="big", text="?", col="red", size=320, x=880, y=Y(52), a=0.6, b=2.3)]
EL += [dict(k="ui", ui="card", x=540, y=960, a=2.35, b=4.92, border="blue",
            lines=[["NICCOFX", 40, "gray"], ["GOLD COMMUNITY", 96, "white"], ["on Telegram", 44, "blue"]]),
       dict(k="pill", text="FREE", col="green", size=60, rot=-8, x=820, y=760, a=3.16, b=4.92)]
for i, (txt, col, a) in enumerate([("FREE GOLD MARKET ANALYSIS", "blue", 4.92), ("2–3 EDUCATIONAL SETUPS A WEEK", "gold", 6.94), ("LIQUIDITY & SMART MONEY LESSONS", "green", 9.82)]):
    EL.append(dict(k="pill", text=txt, col=col, size=44, fg=(20, 20, 22) if col == "gold" else (255, 255, 255), x=540, y=860 + i * 170, a=a, b=12.54))
    SFX.append(("pop", a))
EL += [dict(k="big", text="$0", col="gold", size=360, x=540, y=1000, a=12.54, b=13.78),
       dict(k="pill", text="JOIN FREE ON TELEGRAM →", col="blue", size=58, x=540, y=1000, a=13.78, b=DUR),
       dict(k="label", text="niccofx.com/community", x=540, y=1110, size=34, col="gray", a=14.0, b=DUR)]
SFX += [("impact", 0.6), ("whoosh", 2.3), ("pop", 3.16), ("whoosh", 4.92), ("impact", 12.54), ("whoosh", 13.78), ("ding", 14.0)]
HEAD = [(0, "XAU/USD", "TRADING GOLD ALONE IS HARD", "red"), (2.3, "SO I BUILT A", "FREE TELEGRAM COMMUNITY", "blue"),
        (4.92, "WHAT YOU GET", "ALL OF IT FREE", "green"), (12.54, "IT COSTS", "NOTHING", "gold"), (13.78, "TAP BELOW", "JOIN US ON TELEGRAM", "blue")]
BG = [(0, "red"), (2.3, "blue"), (4.92, "green"), (12.54, "orange"), (13.78, "blue")]
ZOOM = []
