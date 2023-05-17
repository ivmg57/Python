#Diego Ivan Morales Gallardo
#Listas anidadas y matrices
def crea_matriz(ren,col):
#Ren es el número de renglones que va a tener la matriz
  matriz = []
  for i in range(ren):
    lista = []
    for j in range(col):
      dato = int(input('Dato: '))
      lista.append(dato)
    matriz.append(lista)
  return matriz

def despliega_matriz(matriz):
  for renglon in matriz:
    for elemento in renglon:
     print(f'{elemento:3d}', end=' ')
    print()

def matriz_identidad(n):
  matriz = []
  for i in range(n):
    lista = []
    for j in range(n):
      if i == j:
        lista.append(1)
      else:
        lista.append(0)
    matriz.append(lista)
  return matriz

def cuenta_pares(matriz):
  num_pares = 0
  for renglon in matriz:
    for elemento in renglon:
      if (elemento%2) == 0:
        num_pares += 1
  return num_pares

def cambia_negativos(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] < 0:
        matriz[i][j] = 0

def main():
  renglones = int(input('Número de renglones: '))
  columnas = int(input('Número de columnas: '))
  print()
  m1 = crea_matriz(renglones,columnas)
  print()
  despliega_matriz(m1)
  cambia_negativos(m1)
  print()
  print("Después de cambiar negativos...")
  print()
  despliega_matriz(m1)
  #pares = cuenta_pares(m1)
  print()
  #print(f'Tu matriz tiene {pares} pares')
  #num = int(input("Número de renglones y columnas: "))
  #m2 = matriz_identidad(num)
  #despliega_matriz(m2)

main()