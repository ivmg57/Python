#Diego Ivan Morales Gallardo
#Escribe una función que reciba como parámetro 2 números enteros y una clave que es una letra.
#s: Suma
#r: Resta
#m: Multiplicación
#d: División
#La función debe aplicar la operación aritmética a los 2 valores recibidos y regresar como valor de retorno el resultado de dicha operación.
#Nota que dentro de la función no mostrarás nada, solo regresarás el valor usando return.
#Escribe ahora una función main en la que pidas al usuario teclear 2 valores numéricos y una clave (s, r, m, d), después llama la función con los parámetros correspondientes y luego muestra el resultado de la operación que regresó la función.
def operacionesAritmeticas(float1,float2,clave):
  if clave == "s":
    resultado = float1 + float2
  elif clave == "r":
    resultado = float1 - float2
  elif clave == "m":
    resultado = float1 * float2
  elif clave == "d":
    resultado = float1 / float2
  else:
    print("Respuesta incorrecta")
  return resultado

def main():
  num1 = float(input("Escribe el primer valor numérico: "))
  num2 = float(input("Escribe el segundo valor numérico: "))
  clave = input("Escribe la clave de acuerdo a la operación aritmética: ")
  print("s: Suma\nr: Resta\nm: Multiplicación\nd: División")