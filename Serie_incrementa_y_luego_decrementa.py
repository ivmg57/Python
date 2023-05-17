#Diego Ivan Morales Gallardo
#Escribe un programa que lea un número N y muestre la siguiente lista de números:
#1, 2, ... N, N-1, N-2 ... 1

def incrementa_decrementa(n):
  for i in range(1,n):
    print(i,end=", ")
  for i in range(n,1,-1):
    print(i,end=", ")
  print(1)

def main():
  num = int(input(""))
  incrementa_decrementa(num)

main()