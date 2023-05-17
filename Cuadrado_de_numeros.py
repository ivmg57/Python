#Diego Ivan Morales Gallardo
#Desplegar lo siguiente con ciclos anidados
#12345
#12345
#12345...

def cuadrado(n):
  for i in range(n):
    for x in range(1,n+1):
      print(x, end= "")
    print()

def main():
  cuadrado(10)

main()