from config import *

def find(cmd):
    applist = ["about", "CALC"]
    if cmd == applist[0]:
        print(applist)
    elif cmd == applist[1]:
        result = False
        num1 = int(input("Type a number: "))
        op = input("Type an operator: ")
        num2 = int(input("Type another number: "))

        if op == "+":
            print(num1+num2)
            result = True
        if op == "-":
            print(num1-num2)
            result = True
        if op == "*":
            print(num1*num2)
            result = True
        if op == "x":
            print(num1*num2)
            result = True
        if op == "X":
            print(num1*num2)
            result = True
        if op == "/":
            print(num1/num2)
            result = True
        else:
            if result == True:
                pass
            else:
                print(red + "Invalid operator")




    else:
        print(red + "Cannot find program")
