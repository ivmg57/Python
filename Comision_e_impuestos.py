#Diego Ivan Morales Gallardo
#Escribe un programa que nos indique el monto por comisión que le darán a un vendedor, tanto en pesos como en dólares.
#Para lo cual realiza dos funciones:
#Función que reciba como parámetro el monto de ventas (en pesos) de un vendedor durante el mes (flotante) y devuelva (uso de return) el monto que obtendrá de comisión. La comisión de un vendedor será lo correspondiente al del 7% de las ventas realizadas.
#Función que recibe como parámetro el monto de comisión de un vendedor e imprima a pantalla la cantidad que representa en dólares. 1 dólar son 21.50 pesos

#Escribe ahora una función main que haga lo siguiente:
#Recibe del usuario el monto total de ventas del vendedor en este mes.
#Usa las funciones implementadas para realizar lo siguiente:
#Desplegar un mensaje que indique el monto de la comisión del vendedor en pesos.
#Desplegar el equivalente en dólares.

def comision(monto_total):
  monto_comision = monto_total * .07
  return monto_comision

def montoDolares(monto_comision):
  monto_dolares = monto_comision / 21.50
  return monto_dolares

def main():
  monto = float(input("Escribe el monto total de ventas del vendedor en este mes: "))
  comision(monto)
  monto_comision = comision(monto)
  print(f"Monto de comisión en pesos: {monto_comision:.2f}")
  montoDolares(monto_comision)
  monto_dolares = montoDolares(monto_comision)
  print(f"Monto de comisión en dólares: {monto_dolares:.2f}")
  
main()