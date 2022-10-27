T = int(input())

for i in range(T):
  valor1,valor2 = map(int,input().split())
  R = (valor1 / valor2)
  T = (valor1 % valor2)
  print(int(R)+int(T))