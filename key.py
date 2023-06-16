import pyautogui as pg
from os import system as s
from pygame import mixer as mix

mix.init()
mix.music.load('almas.mp3')

passwo = 'swgift.com'
userwo = 'Sinoce'

ans =pg.confirm('START HSC PYTHON ?','HSC STARTER',buttons=['START','DON T START'])
if ans == 'START':
    userw = pg.password(text='ENTER USERNAME : ',title='SINOCE')

    while 1:
        if userw == userwo:
            break
        else:
            userw = pg.password(text='ENTER USERNAME : ',title='SINOCE')
    passw = pg.password(text='ENTER PASSWORD : ',title='SINOCE')

    while 1:
        if passw == passwo:
            mix.music.play()

            
            
        else:
            passw = pg.password(text='ENTER PASSWORD : ',title='SINOCE')
else:
    s('msg %USERNAME% DON T START')
    exit()
