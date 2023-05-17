#Diego Ivan Morales Gallardo
#Programa que calcula el área y volumen de una esfera
import math
#Pedir el radio
radio = float(input("Dame el radio: "))
#Fórmulas para área y volumen
area = 4*(math.pi*(radio**2))
volumen = (4*(math.pi*(radio**3)))/3
#Imprimir los resultados
print(f"El área de la esfera es de {area:.2f}")
print(f"El volumen de la esfera es de {volumen:.2f}")