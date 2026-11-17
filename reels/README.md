# NiccoFX reel engine v4
Claude Code style shorts: glowing Anton headline + kicker, colored bg glow per beat, big glowing candles,
pill labels, standard CTA (PDF -> follow + comment -> not delivered -> delivered), @niccofx logo, Numo-KZ VO + music/SFX.
Sandbox: clone/curl this folder, `bash setup.sh`, put kit/*.mp3 (music,pop,whoosh,impact,ding), per reel a spec module
(spec_<name>.py with DUR, EL, HEAD, BG, SFX), a workdir with vo.wav, then `bash render.sh spec_<name> <workdir> out.mp4`.
Chart price scale: Y(p)=1560-10p (p 0..100). Headline at y=400, kicker y=300.
