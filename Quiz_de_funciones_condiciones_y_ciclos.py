#Diego Ivan Morales Gallardo

import random

def aleatorio(num_vec_resta,lim_sup):
  cont = 1
  while cont <= num_vec_resta:
    primer_numero = random.randint(50,100)
    segundo_numero = random.randint(1,lim_sup)
    resultado = primer_numero - segundo_numero
    print(f"{primer_numero} - {segundo_numero} = {resultado}")
    cont += 1
  
def main():
  num_restas = int(input("Número de restas: "))
  if num_restas > 0:
    lim_sus = int(input("Límite para el sustraendo: "))
    if lim_sus > 0:
      aleatorio(num_restas,lim_sus)
    else: 
      print("Programa terminado!")
  else: 
    print("Programa terminado!")

main()