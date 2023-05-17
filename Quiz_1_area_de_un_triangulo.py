#Programa que calcula el área de un triángulo a partir del valor de dos de sus lados y el ángulo
#Datos de entrada: a(primer lado), b(segundo lado) y c(angulo)
import math
a = float(input("Dame el valor del primer lado: "))
b = float(input("Dame el valor del segundo lado: "))
c = math.radians(float(input("Dame el valor del ángulo: ")))
#Calcular el área (Salida)
area = (0.5*a*b)*math.sin(c)
#Imprimir el resultado
print(f"El área del triángulo es: {area}")