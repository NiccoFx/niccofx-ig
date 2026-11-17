import sys, subprocess, numpy as np, importlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
S = importlib.import_module(os.environ["SPEC"]); SR = 48000; N = int(S.DUR * SR); K = os.path.dirname(os.path.abspath(__file__)) + '/kit/'
def load(p):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()
def trim(x, th=0.003):
    nz = np.where(np.abs(x) > th)[0]; return x[nz[0]:] if len(nz) else x
m = load(getattr(S, 'MUSIC', K + 'music.mp3')); m = np.tile(m, int(np.ceil(N / len(m))))[:N]
f = int(1.5 * SR); m[-f:] *= np.linspace(1, 0, f); m[:int(0.3 * SR)] *= np.linspace(0, 1, int(0.3 * SR))
G = {'pop': 0.8, 'whoosh': 0.5, 'impact': 0.8, 'ding': 0.7, 'tick': 0.9, 'drop': 0.9}
G = {k: v for k, v in G.items() if os.path.exists(K + k + '.mp3')}
X = {k: trim(load(K + k + '.mp3')) for k in G}; X = {k: v / max(1e-6, np.abs(v).max()) for k, v in X.items()}
s = np.zeros(N, np.float32)
for kind, t in S.SFX:
    if kind not in X: continue
    x = X[kind] * G[kind]; t = max(0, t - 0.22) if kind == 'whoosh' else t
    if kind == 'drop': t = max(0, t - np.argmax(np.abs(X['drop'])) / SR)
    i = int(t * SR); j = min(N, i + len(x))
    if i < N: s[i:j] += x[:j - i]
def w(p, x): subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_s16le', p], input=np.clip(x, -1, 1).astype(np.float32).tobytes())
w(sys.argv[1] + '/music.wav', m * 0.9); w(sys.argv[1] + '/sfx.wav', s); print('mix ok')
