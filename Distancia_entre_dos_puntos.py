#Diego Ivan Morales Gallardo
#Programa que calcula la distancia entre dos puntos
import math
#Pedir las coordenadas de los puntos
x1 = int(input("Dame x1: "))
y1 = int(input("Dame y1: "))
x2 = int(input("Dame x2: "))
y2 = int(input("Dame y2: "))
#Fórmula para calcular la distancia entre dos puntos
d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
#Imprimir el resultado
print(f"La distancia entre dos puntos es de {d:.2f}")