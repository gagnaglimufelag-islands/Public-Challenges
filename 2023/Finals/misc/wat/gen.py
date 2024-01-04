import yaml
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent

im0 = open('wat_smol.png', 'rb').read()
im1 = open('wat_big.png', 'rb').read()

FLAG = yaml.safe_load(open('meta.yml'))['flags']

encoded = "".join(f"{ord(i):08b}" for i in FLAG)
print(encoded)

OUT = HERE / 'out'

if OUT.exists():
    shutil.rmtree(OUT)

OUT.mkdir()

for i, bit in enumerate(encoded):
    f = OUT / f'wat-{i}.png'
    f.write_bytes({'0': im0, '1': im1}[bit])


subprocess.run(['ffmpeg', '-i', 'wat-%d.png', '../wat.gif'], cwd=OUT)

shutil.rmtree(OUT)
