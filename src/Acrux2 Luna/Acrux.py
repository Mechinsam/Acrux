# modules

import os
import datetime
import pickle
import shutil
from colorama import init
from pygame.constants import USEREVENT_DROPFILE
from config import *
import Initiative_SDK as isdk
from pygame import mixer
import pyaudio
import wave
import sys
from random import randint

cs()

# /modules

# config
mixer.init()
init(autoreset=True)
installed = 0
setup = 0
allow = False
logged = 0
com = os.getcwd()
sys3827 = os.getcwd() + "/sys3827"
var_name = []
var_data = []
file_open = False
uvn=[".user", ".lcmd", ".out"]
uvd=["", "", ""]

os.system("title Acrux")

# /config

if os.path.exists("sys3827/username.acrx"):
    username = pickle.load(open("sys3827/username.acrx", "rb"))
else:
    username = input(f"Enter Username{key}")
    username = username.lower()
    username = username.capitalize()
    username_dump = pickle.dump(username, open("sys3827/username.acrx", "wb"))

smilechance=randint(1,100) # EATEREGG - 1% chance

if smilechance == 1:
    smile=":)"
else: pass

print(f"""
              :::      ::::::::  :::::::::  :::    ::: :::    ::: 
           :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:    :+:  
         +:+   +:+  +:+        +:+    +:+ +:+    +:+  +:+  +:+    
       +#++:++#++: +#+        +#++:++#:  +#+    +:+   +#++:+      
      +#+     +#+ +#+        +#+    +#+ +#+    +#+  +#+  +#+      
     #+#     #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+#      
    ###     ###  ########  ###    ###  ########  ###    ###

v{ver} {build}                 90 Computer Studios {smile}
""")

# script

uvd[0]=username
print(grn + f"Welcome {username.capitalize()}!")

while True:
    keychangechance=randint(1, 1000) # EATEREGG - 0.1% chance

    if keychangechance==1:
        key="_€ "
    else:
        key="_$ "
    
    if file_open == True:
        x=x+1
        if x == len(file):
            var_name=[]
            var_data=[]
            filer.close()
            file_open = False
            cmd = "nul"
        else:
            cmd = file[x]
    else:
        cmd = (input(os.getcwd() + key))


    i = 0
    while i !=len(var_name):
        if var_name[i] in cmd:
            if isinstance(var_data[i], int):
                pass
            else:
                cmd = cmd.replace(var_name[i], var_data[i])
                i+=1
        else:
            i +=1
    
    i=0
    while i !=len(uvn):
        if uvn[i] in cmd:
            if isinstance(uvn[i], int):
                pass
            else:
                cmd = cmd.replace(uvn[i], uvd[i])
        else:
            i+=1
    
    if ";" in cmd:
        cmd = cmd.split(";")
        cmd = cmd[0]

    uvd[1]=cmd



    if cmd == "help":
        current = os.getcwd()
        os.chdir(sys3827)
        list_cmd = open(commands, "r")
        print(list_cmd.read())
        list_cmd.close()
        os.chdir(current)
    elif cmd == "cs":
        cs()
    elif cmd == "about":
        print(f"""
{name} {ver} {build} by {dev}
[Open Source]

Made using Python3.9

MODULES USED:

- os
- datetime
- pickle
- shutil
- colorama
- Initiative_SDK
- pygame
- pyaudio
- wave
- sys

""")
    
    elif cmd == "time":
        now = datetime.datetime.now()
        print ()
        print (now.strftime("Current date and time: " + "%Y-%m-%d %H:%M:%S"))
    elif cmd == "ex":
        sys.exit()
    
# explorer

    elif cmd.startswith("cr"):
        cmd=cmd.replace("cr ", "")
        if cmd.startswith("-f"):
            cmd = cmd.replace("-f ", "")
            if cmd == "sys3827":
                print(red + "Folder cannot be created")
            else:
                os.mkdir(cmd)
        elif cmd.startswith("-tf"):
            namee = cmd.replace("-tf ", "")
            if ".acrx" in namee:
                print(red + "You cannot create .acrx files")
            else:
                cmd = input()
                doc = open(namee, "w+")
                doc.write(cmd)
                doc.close()
        else:
            print(red + "Invalid argument")

    elif cmd.startswith("op"):
        if cmd.startswith("-tf "):
            cmd = cmd.replace("-tf ", "")
            if os.path.exists(cmd):
                if os.path.isdir(cmd):
                    print(red + "Folders cannot be opened through this command")
                elif os.path.isfile(cmd):
                    if ".acrx" in cmd:
                        print(red + ".acrx files are written in binary and cannot be opened")
                    else:
                        cmd = cmd.replace("op -tf ", "")
                        doc = open(cmd, "r")
                        print(doc.read())
                        doc.close()
            else:
                print(red + "Path does not exist")
        else:
            print(red + "Invalid argument")

    elif cmd.startswith("del"):
        cmd = cmd.replace("del ", "")
        if os.path.exists(cmd):
            if os.path.isdir(cmd):
                if cmd == "sys3827":
                    print(red + "This is critical information to", red + name, red + "And cannot be deleted")
                else:
                    shutil.rmtree(cmd)
            elif os.path.isfile(cmd):
                if ".acrx" in cmd:
                    print(red + "This is critical information to", red + name, red + "And cannot be deleted")
                else:
                    os.remove(cmd)
            else:
                print(red + "This type of file cannot be deleted")
        else:
            print(red + "File/Folder does not exist")

    elif cmd == "dir":
        res = os.listdir(os.getcwd())
        print()
        for item in res:
            print(item)
        print()

    elif cmd.startswith("cd "):
        cmd = cmd.replace("cd ", "")
        if os.path.exists(cmd):
            if os.path.isdir(cmd):
                os.chdir(cmd)
            elif os.path.isfile(cmd):
                print(red + "Path given is a file")
            else:
                print(red + "Invalid input:", cmd)
        else:
            print(red + "Path does not exist")
    elif cmd == "cd..":
        os.chdir("..")

# /explorer

    elif cmd.startswith("app"):
        nfile = cmd.replace("app ", "")
        if os.path.exists(nfile):
            if nfile.endswith(".acrxp"):
                x = -1
                filer = open(nfile, "r")
                file = filer.read().splitlines()
                file_open = True
            else:
                print(red + "This cannot be opened as an app")
        else:
            print(red + "File does not exist")


    elif cmd.startswith(dig): # CALCULATOR
        print_=True
        if cmd.startswith("@"):
            cmd = cmd.replace("@", "")
            print_=False
        result, error = isdk.run("<stdin>", cmd)
        if error:
            print(error.as_string())
        else:
            result=str(result)
            uvd[2]=result
            if print_==False:
                pass
            else:
                print(result)


    elif cmd.startswith("var"):
        cmd=cmd.replace("var ", "")
        if cmd == "-cv":
            var_data=[]
            var_name=[]
        elif cmd.startswith("-c "):
            cmd = cmd.replace("-c ", "")
            if "=" in cmd:
                cmd = cmd.split("=")
                vname="<"+cmd[0]+">"
                vdata=cmd[1]
                if vname in var_name:
                    print(red+f"Variable: '{red2+vname+red}' is already defined")
                else:
                    var_name.append(vname)
                    var_data.append(vdata)
            else:
                print(nv)
        elif cmd == "-li":
            print("NAME :", var_name)
            print("VALUE:", var_data)
        elif cmd.startswith("-a"):
            cmd = cmd.replace("-a ", "")
            cmd = cmd.split("=")
            vdata=cmd[1]
            vname="<"+cmd[0]+">"
            if vname in var_name:
                print(red+f"Variable: '{red2+vname+red}' is already defined")
            else:
                vdata=input(vdata)
                var_name.append(vname)
                var_data.append(vdata)
        
    elif cmd == "nul":
        pass
    elif cmd == "":
        pass
    elif cmd.startswith(";"):
        pass
    elif cmd.startswith("pr"):
        if "-" in cmd:
            if cmd.startswith("pr -clr"):
                cmd = cmd.replace("pr -clr ", "")
                if cmd.startswith("-red"):
                    cmd = cmd.replace("-red ", "")
                    print(red + cmd)
                elif cmd.startswith("-red2"):
                    cmd = cmd.replace("-red2 ", "")
                    print(red2 + cmd)
                elif cmd.startswith("-grn"):
                    cmd = cmd.replace("(grn) ", "")
                    print(grn + cmd)
                elif cmd.startswith("-blu"):
                    cmd = cmd.replace("-blu ", "")
                    print(blu + cmd)
                elif cmd.startswith("-whi"):
                    cmd = cmd.replace("whi ", "")
                    print(white + cmd)
                else:
                    print(red + iclr)
        else:
            cmd = cmd.replace("pr ", "")
            print(cmd)
    elif cmd.startswith("sound"):
        cmd = cmd.replace("sound ", "")
        if cmd.startswith("-play "):
            cmd = cmd.replace("-play ", "")
            if os.path.exists(cmd):
                if cmd.endswith(".mp3"):
                   print(grn + "Playing", grn2 + cmd)
                   mixer.music.load(cmd)
                   mixer.music.play()
                elif cmd.endswith(".wav"):
                    print(red+"WAVs cannot be played")
                else:
                    print(red + "Unsupported file type")
            else:
                print(red + "Path does not exist")
        elif cmd.startswith("-rec "):
            input("Press enter to record sound and ctrl+c to stop ")
            audd = cmd
            audd = audd.replace("-rec ", "")
            audd = audd+".wav"
            print("Recording...")
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            
            frames = []
            try:
                while True:
                    data = stream.read(1024)
                    frames.append(data)
            except KeyboardInterrupt:
                pass
            
            stream.stop_stream()
            stream.close()
            audio.terminate()

            sound_file = wave.open(audd, "wb")
            sound_file.setnchannels(1)
            sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(44100)
            sound_file.writeframes(b"".join(frames))
            sound_file.close()
        else:
            print(ia)
    else:
        print(red + "Invalid Command:", red + cmd)

# /script
