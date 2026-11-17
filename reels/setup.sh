# usage: bash setup.sh   (run inside reels/ in the sandbox) — fetch fonts, build logo tiles
set -e; cd "$(dirname "$0")"; mkdir -p fonts kit
[ -f fonts/Anton.ttf ] || curl -sfL -o fonts/Anton.ttf https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf
[ -f fonts/Inter.ttf ] || curl -sfL -o fonts/Inter.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"
python3 - <<'PY'
from PIL import Image, ImageDraw
im=Image.open('logo_src.png').convert('RGBA'); w,h=im.size
tile=im.crop((int(w*0.03),int(h*0.03),int(w*0.97),int(h*0.97))); s=tile.size[0]
m=Image.new('L',tile.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,s-1,s-1],radius=int(s*0.2),fill=255)
tile.putalpha(m); tile.save('logo_tile.png'); print('logo ok')
PY
