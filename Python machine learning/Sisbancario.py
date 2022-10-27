def Deposito(show):
    print("Qual o valor do deposito? ")
    valor = int(input())

def Saque(show):
  return
def Extrato(show):
  return

def Menu ():

  show=[]

  while True:
    print("1. Deposito")
    print("2. Saque")
    print("3. Extrato")   
    print("4. Sair do sistema")
    op = int(input("> "))

    if op == 1:
      Deposito(show)
    elif op == 2:
      Saque(show)
    elif op == 3:
      Extrato(show)    
    elif op == 4:  
      print("Saindo do sistema \n")
      break
    else:
      print("Opção invalida. Escolha outra opção da lista. \n")
Menu()