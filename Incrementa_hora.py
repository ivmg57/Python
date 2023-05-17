#Diego Ivan Morales Gallardo
#Escribe un programa en que sea útil para calcular la siguiente hora después de pasar un minuto.
#Pide al usuario la hora inicial, después lee una clave (s – siguiente, t – terminar).
#Si el usuario teclea s, muestra la hora después de sumar 1 minuto y vuelve a leer la clave.
#Si el usuario teclea t, termina el programa.
#Por ejemplo si la hora es:             Después de sumarle un minuto será:
#10:10                                             10:11
#05:59                                             06:00
#23:59                                             00:00

def incrementa_hora(hora_inicial,minuto_inicial):
  clave = input("Ingresa la clave (s/t): ")
  while clave != "t":
    if clave == "s":
      minuto_inicial += 1
      if minuto_inicial == 60:
        hora_inicial += 1
        minuto_inicial = 0
        if hora_inicial == 24:
          hora_inicial = 0
    else:
      print("Clave incorrecta")
    print(str(hora_inicial).zfill(2) + ":" + str(minuto_inicial).zfill(2))
    clave = input("Ingresa la clave (s/t): ")

def main():
  hora = int(input("Ingresa hora inicial: "))
  minutos = int(input("Ingresa minutos iniciales: "))
  incrementa_hora(hora,minutos)

main()