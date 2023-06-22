# modules

import os
import datetime
import pickle
import shutil
from colorama import init
from config import *
import programs

# /modules

# config

init(autoreset=True)
installed = 0
setup = 0
allow = False
logged = 0

# /config

# setup

while allow !=True:
    if os.path.exists("sys3827/setup.acrx"):
        sys_ch = pickle.load(open("sys3827/setup.acrx", "rb"))
        if sys_ch == 1:
            os.chdir("sys3827")
            com = os.getcwd()
            logon_data = os.getcwd() + "/logon3827.acrx"
            os.chdir("..")
            allow = 1
        elif sys_ch == 0:
            setup = 1
            allow = True
        else:
            print(red + "System Error: setup.acrx is damaged")
            exit()
    else:
        setup = 1
        allow = True

if setup == 1:
    allow2 = False

    while allow2 !=True:
        print(red2 + name, white + ver, build, "Setup")
        print()
        print("[1] Continue with setup")
        print("[2] Exit")

        setup = input()
        if setup == "1":
            if os.path.exists("sys3827"):
                shutil.rmtree("sys3827")
            else:
                pass
            if os.path.exists("users"):
                shutil.rmtree("users")
            else:
                pass
            cs()
            os.mkdir("sys3827")
            os.mkdir("users")
            os.chdir("users")
            os.mkdir("main")
            os.chdir("..")
            os.chdir("sys3827")
            print("Creating sys commands.acrx...")

            f = open(commands, "w+")
            f.write(f"""
SYSTEM:


help | Brings up this menu
about | about {name}
cs | Clears the screen
time | Shows the date/time
app.*app name* | Opens programs (app.about to check apps)
ex | Exit {name}


EXPLORER:


cd *folder name* | Opens folders
cd.. | Goes back a folder

del *file/folder name* | Deletes files/folders

dir | View files/folders in directory

cr -tf - Makes a file
cr -f - Makes a folder

op -tf - Opens text files
op -p - Opens programs (not available yet)
""")
            f.close()
            com = os.getcwd()
            os.chdir("..")
            print()
            print(grn + "Done!")
            input("Press enter to continue... ")
            cs()
            print("""
        ▄▀█ █▀▀ █▀█ █░█ ▀▄▀
        █▀█ █▄▄ █▀▄ █▄█ █░█
            """)
            print()
            print(grn + "           Setup User:")
            print()
            username = (input("Username" + key))
            password = (input("Password" + key))
            login = [username, password]
            os.chdir("sys3827")
            pickle.dump(login, open("logon3827.acrx", "wb"))
            installed = 1
            pickle.dump(installed, open("setup.acrx", "wb"))
            os.chdir("..")
            cs()
            logged = 1
            allow = True
            allow2 = True
        elif setup == "2":
            exit()
        else:
            cs()
            print(red + "Invalid input")

# /setup

# login

if logged == 1:
    pass
else:
    logged = 0
    print("""
    ▄▀█ █▀▀ █▀█ █░█ ▀▄▀
    █▀█ █▄▄ █▀▄ █▄█ █░█
    """)
    print(grn + "           Login:")
    while logged !=1:
        username = (input("Username" + key))
        password = (input("Password" + key))
        cs()
        login = [username, password]
        check = pickle.load(open("sys3827/logon3827.acrx", "rb"))
        if login == check:
            print(grn + "Success!")
            logged=1
        else:
            print(red + "Incorrect username or password")

os.chdir("users")
os.chdir("main")

# /login

# kernal

while True:
    cmd = (input(os.getcwd() + key))

    if cmd == "help":
        current = os.getcwd()
        os.chdir(com)
        list_cmd = open(commands, "r")
        print(list_cmd.read())
        list_cmd.close()
        os.chdir(current)
    elif cmd == "cs":
        cs()
    elif cmd == "about":
        print(name, ver, build, "By", dev)
    
    elif cmd == "time":
        now = datetime.datetime.now()
        print ()
        print (now.strftime("Current date and time: " + "%Y-%m-%d %H:%M:%S"))
    elif cmd == "ex":
        exit()
    
# explorer

    elif cmd.startswith("cr "):
        if cmd.startswith("cr -f"):
            cmd = cmd.replace("cr -f ", "")
            if cmd == "sys3827":
                print(red + "Folder cannot be created")
            else:
                os.mkdir(cmd)
        elif cmd.startswith("cr -tf"):
            namee = cmd.replace("cr -tf ", "")
            cmd = input()
            doc = open(namee, "w+")
            doc.write(cmd)
            doc.close()
        else:
            print(red + "Invalid use of 'cr'")

    elif cmd.startswith("op "):
        if cmd.startswith("op -tf "):
            cmd = cmd.replace("op -tf ", "")
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
        elif cmd.startswith("op -p "):
            print(grn + "This feature will come to", grn + name, "soon!")

    elif cmd.startswith("del "):
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
        for x in res:
            print(x)
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

    elif cmd.startswith("app."):
        cmd = cmd.replace("app.", "")
        programs.find(cmd)

    else:
        print(red + "Invalid Command:", red2 + cmd)

# /kernal
