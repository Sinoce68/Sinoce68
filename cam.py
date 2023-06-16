import cv2
from time import sleep as sp
from colorama import Fore as c
from os import system as s
# from pyfiglet import figlet_format as pf
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
s('cls')
# print(ch(colors)+pf("CAMREA HACKING",'slant'))
# print(f"""{bl}CAMERA HACK {rd}
# ~ ~ ~ ~ ~{gr} ---{rd} 
# ~ ~ ~ ~{bl} ////{gr}  ---
# {lmg}    @@ {gr}*****{bl} //// {gr} ---      
# {lmg}       @@@ {gr} *****{bl} //// {gr} ---      
# {lmg}          @@@@ {gr}  *****{bl} ////{gr}   ---      
# {lmg}              @@@@@ {gr}   *****{bl} ////
# {lmg}                   @@@@@@ {gr}  *****
#                    """)
print(f"""
HH   HH        
HH   HH         S
HH   HH  
HHHHHHH
HH   HH
HH   HH
HH   HH""")
print('\n')

def start():
    while True:
        _, frame = cap.read()

        cv2.imshow("CAMREA CHMU10", frame)

        cv2.waitKey(5   )

ip = input(f"{gr}IP{bl} :{rd} ")
port = int(input(f"{gr}PORT{bl} :{rd} "))
cap = cv2.VideoCapture(f"http://{ip}:{port}/video")
print(f"{gr}STARTED SEARCHING{rd} IP {bl}. . .")
sp(15)
print(f"{rd}START HACKING{mg} CAMERA ")

sp(15)

print(f"{rd}HACKED FINISH {lrd}> {rd}>>{lrd} > ")
print(f"\n {lbl} TIME{gr} LIMITED{rd} 5")
sp(5)
start()

