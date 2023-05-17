#Diego Ivan Morales Gallardo
#Programa que indica si un número es par o impar y negativo o positivo
#Pedir el número
numero=int(input("Teclea un valor entero: "))
#Fórmula para par positivo
if numero>=0 and numero%2 == 0:
  print("Tu número es par positivo")
#Fórmula para impar positivo
elif numero>=0 and numero%2 != 0:
  print("Tu numero es impar positivo")
#Fórmula para par negativo
elif numero<0 and numero%2 == 0:
  print("Tu numero es par negativo")
#Fórmula para impar negativo
else:
  print("Tu número es impar negativo")