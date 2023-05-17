#Diego Ivan Morales Gallardo
#Escribe un programa que lea un string y muestre fragmentos de este
#En la primera línea imprimir la longitud del string recibido.
#En la segunda línea imprimir solo el primer carácter del string recibido.
#En la tercera línea imprimir solo el último carácter del string recibido.
#En la cuarta línea imprimir solo los caracteres con índice impar dentro del string.

def main():
  texto = input('Escribe el string: ')
  longitud = len(texto)
  print(f'Longitud del string: {longitud}')
  primer_caracter = texto[0]
  print(f'Primer caracter: {primer_caracter}')
  ultimo_caracter = texto[-1]
  print(f'Último caracter: {ultimo_caracter}')
  caracteres_impares = texto[::2]
  print(f'Caracteres impares: {caracteres_impares}')

main()