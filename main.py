import eel
import socket
import threading
import os
from tkinter.messagebox import showwarning
import sys
eel.init("DESIGN")
txt_files = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".andrewschatconfig"):
        txt_files.append(file)
try:
    f=open(txt_files[0]).read()
    f=f.split(":")
except:
    showwarning("Предупреждение","Проверьте файл конфигурации")
    sys.exit(1)
username=""
sock = socket.socket()
@eel.expose
def take_andsend(mode,mes,pin):
    username=mes
    sock.connect((f[0], int(f[1])))
    sock.settimeout(5000)
    sock.send(bytes(mode+"><"+mes+"><"+pin,"utf8"))
    a.start()
   

@eel.expose
def sendmessage(text):
    sock.send(bytes(text,"utf8"))
    eel.mynewmessage(text)
def resivemes():
    print("start")
    while True:
        datames=sock.recv(1024)
        message = datames.decode()
        print(message)
        eel.yournewmessage(message)
        if(message=="YOURAPPLE"):
            eel.show("/foreror/error.html")
        if(message=="YOUAReAPPLE" or message=="успешно"):
            eel.show("/chat/index.html")
        if(message=="loginzanyat"):
            eel.show("/foreror/errorreg.html")

a = threading.Thread(target=resivemes)



eel.start("login.html",size=(1500,1500))

