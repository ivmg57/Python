#Diego Ivan Morales Gallardo
def leer_archivo(nombre):
  matriz = []
  try:
    archivo = open(nombre,'r')
  except IOError:
    print('No se puede abrir el archivo')
  else:
    for linea in archivo:
      linea = linea.rstrip()
      lista = linea.split(',')
      matriz.append(lista)
    archivo.close()
  return matriz  

def main():
  nombre_archivo = input('Nombre del archivo: ')
  m1 = leer_archivo(nombre_archivo)
  print(m1)

main()