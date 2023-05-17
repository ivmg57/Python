#Diego Ivan Morales Gallardo
#Programa para practicar uso de while y funciones con un menú

def repite_palabra(palabra,n):
  for i in range(1,n+1):
    print(f"{i}. {palabra}")

def impares_hasta(n):
  numero = 1
  while numero <= n:
    print(numero, end=" ")
    numero += 2
    print()

def suma_consecutivos_hasta(n):
  for i in range(1,n+1):
    acumulador = acumulador + n
  return acumulador

def promedio(n):
  suma = 0
  for num in range(n):
    dato = int(input("Ingresa un número: "))
    suma = suma + dato
  promedio = suma/n
  return promedio

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
      num = int(input("Ingrese cantidad de veces a repetir: "))
      repite_palabra(palabrita,num)
    elif opc == "2":
      num = int(input("Ingresa el límite: "))
      if num > 0:
        impares_hasta(num)
      else:
        print("No funciona esta opción para negativos")
    elif opc == "3":
      num = int(input("Ingresa el límite: "))
      if num > 0:
        resultado = suma_consecutivos_hasta(num)
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