from colorama import Fore, Back, Style
from os import system
from pickle import dump, load

red = Fore.RED
red2 = Fore.LIGHTRED_EX
grn = Fore.GREEN
grn2 = Fore.LIGHTGREEN_EX
ylw = Fore.YELLOW
blu = Fore.CYAN
white = Fore.WHITE
name = "Acrux"
ver = "2.1"
build = "Luna"
dev = "90 Computer Studios"
key = "_$ "
blklist = ["/", "\ ", "<", ">", "*", "?", "|", ":"]
commands = "commands3827.acrx"
dig = ("@", "(", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")")
smile = ""

ia=red + f"Invalid argument"
nv=red + "No value given"
iclr = "Invalid Color"

def cs():
    system("cls")
