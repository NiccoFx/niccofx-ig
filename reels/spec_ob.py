from cta import cta, cs, Y
DUR = 32.5
EL = []
# hook: several "order blocks", most wrong
EL += cs([(70,72,58,60),(60,64,54,56),(56,62,52,60),(60,61,46,48),(48,50,40,42),(42,58,41,56),(56,70,55,68)], 180, 110, 0.0, 3.9)
EL += [dict(k="box", x1=230, x2=290, p1=54, p2=60, col="gold", fill=0.18, a=0.6, b=3.9),
       dict(k="box", x1=510, x2=570, p1=46, p2=60, col="gold", fill=0.18, a=0.75, b=3.9),
       dict(k="box", x1=620, x2=680, p1=40, p2=50, col="gold", fill=0.18, a=0.9, b=3.9),
       dict(k="pill", text="WRONG", col="red", x=260, y=Y(48), a=2.3, b=3.9),
       dict(k="pill", text="WRONG", col="red", x=540, y=Y(40), a=2.5, b=3.9),
       dict(k="pill", text="?", col="gold", fg=(20,20,22), size=44, x=650, y=Y(33), a=2.7, b=3.9)]
EL += [dict(k="nums", x0=290, dx=250, y=960, a=4.2, b=6.88)]
# rule 1: break of structure
EL += cs([(70,72,58,60),(60,66,56,64),(64,65,48,50),(50,52,40,42),(42,62,41,60),(60,76,59,74)], 180, 110, 6.95, 11.68, extra={4:(8.0,0.3),5:(8.5,0.3)})
EL += [dict(k="box", x1=470, x2=1000, p1=40, p2=52, col="gold", fill=0.12, a=7.4, b=11.68),
       dict(k="label", text="ORDER BLOCK", x=860, y=Y(46), size=26, col="gold", a=7.5, b=11.68),
       dict(k="hline", p=66, x1=250, x2=980, col="gray", a=7.6, b=11.68),
       dict(k="label", text="SWING HIGH", x=900, y=Y(66)-28, size=24, col="gray", a=7.7, b=11.68),
       dict(k="pill", text="BREAK OF STRUCTURE", col="green", x=700, y=Y(84), a=8.6, b=11.68)]
# rule 2: FVG
EL += cs([(60,62,50,52),(52,54,44,46),(46,70,45,68),(68,76,64,74),(74,78,70,77),(77,84,75,82)], 230, 110, 11.75, 17.64, extra={2:(12.9,0.3),3:(13.2,0.25)})
EL += [dict(k="box", x1=300, x2=380, p1=44, p2=54, col="blue", fill=0.22, a=12.3, b=17.64),
       dict(k="label", text="OB", x=340, y=Y(40), size=26, col="blue", a=12.4, b=17.64),
       dict(k="box", x1=380, x2=1000, p1=54, p2=64, col="gold", fill=0.16, a=14.2, b=17.64),
       dict(k="pill", text="FAIR VALUE GAP", col="gold", fg=(20,20,22), x=800, y=Y(50), a=14.3, b=17.64),
       dict(k="pill", text="BIG MONEY", col="green", x=450, y=Y(80), a=15.9, b=17.64)]
# rule 3: unmitigated
EL += cs([(45,47,32,34),(34,55,33,53),(53,57,50,55),(55,56,38,40),(40,52,39,50),(50,51,46,47),(47,70,46,68),(68,75,66,73)], 180, 95, 17.75, 22.22, stag=0.08)
EL += [dict(k="box", x1=130, x2=520, p1=34, p2=45, col="red", fill=0.14, a=18.4, b=22.22),
       dict(k="box", x1=630, x2=1000, p1=46, p2=51, col="green", fill=0.18, a=18.6, b=22.22),
       dict(k="pill", text="MITIGATED", col="red", x=330, y=Y(26), a=19.3, b=22.22),
       dict(k="pill", text="FRESH", col="green", x=850, y=Y(40), a=19.5, b=22.22),
       dict(k="ring", x=465, y=Y(39), r=34, col="red", a=20.98, b=22.22)]
# all three
EL += [dict(k="nums", x0=290, dx=250, y=900, a=22.3, b=24.56, col="green"),
       dict(k="pill", text="WAIT FOR MY ENTRY", col="green", size=40, x=540, y=1150, a=22.9, b=24.56)]
HEAD = [(0, "XAU/USD", "NOT EVERY ORDER BLOCK WORKS", "orange"), (2.02, "MOST TRADERS", "PICK THE WRONG ONE", "red"),
        (3.9, "HERE ARE", "3 RULES FOR A VALID OB", "orange"),
        (6.88, "RULE 1", "IT MUST BREAK STRUCTURE", "green"), (9.84, "NO BREAK", "NO ORDER BLOCK", "red"),
        (11.68, "RULE 2", "IT LEAVES A GAP BEHIND", "green"), (15.2, "THAT GAP PROVES", "BIG MONEY STEPPED IN", "green"),
        (17.64, "RULE 3", "IT MUST BE UNMITIGATED", "orange"), (20.34, "PRICE HASN'T", "COME BACK TO IT YET", "orange"),
        (22.22, "ALL THREE?", "THAT'S WHERE I WAIT", "green")]
BG = [(0, "orange"), (2.02, "red"), (3.9, "orange"), (6.88, "green"), (9.84, "red"), (11.68, "green"), (17.64, "orange"), (22.22, "green")]
SFX = [("whoosh", t) for t in (2.02, 3.9, 6.88, 11.68, 17.64, 22.22)] + [("pop", t) for t in (0.6, 0.75, 0.9, 4.2, 4.45, 4.7, 7.4, 12.3, 14.3, 18.4, 18.6, 19.3, 19.5, 22.3, 22.55, 22.8, 22.9)] + \
      [("impact", t) for t in (2.3, 8.6, 15.9, 20.98)]
e, h, b, s = cta(24.56, 25.84, 26.32, 27.24, 30.0, DUR); EL += e; HEAD += h; BG += b; SFX += s
