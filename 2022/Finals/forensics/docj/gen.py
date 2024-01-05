from bs4 import BeautifulSoup, NavigableString
import zipfile
import json
from pathlib import Path

def dostuff(tree):
    if isinstance(tree, NavigableString):
        return str(tree)
    ob = {f'@{k}':v for k,v in tree.attrs.items()}
    ob[tree.name] = [dostuff(t) for t in tree.children]

    return ob

def fuck_up(xml):
    soup = BeautifulSoup(xml, features='xml')
    root = next(iter(soup))
    jsn = dostuff(root)
    return jsn


zf = zipfile.ZipFile('report.xlsx')

OUT = Path('report.xlsj')
if OUT.exists():
    OUT.unlink()

outfile = zipfile.ZipFile(OUT, 'w')

for f in zf.namelist():
    data = zf.read(f)
    if '.xml' in f :
        data = json.dumps(fuck_up(data)).encode()

    newpath = f.replace('.xml', '.json')
    outfile.writestr(str(newpath), data)

