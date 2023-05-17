#Diego Ivan Morales Gallardo
#Escribe un programa que lea 2 valores a y b y que muestre en la pantalla pares de números en donde el valor de a se incrementa de 2 en 2 y el valor de b se decrementa de 1 en 1 hasta llegar a 1. El ciclo se va a detener cuando b llegue a 1.
def dos_contadores(valor_a,valor_b):
  for i in range(valor_b,0,-1):
    print(valor_a,i)
    valor_a += 2

#Alternativa:
#while valor_b >= 1:
#print(valor_a,valor_b)
#valor_a += 2
#valor_b -= 1

def main():
  a = int(input("Valor de A: "))
  b = int(input("Valor de B: "))
  dos_contadores(a,b)
main()