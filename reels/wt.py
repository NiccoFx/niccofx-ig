import json, sys
from faster_whisper import WhisperModel
m = WhisperModel("base.en", compute_type="int8")
segs, _ = m.transcribe(sys.argv[1], word_timestamps=True)
w = [[x.word.strip(), round(x.start, 2), round(x.end, 2)] for s in segs for x in s.words]
json.dump(w, open(sys.argv[2], 'w')); print(' '.join(f"{a}@{b}" for a, b, c in w)); print('END', w[-1][2])
