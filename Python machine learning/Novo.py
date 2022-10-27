n = int(input())

while(n > 0):
    valor = input().split()
    a = valor[0]
    b = valor[1]
    c = a[-len(b):]
    if len(b) > len(a):
      print("nao encaixa") 
      n = n -1
      continue
    if  c == b :
        print("encaixa")
    else:
        print("nao encaixa")
    n = n -1