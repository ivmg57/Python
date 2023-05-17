#Diego Ivan Morales Gallardo
#Programa que indica el número de segundos que se tardan 2 procesos
#Definir la función y sus parámetros
def equivalente(horas, minutos, segundos):
#Fórmula para convertir horas y minutos a segundos y sumarlos
  totales = horas*3600 + minutos*60 + segundos
#Regresar resultado
  return totales
#Función principal:
def main():
#Pedir las horas, minutos y segundos de los dos procesos y asignarlos a una variable
  print("PROCESO 1")
  h1 = int(input("\tHoras: "))
  m1 = int(input("\tMinutos: "))
  s1 = int(input("\tSegundos: "))
  print("PROCESO 2")
  h2 = int(input("\tHoras: "))
  m2 = int(input("\tMinutos: "))
  s2 = int(input("\tSegundos: "))
#Asignar los resultados que regresa la funcion equivalente a una variable
#IMPORTANTE: asignar los argumentos en el orden que están los parámetros
  tiempo_p1 = equivalente(h1,m1,s1)
  tiempo_p2 = equivalente(h2,m2,s2)
#Imprimir los resultados
  print(f"Tiempo en segundos del proceso 1: {tiempo_p1}")
  print(f"Tiempo en segundos del proceso 2: {tiempo_p2}")

#Llamar a main()
main()