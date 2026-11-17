"""Standard NiccoFX CTA ending: playbook PDF -> follow + comment SMA -> not delivered -> delivered."""
def cta(t_want, t_follow, t_comment, t_if, t_end, dur, key="SMA"):
    EL = [dict(k="ui", ui="pdf", x=540, y=930, rot=-6, a=t_want + 0.15, b=t_follow - 0.05),
          dict(k="ui", ui="pdf", x=540, y=760, s=0.55, rot=-6, a=t_follow, b=t_if),
          dict(k="ui", ui="profile", x=540, y=1010, a=t_follow + 0.05, b=t_if),
          dict(k="ui", ui="comment", x=540, y=1170, a=t_comment, b=t_if, type=key),
          dict(k="ui", ui="dm", x=540, y=960, a=t_if + 0.05, b=t_end, ok=False),
          dict(k="pill", text="NOT DELIVERED", col="red", size=44, x=640, y=1150, rot=-8, a=t_if + 1.1, b=t_end),
          dict(k="ui", ui="dm", x=540, y=960, a=t_end, b=dur, ok=True)]
    HEAD = [(t_want, "WANT MY", "FREE GOLD PLAYBOOK", "orange"), (t_follow, "FOLLOW & COMMENT", f'"{key}"', "orange"),
            (t_if, "IF YOU DON'T FOLLOW", "NO PDF IN YOUR DM", "red"), (t_end, "FOLLOW FOR", "DAILY GOLD TRICKS", "green")]
    BG = [(t_want, "orange"), (t_if, "red"), (t_end, "green")]
    SFX = [("whoosh", t_want), ("whoosh", t_if), ("whoosh", t_end), ("pop", t_want + 0.15), ("pop", t_follow + 0.05),
           ("pop", t_comment + 0.3), ("pop", t_if + 1.1), ("ding", t_end + 0.1)]
    return EL, HEAD, BG, SFX
