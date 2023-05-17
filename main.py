import random, os
def despliega_tablero(tablero):
  for renglon in tablero:
    print("\n---------------------------------")
    print("|", end="")
    for elemento in renglon:
      print(f'{elemento}'.center(10), end='')
      print("|", end="")
  print("\n---------------------------------")

def llena_escondida():
  '''Crea una matriz de 3x3 con elementos 'Negro' y 'Dorado' asignados al azar. La función devuelve la matriz creada'''
  matriz = []
  eleccion = ["dorado", "negro", "dorado", "negro", "dorado", "negro", "negro", "negro", "negro"]
  random.shuffle(eleccion)
  for i in range(3):
    lista = []
    for j in range(3):
      lista.append(eleccion.pop())
    matriz.append(lista)
  return matriz
    
def verifica_cambia(r,c, tab, esc):
  '''Verifica que r y c sean valores válidos para renglón y columna, si son validos, se destapa esa posición en el tablero y se despliega mensaje Muy bien si la posición es un dorado, de lo contrario el mensaje Perdiste. Si r o c son valores invalidos se indica con mensaje. La función devuelve un 0 o un 1, 0 en caso de error o Negro y 1 en caso de que se la posición contenga un dorado '''
  if (0 < r <= 3) and (0 < c <= 3):
    posicion = esc[r-1][c-1]
    tab[r-1][c-1] = esc[r-1][c-1]
    despliega_tablero(tab)
    if posicion == "dorado":
      return 1
    else:
      return 0
  else: 
    return 2

def limpia():
  '''Función que limpia a pantalla sin importar el sistema operativo de la máquina donde esté corriendo'''
  if os.name == 'nt':
    os.system('cls') #Windows
  else: #'posix'
    os.system('clear') #Mac/Linux

#Programa principal
def main():
  tablero=[['XXXXXX','XXXXXX','XXXXXX'],['XXXXXX','XXXXXX','XXXXXX'],['XXXXXX','XXXXXX','XXXXXX']]
  escondida=llena_escondida()
  destapados=0
  dorados=0
  sigue=1
  while sigue == 1 and destapados<3:
  #Realiza las acciones necesarias del juego
    despliega_tablero(tablero)
    r = int(input("Renglón: "))
    c = int(input("Columna: "))
    resultado = verifica_cambia(r,c,tablero,escondida)
    if resultado == 1:
      destapados += 1
      dorados += 1
      limpia()
      print('Muy bien')
    elif resultado == 0:
      sigue += 1
      limpia()
      despliega_tablero(tablero)
      print('Perdiste')
    else:
      limpia()
      print('Valores incorrectos')
  #Despliega el tablero en su estatus final
  if dorados==3:
    limpia()
    despliega_tablero(tablero)
    cantidad=random.randint(5,100)
    print(f'Ganas ${cantidad:.2f}')

main()
