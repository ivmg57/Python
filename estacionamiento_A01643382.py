# Autor: 
import random, time, os

def clrscr():
    # If en una sola línea
    os.system("clear") if os.name == "posix" else os.system("cls")
    
def simulacion():
    try:
        # Abrir el archivo como de escritura
    except IOError:
        print("No se puede abrir o generar el archivo")
    else:
        #Generar aleatoriamente un archivo de 0 y 1s
        #Cerrar el archivo

def mapa_estacionamiento():
    try:
        # Abrir el archivo como de lectura
    except IOError:
        print("No se puede abrir o leer el archivo")
    else:
        letras="abcdefghij"
        cont=0
        print('-------'*15)
        #Leer el archivo y desplegar el mapa
        #Cerrar el archivo
        print('-------'*15)
       
    
def despliega_linea(letra,linea):
    for i, espacio in enumerate(linea):
        if espacio == "0":
            vacio=letra+str(i+1)
            print(f"|{vacio.center(5)}|", end="")
        else:
            print("|  X  |", end="")
    print('|')
    
#Programa principal
def main():
    opc=""
    while opc!='3':
        clrscr()
        opc=input('''
    1. Recibe datos de sensores...
    2. Despliega mapa de estacionamiento...
    3. Salir
    Opción: ''')
        if opc=="1":
            print("Solicitando datos al sistema de sensores...")
            time.sleep(2)
            simulacion()
            print("Finaliza la carga de datos")
            input("Enter para continuar")
        elif opc=="2":
            print("Generando mapa de espacios vacios...")
            time.sleep(2)
            mapa_estacionamiento()
            input("Enter para continuar")
        elif opc=="3":
            print("Saliendo del sistema")
        else:
            print("Opción inválida")

main()