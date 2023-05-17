#Diego Ivan Morales Gallardo
#Crea un programa que pida al usuario dos cadenas de caracteres como entrada e imprima la cadena con la longitud mayor en la consola. Si las dos cadenas tienen la misma longitud, la función debe imprimir ambas cadenas una en cada renglón.

def mayor_longitud(texto1,texto2):
  if len(texto1) > len(texto2):
    print(f'\nEs más grande el primer texto:\n{texto1}')  
  elif len(texto2) > len(texto1):
    print(f'\nEs más grande el segundo texto:\n{texto2}')
  else:
    print(f'\nLos dos textos tienen la misma longitud:\n{texto1}\n{texto2}')

def main():
  cadena1 = input("Escribe el primer texto: ")
  cadena2 = input("Escribe el segundo texto: ")
  mayor_longitud(cadena1,cadena2)
  
main()