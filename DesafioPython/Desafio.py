menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """



saldo = 0
limite =500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  op = input(menu)
  if op == "d": 
    valor = float(input("informe o valor do deposito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Deposito : R$ {valor:.2f}\n"
    else:
        print("Operaçao falho! O valor informado é invalido.")

  elif op == "s":
      valor = float(input("Informe o valor do saque: "))

      excedeu_saldo = valor > saldo
      
      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= LIMITE_SAQUES

      if excedeu_saldo:
          print("Operação falho! Voce nao tem saldo suficiente.")
      elif excedeu_limite:
          print("operação falho! O vlaor do saque exece o limite.")
      elif excedeu_saques:
          print("operação falho! Numero maixmo de saque excedido.")

      elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1
      else:
          print("Operaçao falhou! O valor informado é invalido.")

  elif op =="e":
      print("===========Extrato===========")
      print("Não foram realziada movimentações." if not extrato else extrato)
      print(f"\n Saldo: R$ {saldo:.2f} ")
      print("==============================")

  elif op == "q":
      break

  else:
      print("Operaçao invalida, por favor selecione novamente a operação	desejada.")