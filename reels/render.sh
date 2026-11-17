# usage: bash render.sh <spec_module> <workdir with vo.wav> <out.mp4>
set -e; R=$(cd "$(dirname "$0")" && pwd); SP=$1; WD=$2; OUT=$3
DUR=$(cd $R && SPEC=$SP python3 -c "import importlib,os;print(importlib.import_module(os.environ['SPEC']).DUR)")
MV=$(cd $R && SPEC=$SP python3 -c "import importlib,os;print(getattr(importlib.import_module(os.environ['SPEC']),'MUSIC_VOL',0.20))")
cd $R && SPEC=$SP python3 eng.py $WD/silent.mp4
cd $R && SPEC=$SP python3 mix.py $WD
ffmpeg -v error -y -i $WD/silent.mp4 -i $WD/vo.wav -i $WD/music.wav -i $WD/sfx.wav -filter_complex "[1]asplit=2[v1][v2];[2]volume=$MV[m];[m][v2]sidechaincompress=threshold=0.05:ratio=4:attack=8:release=280[md];[3]volume=0.42[s];[v1][md][s]amix=inputs=3:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=9[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -t $DUR -movflags +faststart $OUT
echo DONE $OUT
