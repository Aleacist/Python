import time
import os
def clear():
    if os. getcwd() == 'C:\WINDOWS\System32' :
        os.system('cls')
    else: 
        os.system('clear')

def menu():
    print('Elija el script que vas a usar')
    time.sleep(0.25)
    print(' 1.-')
    time.sleep(0.25)
    print(' 2.-')
    time.sleep(0.25)
    print(' 3.-')
    time.sleep(0.25)
    print(' 4.-')
    time.sleep(0.25)
    print(' 5.-')
    time.sleep(0.25)
    print(' 6.-')
    time.sleep(0.25)
    print(' 7.-')
    time.sleep(0.25)
    print(' 8.-')
    time.sleep(0.25)
    print(' 9.-')
    time.sleep(0.25)
    print(' 10.-')
    time.sleep(0.25)
    MenuNum = input('Numero del script : ')
    try:
        MenuNum = int(MenuNum)
    except ValueError:
        print('Pase un numero entero')
        time.sleep(1)
        clear()
        menu()
    while MenuNum < 0 or MenuNum > 10 :
        print(MenuNum ,' no es uno de los scripts ')
        time.sleep(0.15)
        MenuNum = int(input('Por favor digan el numero de uno de los scripts : '))
    if MenuNum == 1:
        print("script 1")
        time.sleep(1)
        repeat = input('¿vas a seguir calculando? (s/n)')
        if repeat.lower() == 's' or repeat.lower() == 'si':
            clear()
            menu()
        else : return
    elif MenuNum == 2:
        print("script 2")
    elif MenuNum == 3:
        print("script 3")
    elif MenuNum == 4:
        print("script 4")
    elif MenuNum == 5:
        print("script 5")
    elif MenuNum == 6:
        print("script 6 ")
    elif MenuNum == 7:
        print("script 7")
    elif MenuNum == 8:
        print("script 8")
    elif MenuNum == 9:
        print("script 9 ")
    elif MenuNum == 10:
        print("script 10 ")


menu()