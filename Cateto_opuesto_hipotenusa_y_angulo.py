#Diego Ivan Morales Gallardo
#Programa que calcula el cateto opuesto con base en la hipotenus y el ángulo
import math
#Pedir la hipotenusa y el ángulo
hipotenusa = float(input("Dame la hipotenusa: "))
angulo = float(input("Dame el ángulo: "))
#Convertir el ángulo a radianes
angulo = math.radians(angulo)
#Fórmula para calcular el cateto opuesto
catetoopuesto = math.sin(angulo)*hipotenusa
#Imprimir el resultado
print(f"El cateto opuesto del triángulo con hipotenusa de {hipotenusa} y un ángulo en radianes de {angulo} es de {catetoopuesto:.2f}")