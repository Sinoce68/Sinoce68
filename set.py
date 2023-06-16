from os import system as s
import os
import pyautogui as pg
from pyautogui import hotkey as key
from pyautogui import typewrite as tp
from time import sleep as sp
from random import choice as ch
import subprocess as sb
from colorama import Fore as c
import sys
#     try:
#         Group_Guid=wolf.joinGroup(Link)["data"]["group"]["group_guid"]
#     except KeyError:
#         print("NOT OK GROUP")
#     while 1:
#         try:
#             try:
#                 min_id = wolf.getGroupInfo(Group_Guid)["data"]["chat"]["last_message_id"]                
#             except KeyError:
#                 pass
#             messages = wolf.getMessages(Group_Guid,min_id)
#             ans = input(f'''({lrd}┌─<({cy}Sinoce{gr}@{lmg}({lcy}Root{lmg}){lrd}-{yl}[~]{lrd}>
#  └─< ({gr}#root{lrd}){rd}* {lrd}>──»  {cy} ''')
#             wolf.sendMessage(ans)
#             for msg in messages:
#                 if msg['type'] == 'Text' :
#                         if msg.get('message_id') not in msgs:
#                             msgs.append(msg.get("message_id"))
#                             text = str(msg.get('text'))
#                             print(text)

password = 'Sinoce68/Rubika'

user = sb.getoutput('echo %Username%')

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

auth = 'tkbaqlcbeqqbeiqawdhwyzscfjshbvde'
Link = 'https://rubika.ir/joing/EDCDEJEG0ONCRUTIUYFEUEYJYQQQGBJZ'
nog = '.'
msgs = []
def wolf__Secret():
        pass
for start in range(5):
        print(f"{lgr}START {nog}")
        sp(0.5)
        s('cls')
        nog += '.'
        if nog == '....':
            s('cls')
            break
print(f'..{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce')
print(f'..{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}....')
print(f'..{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce')
print(f'..{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}....')
print(f'..{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce')
print(f'..{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}....')
print(f'..{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce{lyl}......{lrd}Sinoce')

print('\n')
print(f'{lgr}Welcome To {bl}Hsc {rd}*{lrd}*{yl}*{lyl}*')
print('\n')
system =  sb.getoutput('echo %Os%')
sets = {}
File_WF = open('Wifi_Pass.txt','w')
file_com = open('Commands.txt','w')

def Terminal_Pro():
    while 1:
        try:    
            try:
                ans = input(f'''({lrd}┌─<({cy}Sinoce{gr}@{lmg}({lcy}Root{lmg}){lrd}-{yl}[~]{lrd}>
    └─< ({gr}#root{lrd}){rd}* {lrd}>──»  {cy} ''')
                if ans.startswith('cd '):
                    dr = ans.replace('cd ','')
                    os.chdir(dr)
                    file_com.write(ans)
                else:
                    pass
                if ans == 'cd ..':
                    os.chdir('.')
                    file_com.write(ans)
                else:
                    pass
                if ans.startswith('set '):
                    file_com.write(ans)
                    r = str(ans.replace('set ','')).split('=')
                    var = r[0]
                    command = r[1]
                else:
                    pass
                if ans.startswith('%'):
                    file_com.write(ans)
                    se = str(ans.replace('%','')).split('%')
                    print(f"VAR = {var} COMMAND = {command}")
                else:
                    pass
                if ans.lower() == 'exit':
                    break
                if ans.lower() == 'pwd':
                    file_com.write(ans)
                    pwd = sb.getoutput('cd')
                    print(f'{lgr}YOUR LOCATION{lrd} >>{lbl} '+pwd)
                else:
                    pass
                if ans.lower() == 'screen':
                    file_com.write(ans)
                    pg.screenshot('SRCEENSHOT.jpg')
                else:
                    pass
                if ans == ('uname'):
                    file_com.write(ans)
                    print(f'{bl}YOUR SYSTEM {rd}--{lrd}>> '+str(sb.getoutput('echo %Os%')))
                else:
                    pass
                if ans.lower() == 'clear' or ans == 'cls':
                    if system.startswith('Win'):
                        s('cls')
                    else:
                        s('clear')
                if ans.lower().startswith('dir'):
                    s(ans)
                if ans.startswith('netsh '):
                    s(ans)
                if ans == 'netsh':
                    s(ans)
                if ans == 'reload':
                    print(f'{lbl}Welcome {cy}From {lcy}New{lgr} Terminal {yl}*{lyl}*{rd}*{lrd}*')
                    Terminal_Pro()
                if ans.startswith('wifi_sin '):
                    wifi = ans.replace('wifi_sin ','')
                    File_WF = open(f'Wifi_Pass{wifi}.txt','w')
                    profile_wifi = str(f'netsh wlan show profiles {wifi} key=clear | findstr Key')
                    Attack = sb.getoutput(str('profile_wifi'+f' > Wifi_Pass.txt'))
                    print(f'{lrd}PASSWORD {lgr}Wireless {lmg}{wifi}{lyl} -->>{lgr} Wifi_Pass_{wifi}.txt')
                if ans.startswith('passwd '):
                    pas = ans.replace('passwd ','')
                    pass_change = sb.getoutput(f'net user {user} {pas}')
                    print(f'{lcy}USERNAME {lbl}--{lgr}{user}{lbl}-- {lcy}PASSWORD{lrd} CHANGED{lbl} --{lgr}{pas}{lbl}-- ')
                if ans == 'Users':
                    users = sb.getoutput('net user').split('DefaultAccount')
                    print(users)
            except EOFError:
                pass
        except KeyboardInterrupt:
            paswd =  input(f'ENTER PASSWORD FROM EXIT {lmg}')
            if paswd == password:
                print("PASSWORD IS CORRECT ")
                sp(2)
                wolf__Secret()
            else:
                file_com.write(paswd)
                pass
            print(f"{lgr}Sinoce Is Not Access {lrd} EXIT")
            pass
Terminal_Pro()