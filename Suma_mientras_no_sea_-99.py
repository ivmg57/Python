#Diego Ivan Morales Gallardo
#Escribe un programa que pida al usuario teclear un número y lo agregue a una suma, el programa se debe repetir mientras el número tecleado no sea -99. Cuando se teclee este valor el programa deberá mostrar un mensaje que diga cuantos números se sumaron y la suma de los números tecleados (sin contar ni sumar el -99).

def suma_menos99():
  suma = 0
  cont = 0
  num = int(input("Número: "))
  while num != -99:
    suma += num
    cont += 1
    num = int(input("Número: "))
  print(f"La suma de los números es {suma}")
  print(f"Se sumaron {cont} números")

def main():
  suma_menos99()

main()