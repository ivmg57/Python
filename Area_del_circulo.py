#Diego Ivan Morales Gallardo
#Programa que calcula el área de un círculo
#Pedir el radio
radio = float(input("Ingresa el radio: "))
#Fórmula para el área
area = 3.1416*radio**2
#Imprimir el resultado
print("El area del circulo es", area)
# También se podría
print("El area del circulo es "+str(area))
print(f"El area del circulo de radio {radio} es {area:.2f}")