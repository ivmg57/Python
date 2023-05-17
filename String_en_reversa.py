#Diego Ivan Morales Gallardo
#Escribir un programa que lea un string y muestre como salida el string recibido escrito en reversa, comenzando con el último carácter y terminando con el primer carácter del string original, y completamente en mayúsculas.

def main():
  texto = input("Escribe el string: ")
  texto_en_mayusculas = texto.upper()
  texto_reversa = texto_en_mayusculas[::-1]
  print(texto_reversa)

main()