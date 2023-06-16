from os import system as s
from pyautogui import hotkey as key
from pyautogui import typewrite as tp
from time import sleep as sp


dafe = int(input('ENTER NUMBER DAFE : '))
tedad = int(input("ENTER NUMBER DAFE : "))


for i in range(dafe):
    for td in range(tedad):
        s('start sms_pro.py')
        sp(1)
        tp('09940113531')
        sp(1)
        key('Enter')
        tp('5')
        key('Enter')
        sp(1)

sp(25)
s("taskkill /f /im py.exe")
s("taskkill /f /im cmd.exe")
s("taskkill /f /im sms_bomber.py")
