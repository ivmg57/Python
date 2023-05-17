#Diego Ivan Morales Gallardo
#Programa que indica el tipo de triángulo
#Pedir el valor de cada lado
x=int(input("Indica el valor del primer lado: "))
y=int(input("Indica el valor del segundo lado: "))
z=int(input("Indica el valor del tercer lado: "))
#Comprobar si todos los lado son mayores a 0
if x>0 and y>0 and z>0:
#Comprobar que la suma de dos de sus lados es mayor al tercero
  if x+y>z and x+z>y and y+z>x:
#Fórmula para equilátero
    if x == y == z:
      print("El triángulo es equilátero")
#Fórmula para escaleno
    elif x != y != z:
      print("El triángulo es escaleno")
#Fórmula para isósceles
    else:
      print("El triángulo es isósceles")
#Si no cumple con las condiciones anteriores, no es un triángulo
  else:
    print("No es un triángulo")
else:
   print("No es un triángulo")