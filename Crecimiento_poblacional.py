#Diego Ivan Morales Gallardo
#Programa que calcula el crecimiento de una población
import math
#Pedir los datos
ni = int(input("Dame la población incial: "))
t = int(input("Dame el tiempo en años: "))
r = float(input("Dame la tasa de crecimiento entre 0 y 1: "))
#Fórmula para calcular el crecimiento
poblacion = math.trunc(ni*((math.e)**(r*t)))
#Imprimir el resultado
print(f"El crecimiento de la poblacion es de: {poblacion}")