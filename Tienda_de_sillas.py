#Diego Ivan Morales Gallardo

def precio_sd(tipodesilla,cantidaddesillas):
  if tipodesilla == 'B':
    total = cantidaddesillas * 700
  elif tipodesilla == 'E':
    total = cantidaddesillas * 900
  elif tipodesilla == 'L':
    total = cantidaddesillas * 1500
  else:
    print("Respuesta incorrecta")
  return total
  
def descuentos_mayoreo(totalsindescuento,tipocliente):
  if tipocliente == 'F':
    totalcondescuento2 = 20
  elif tipocliente == 'N':
    totalcondescuento1 = totalsindescuento
  else:
    print("Respuesta incorrecta")
  if totalcondescuento1 >= 10000 and < 20000:
    totalcondescuento2 = 10
  elif totalcondescuento1 >= 20000:
    totalcondescuento2 = 15
  return totalcondescuento2
  
  
def main():
  tipo_de_silla = input(f"Indica el tipo de silla (B,E,L): ")
  tipo_de_cliente = input(f"Indica el tipo de cliente (N,F): ")
  cantidad_de_sillas = int(input(f"Indica el número de sillas: "))
  total_sd = precio_sd(tipo_de_silla,cantidad_de_sillas)
  print(f"El precio sin descuento es: {total_sd}")
  total_cd = descuentos_mayoreo(total_sd,tipo_de_cliente)
  print (f"El precio con descuento es: {total_cd}")
  
main()