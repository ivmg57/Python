#Diego Ivan Morales Gallardo
#Escribe una función llamada areaRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el área del rectángulo.
#Escribe una función llamada perimetroRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el perímetro del rectángulo.
#Observa que dentro de las funciones no mostrarás nada, solo regresarás el valor calculado usando return.
#Escribe ahora una función main que pregunte al usuario el largo y ancho del rectángulo y después pregunte si quiere calcular el área o el perímetro del rectángulo (pide una clave a para área y p para perímetro) y después muestre el valor correspondiente al cálculo que pidió el usuario.

#Definir función para acalcular el área y sus parámetros
def areaRect(largo,ancho):
#Fórmula para calcular el área
  area = largo*ancho
#Regresar resultado
  return area

#Repetir lo mismo con el perímetro
def perimetroRect(largo,ancho):
  perimetro = 2*largo + 2*ancho
  return perimetro

def main():
  largo = float(input("Escribe el largo del rectángulo: "))
  ancho = float(input("Escribe el ancho del rectángulo: "))
  opcion = input("¿Quieres calcular el área o el perímetro? (a/p): ")
  if opcion == "a":
    area = areaRect(largo,ancho)
    print(f"El area del rectángulo es de: {area:.2f}")
  elif opcion == "p":
    perimetro = perimetroRect(largo,ancho)
    print(f"El perimetro del rectángulo es de: {perimetro:.2f}")
  else:
    print("Respuesta incorrecta")

main()