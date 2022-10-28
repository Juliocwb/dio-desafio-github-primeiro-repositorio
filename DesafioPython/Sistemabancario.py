import textwrap

def menu():
    menu = """\n
    ===============MENU===============
    [d]\tDepoistar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Conta
    [nu]\tNovo usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
      saldo += valor
      extrato += f"Deposito : R$ {valor:.2f}\n"
      print("Deposito realizado com sucesso!")
    else:
      print("Operaçao falho! O valor informado é invalido.")
    return saldo, extrato

def sacar(*,saldo,valor, extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("Operaçao falhou! voce nao tem saldo suficiente.")

    elif excedeu_limite:
        print("Operaçao falhou! O valor do saque excdeu o limite.")

    elif excedeu_saques:
        print("Operaçao falhou! Numero maixmo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operaçao falhou! O valor informado é invalido.")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("===========Extrato===========")
    print("Não foram realziada movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f} ")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somento Numero):  ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("ja existe usuario com esse CPF!")
        return
    nome = input("Informe o nome completo")
    data_nascimento = input("Informe a data de nascimento ( dd-nmm-aaaa): ")
    endereco = input("Informe o endereco (logradourom nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario Criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do Usuario")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia":agencia, "numero_conta":numero_conta, "usuarios":usuario}
    print("Usuario nao encontrado, Fluxo de criação de cotna encerrado!")

def listar_contas(contas):
  for conta in contas:
      linha = f"""\
          Agencia:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
            itular:\t{conta['usuario']['nome']}
        """
      print("="* 100)
      print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 5000
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []

    while True:
        op = menu()

        if op == "d":
          valor = float(input("Informe o valor do deposito: "))

          saldo, extrato = depositar(saldo,valor,extrato)
        elif op =="s":
            valor= float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                  sald0=saldo,
                  valor=valor,
                  extrato=extrato,
                  limite=limite,
                  numero_saques=numero_saques,
                  limite_saque=LIMITE_SAQUES
            )
        elif op == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif op =="nu":
            criar_usuario(usuario)

        elif op == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuario)

            if conta:
                contas.append(conta)
        elif op == "lc":
            listar_contas(contas)

        elif op == "q":
            break

main()