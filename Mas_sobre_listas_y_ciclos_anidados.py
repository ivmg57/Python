#Diego Ivan Morales Gallardo
#Patrones de números

def triangulo_a(n):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j, end=' ')
    print()

def triangulo_b(n):
  for i in range(n,0,-1):
    for j in range(1,i+1):
      print(j, end=' ')
    print(' '*((n-i)*2), end=' ')
    print()

def triangulo_c(n):
  for i in range(1,n+1):
    print(' '*((n-i)*2), end=' ')
    for j in range(i,0,-1):
      print(j, end=' ')
    print()

def triangulo_d(n):
  for i in range(n,0,-1):
    print(' '*((n-i)*2), end=' ')
    for j in range(1,i+1):
      print(j, end=' ')
    print()

def main():
  triangulo_a(6)
  print()
  triangulo_b(6)
  print()
  triangulo_c(6)
  print()
  triangulo_d(6)

main()