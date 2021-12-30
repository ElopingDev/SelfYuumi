import socket
from time import sleep
import pyautogui
import keyboard

yuumi_ip = "1.2.3.4"  # <- HAMACHI IP
# yuumi_ip = socket.gethostname()
port = 3333

s = socket.socket()
s.connect((yuumi_ip, port))

bindings = {
    '1': '-101 ',
    '2': '-102 ',
    '3': '-103 ',
    '4': '-104 ',
    '5': '-105 ',
    '6': '-106 ',
}

while True:
    messaggio = ""
    x, y = pyautogui.position()
    messaggio += str(x) + " " + str(y) + " "
    for bind in bindings:
        if keyboard.is_pressed(bind):
            messaggio += bindings[bind]  # TODO mettere timer per anti spam
    messaggio += "-1 "
    s.send(messaggio.encode('utf-8'))
    # print(messaggio)
    sleep(.01)
    # s.close()
