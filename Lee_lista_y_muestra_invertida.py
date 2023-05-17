#Diego Ivan Morales Gallardo

lista = []
cantidad_de_elementos = int(input())
cont = 0
if cantidad_de_elementos > 0:
  while cont < cantidad_de_elementos:
    num = input()
    lista.append(num)
    cont += 1
for pos in range(len(lista)):
  pos1 = -1-pos
  lugar = lista[pos1]
  print(f"lista[{pos1}] = {lugar}")

#for pos in range(-1,-len(lista)-1,-1):
#print(f"lista[{pos}] = {lista[pos]}")

#num = int(input("Cuantos elemetos para la lista: "))
#while num <= 0:
#print("Valor incorrecto")
#num = int(input("Cuantos elementos para la lista: "))
#lista_uno = crea_lista(num)  
#imprime_inversa(lista_uno)