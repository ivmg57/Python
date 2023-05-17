# Autor: Diego I
import random, time, os

def clrscr():
    # If en una sola línea
    os.system("clear") if os.name == "posix" else os.system("cls")
    
def simulacion():
    try:
        # Abrir el archivo como de escritura
        archivo = open('estaciona.txt','w')
    except IOError:
        print("No se puede abrir o generar el archivo")
    else:
        #Generar aleatoriamente un archivo de 0 y 1s
        for i in range(10):
          linea = []
          for dato in range(15):
            linea.append(str(random.randint(0,1)))
          a_escribir = ','.join(linea)
          archivo.write(a_escribir+'\n')
        #Cerrar el archivo
        archivo.close()

def mapa_estacionamiento():
    try:
        # Abrir el archivo como de lectura
        archivo = open('estaciona.txt','r')
    except IOError:
        print("No se puede abrir o leer el archivo")
    else:
        letras="abcdefghij"
        cont=0
        print('-------'*15)
        #Leer el archivo y desplegar el mapa
        for linea in archivo:
          lista = linea.rstrip().split(',')
          despliega_linea(letras[cont], lista)
          cont += 1
        #Cerrar el archivo
        archivo.close()
        print('-------'*15)
       
    
def despliega_linea(letra,linea):
    for i, espacio in enumerate(linea):
    #i regresa la posición y espacio regresa el elemento
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