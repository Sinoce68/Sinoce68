from os import system as s
from subprocess import getoutput as out

drives = str(out('fsutil fsinfo drives')).split()
for i in drives[1:]:
    files = out(f'dir /S /B {i[0]}:\*.exe')
    print(f"SEARCHING FILLES DRIVE {i[0]}")
    print('\n')
    print(files)