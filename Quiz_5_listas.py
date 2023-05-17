#Diego Ivan Morales Gallardo

def crea_lista(n):
  lista = []
  for i in range(1,n+1):
    dato = input(f"Elemento {i}: ")
    lista.append(dato)
  return lista

def intercala(lista1,lista2):
  lista3 = []
  for pos in range(len(lista1)):
    lista3.append(int(lista1[pos]))
    lista3.append(int(lista2[pos]))
  return lista3

def main():
  n = int(input("Número de elementos para tus listas: "))
  print("INGRESO DE DATOS DE LISTA 1")
  lista1 = crea_lista(n)
  print("INGRESO DE DATOS DE LISTA 2")
  lista2 = crea_lista(n)
  print("La lista intercalada:")
  lista_intercalada = intercala(lista1,lista2)
  print(lista_intercalada)
  
main()