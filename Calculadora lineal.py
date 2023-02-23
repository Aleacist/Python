# CALCULADORA CAIO
# Lo que tenemos que hacer:
#   Primero pasamos un string DONE
#   Que este lo pase a un array DONE
#   Que lea si es numero o letra
#   Que lea la operacion a realizar DONE
#   Si es division entre 0 que diga que es infinito DONE
#   Que respete las prioridades
#   Que lea los parentesis
#   Potencias y raices
#   Que resuelva ecuacuiones primer grado
#   Que resuelva operacion de segundo grado
#   Que resuelva 1 y 2 incognitas 
#   Seno,Coseno,Tangente
#   Log
#   Integrales y derivadas
#   Matrices
# 
# 

# Escribiendo Help/ayuda/info de una explicacion de como funciona

# Imports
import time
import os
import math

#Variables
TextInfo = [
    'inf',
    'info',
    'informacion',
    'ayuda',
    'help'
]

print('Calculadora')

#Menu

def Menu():
    OperacionUsuario = input()
    # OperacionUsuario.find(",posu")
    for i in TextInfo:
        if i == OperacionUsuario:
            Info(OperacionUsuario)
    Espacio(OperacionUsuario)

#Infomacion de como funciona la calculadora

def Info(OperacionUsuario):
    print('  Calculadora elaborada por Aday de la Cruz Sánchez')
    time.sleep(0.25)
    print('Para ejecutar operaciones sencillas como pueden ser suma,resta,multiplicacion o division simplemente escribanlo en una linea')
    time.sleep(0.25)
    print('ejemplo:  12+2')
    del OperacionUsuario
    Menu()

#Lector de operaciones

def Lector(OperacionUsuario): 
    Number=[] #Array para mover los resultado de los numeros del usuario a valor float/int
    Oper=[] #Array para el lector de operaciones 
    Num = '0' #Variable donde se crean los numero
    for i in OperacionUsuario:
        if i == '+' :
            Number.append(float(Num))
            Oper.append('+')
            Num = '0'
        elif i == '-':
            Number.append(float(Num))
            Oper.append('-')
            Num = '0'
        elif i == '*':
            Number.append(float(Num))
            Oper.append('*')
            Num = '0'
        elif i == '/':
            Number.append(float(Num))
            Oper.append('/')
            Num = '0'
        else:
            Num = Num + i
    Number.append(float(Num))
    Calc(Number,Oper)
    print(Number)
    time.sleep(1)
    Menu()

# Ordenador

def Order(OperacionUsuario):
    if OperacionUsuario.find("(") != -1 and OperacionUsuario.find(")") != -1:
        print('existesn parentesis en ',OperacionUsuario.find("("),"y",OperacionUsuario.find(")"))
        time.sleep(2)
        for i in range(OperacionUsuario.find("(")+1, OperacionUsuario.find(")")-1):      
            print(OperacionUsuario[i])
            time.sleep(1)
    else:
        Lector(OperacionUsuario)
    

# Limpiador de espacio

def Espacio(OperacionUsuario):
    OperacionUsuario = OperacionUsuario.strip()     # Limpia los espacios de las lineas de codigo al inicio y al final
    OperacionUsuario = OperacionUsuario.replace(" ", "") # Limpia los espacios de en medio
    Order(OperacionUsuario)


#Elector de operaciones

def Calc(Number,Oper):
    for i in Oper:
        if i == '+' :
            Suma(Number)
        elif i == '-':
            Resta(Number)
        elif i == '*':
            Multiplicacion(Number)
        elif i == '/':
            Division(Number)

#Operaciones Base

def Suma(Number):
    Number.insert(0,float(Number[0]+Number[1]))
    del Number[1]
    del Number[1]

def Resta(Number):
    Number.insert(0,float(Number[0]-Number[1]))
    del Number[1]
    del Number[1]

def Multiplicacion(Number):
    Number.insert(0,float(Number[0]*Number[1]))
    del Number[1]
    del Number[1]

def Division(Number):
    if Number[1] == 0:
        print('Infinito')
        return
    else:
        Number.insert(0,float(Number[0]/Number[1]))
    del Number[1]
    del Number[1]

Menu()