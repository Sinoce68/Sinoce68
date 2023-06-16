import email

from pygame import mixer

from tkinter import *

from tkinter.messagebox import *

users = [{"email":"zari45@gmail.com","password":"09933587856"}]

def login():

global password_input, email_input

password = password_input.get()

email = email_input.get()

for person in users:

if person["email"]== email:

if person["password"] == password:

showinfo("هک موفقیت امیز بود", "قربانی هک شد پسورد قربانی برای شما ارسال شد")

else:

showwarning("ایمیل موجود نیست", "لطفا ایمیل درست را وارد کنید!")

users.append({"email":email,"password":password})

else:

showwarning("شماره موجود نیست", "لطفا شماره درست بزنید!")

window = Tk()

window.geometry("500x500")

window.title("هک ایمیل")

imge = PhotoImage(file="admin.png")

File = "hak.mp3"

mixer.init()

mixer.music.load(File)

mixer.music.play()

window.iconphoto(False, imge)

labels_conf = dict(fg="red", bg="black", font=("fantacy", 18, "bold"), padx=10,pady=8)

entry_conf = dict(fg="red", bg="black", font=("fantacy", 18, "bold"))

title_label = Label(text="هک ایمیل",**labels_conf)

email_label = Label(text=":ایمیل قربانی را وارد",**labels_conf)

email_input = Entry()

email_input.configure(**entry_conf)

password_label = Label(text=":شماره خودتان برای ارسال پسورد قربانی بنویسید",**labels_conf)

password_input = Entry()

password_input.configure(**entry_conf)

cancel_btn = Button(text="خارج شدن از برنامه", **labels_conf,width=300, command=window.quit)

sing_up_btn = Button(text="برای هک کلیک کنید", **labels_conf,width=300, command=login)

window.config(bg="red")

title_label.pack(padx=10,pady=10)

email_label.pack(anchor=W, padx=10)

email_input.pack(anchor=W, padx=10, pady=10)

password_label.pack(anchor=W, padx=10)

password_input.pack(anchor=W, padx=10, pady=10)

sing_up_btn.pack(anchor=W, padx=10, pady=5)

cancel_btn.pack(anchor=W, padx=10, pady=5)

window.mainloop()