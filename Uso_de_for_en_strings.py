#Diego Ivan Morales Gallardo

def cuantas_vocales(texto):
  '''Recibe un string y nos devuelve el número de vocales que tiene'''
  num_vocales = 0
  for letra in texto:
    if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
      num_vocales += 1
  return num_vocales

def locura(texto):
  lista = list(texto)
  #Se necesita un recorrido por posición para hacer cambios en la lista
  for pos in range(len(texto)):
    if lista[pos] in 'aáAÁ':
      lista[pos] = '4'
    elif lista[pos] in 'eéEÉ':
      lista[pos] = '3'
    elif lista[pos] in 'lL':
      lista[pos] = '1'
    elif lista[pos] in 'oóOÓ':
      lista[pos] = '0'
  return ''.join(lista)

def locura_v2(texto):
  nuevo = ''
  for letra in texto:
    if letra in 'aAáÁ':
      nuevo += '4'
    elif letra in 'eEéÉ':
      nuevo += '3'  
    elif letra in 'lL':
      nuevo += '1' 
    elif letra in 'oOóÓ':
      nuevo += '0' 
    else:
      nuevo += letra
  return nuevo

def main():
  palabra = input('Ingresa un texto: ')
  vocales = cuantas_vocales(palabra)
  print(f'Tu texto tiene {vocales} vocales')
  print('LOCURA')
  print(locura(palabra))
  print(locura_v2(palabra))

main()