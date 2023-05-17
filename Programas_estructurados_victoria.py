#Diego Ivan Morales Gallardo
#Aplicacion para Victoria, cálculo de descuentos y cómo pagar
import random,math

def billetes(cantidad):
#Despliega a pantalla la cantidad de billetes y monedas de cada denominación que se requiere para pagar una determinada cantidad
  bill200 = cantidad // 200
  cantidad = cantidad % 200
  bill100 = cantidad // 100
  cantidad = cantidad % 100
  bill50 = cantidad // 50
  cantidad = cantidad % 50
  bill20 = cantidad // 20
  cantidad = cantidad % 20
  mon5 = cantidad // 5
  cantidad = cantidad % 5
  print(f"{bill200:.0f} de 200")
  print(f"{bill100:.0f} de 100")
  print(f"{bill50:.0f} de 50")
  print(f"{bill20:.0f} de 20")
  print(f"{mon5:.0f} de 5")
  print(f"{math.ceil(cantidad)} de 1")

def monto_total():
  total = 0
  cont = 1
  while cont <= 5:
    precio = int(input(f"Precio {cont}: "))
    total += precio
    cont += 1
  return total
  
def calculo_descuento(sin_descuento):
  porcentaje = random.randint(5,40)
  print(f"\nDescuento obtenido: {porcentaje}%\n")
  con_descuento = sin_descuento * (1-porcentaje/100)
  return con_descuento

def conversion(total_pesos):
  total_euros = total_pesos / 21
  return total_euros

def main():
  total_sindescuento = monto_total()
  total_condescuento = calculo_descuento(total_sindescuento)
  total_euros = conversion(total_condescuento)
  print(f"Resultados:\n")
  print(f"El precio sin descuento: ${total_sindescuento}")
  print(f"El precio con descuento: ${total_condescuento:.2f}")
  print(f"El precio en euros: {total_euros:.2f}\n")
  billetes(total_condescuento)

main()