from art import *
from pyfiglet import figlet_format as pf
from colorama import Fore as c
from random import choice as ch

gr,rd,bl,cy,mg,yl = c.GREEN,c.RED,c.BLUE,c.CYAN,c.MAGENTA,c.YELLOW
lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]

def banner():
    ber = text2art(ch(colors)+'H S C','random')
    print(ber)
def info():
    print(ch(colors)+'DEVLOPER SINOCE \n'+ch(colors)+' \b H S C '+f'{gr}2023{bl}/{gr}11{bl}/{gr}4')