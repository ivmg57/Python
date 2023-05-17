#Diego Ivan Morales Gallardo
#Programa para practicar uso de while y funciones con un menú

def repite_palabra(palabra):
  numero = 1
  while numero <= 10:
    print(f"{numero}. {palabra}")
    numero += 1

def impares_hasta(n):
  numero = 1
  while numero <= n:
    print(numero, end=" ")
    numero += 2
    print()

def suma_hasta(n):
  numero = 1
  acumulador = 0
  while numero <= n:
    acumulador = acumulador + numero
    numero += 1
  return acumulador

def recibe_hasta(n):
  ahorro = 0
  dias = 0
  while ahorro <= n:
    deposito = float(input("Ingresa la cantidad a depositar: "))
    if deposito > 0:
      ahorro = ahorro + deposito
      dias += 1
    else:
      print("Cantidad inválida")
  print(f"Numero de depósitos: {dias}")
  return ahorro

def main():
  opc = 0
  while opc != "5":
    print("MENU")
    print("------------------------")
    print ("\t1.Repite palabra. ")
    print ("\t2.Impares hasta. ")
    print ("\t3.Suma hasta. ")
    print ("\t4.Recibe hasta. ")
    print("------------------------")
    opc = input("Opcion: ")
    if opc == "1":
      palabrita = input("Ingresa la palabra a repetir: ")
      repite_palabra(palabrita)
    elif opc == "2":
      num = int(input("Ingresa el límite: "))
      if num > 0:
        impares_hasta(num)
      else:
        print("No funciona esta opción para negativos")
    elif opc == "3":
      num = int(input("Ingresa el límite: "))
      if num > 0:
        resultado = suma_hasta(num)
        print(f"La suma de 1 hasta {num} es: {resultado}")
      else:
        print("No funciona esta opción para negativos")
    elif opc == "4":
      num = int(input("Ingresa el límite de ahorro: "))
      if num > 0:
        ahorro = recibe_hasta(num)
        print(f"El total de ahorro es de: {ahorro}")
      else:
        print("No funciona esta opción para negativos")
    else:
      print("Opcion inválida")

#Llamada a main
main()