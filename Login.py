import pyautogui as pg
from os import system as s
from cryptography.fernet import Fernet as f
import os

key_pass = b'wuWQORn79jqhm-wLYCNJWwyo_S7cmXHMdM308ADwnuM='
key_ = f(key_pass)
with open('Rubika\passwd.txt','rb')as pfile:
    pread = pfile.read()
passwd = key_.decrypt(pread).decode()
code = input("ENTER TEXT ENCRIPT : ").encode()
enc_code = key_.encrypt(code)
print(enc_code)
names = ['mehdi','sinoce','navid','rubika']


ans = pg.password(text='ENTER USERNAME',title='H S C',mask='=')
while ans != 'mehdi':
    if ans == 'download.php':
        s('notepad Rubika\passwd.txt')
        s('msg * Welcome From Administrator')
    ans = pg.password(text='ENTER USERNAME',title='H S C',mask='=')
ans = pg.password(text='ENTER PASSWORD',title='H S C',mask='*')
while ans != passwd:
    ans = pg.password(text='ENTER PASSWORD',title='H S C',mask='*')
s('notepad')
s('python Main.py')