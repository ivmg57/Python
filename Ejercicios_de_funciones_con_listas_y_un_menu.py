#Diego Ivan Morales Gallardo

def crea_lista(n):
  '''Recibe n elementos y los ingresa a una lista
  la función devuelve la lista creada'''
  lista = []
  for i in range(n):
    dato = input(f"Dato {i}: ")
    lista.append(dato)
  return lista

def convierte_enteros(lista):
  for pos in range(len(lista)):
    lista[pos] = int(lista[pos])

def multiplos_3(lista):
  '''Regresa cuántos múltiplos de 3 tiene una lista'''
  cuantos = 0
  for elemento in lista:
    if (elemento % 3) == 0:
      cuantos += 1
  return cuantos

def sumar_pares(lista):
  '''Suma los elementos que son pares de la lista'''
  suma = 0
  for elemento in lista:
    if (elemento % 2) == 0:
      suma += elemento
  return suma

def duplica(lista):
  '''Duplica todos los datos de la lista'''
  for pos in range(len(lista)):
    lista[pos] = 2*(lista[pos])

def tam_palabras_3(lista):
  '''Recibe una lista de strings e imprime a pantalla las que tienen una longitud mayor a 6'''
  for elemento in lista:
    if len(elemento) > 6:
      print(elemento)

def empieza_con(lista,letra):
  nueva = []
  for elemento in lista:
    if elemento[0] == letra:
      nueva.append(elemento)
  return nueva
  
def main():
  print('Menu de funciones de listas')
  opc = '1'
  while opc != '0':
    print('1. Múltiplos de 3')
    print('2. Sumar los números pares')
    print('3. Duplica lista')
    print("4. Palabras de longitud mayor a 6")
    print("5. Palabras que empiezan con...")
    print('0. Salir')
    opc = input('\tOpción: ')
    print('---------------------------------')
    if opc == '1':
      num = int(input('Números en la lista: '))
      lista1 = crea_lista(num)
      convierte_enteros(lista1)
      resultado = multiplos_3(lista1)
      print(f'En tu lista:\n{lista1}\nTienes {resultado} múltiplos de 3')
      print('---------------------------------')
    elif opc =='2':
      num = int(input('Números en la lista: '))
      lista2 = crea_lista(num)
      #Poner lo que falta
      convierte_enteros(lista2)
      resultado = sumar_pares(lista2)
      print(f"En tu lista:\n{lista2}\nLa suma de pares es: {resultado}")
      print('---------------------------------')
    elif opc == '3':
      num = int(input('Números en la lista: '))
      # Incluir aquí la llamada a la función
      lista3 = crea_lista(num)
      convierte_enteros(lista3)
      print(lista3)
      duplica(lista3)
      print('Lista Modificada')
      print(lista3)
    elif opc == "4":
      num = int(input('Palabras en la lista: '))
      lista4 = crea_lista(num)
      tam_palabras_3(lista4)
    elif opc == "5":
      num = int(input('Palabras en la lista: '))
      lista5 = crea_lista(num)
      letra = input("Ingresa la letra: ")
      letra = letra[0]
      lista6 = empieza_con(lista5,letra)
      print(f"En tu lista:\n{lista5}\nLas palabras que empiezan con {letra} son: {lista6}")
    elif opc == '0':
      print('Terminando programa de listas...')
    else:
      print('Opción inválida')
    
main()