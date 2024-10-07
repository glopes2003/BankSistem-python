menu = """
<<< Bem-Vindo(a) ao Sistema Bancário Python >>>

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=> Escolha a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input( menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação cancelada. O valor informado é inválido!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n=====================================================")
            print("Operação cancelada. Você não tem saldo suficiente :(")
            print("=====================================================")

        elif excedeu_limite:
            print("\n=============================================================================")
            print("Operação cancelada. O valor do saque excede o limite de 500 reais por saque.")
            print("=============================================================================")

        elif excedeu_saques:
            print("\n==============================================================")
            print("Operação cancelada. Número máximo de saques diários excedido.")
            print("==============================================================")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\n==================================================")
            print("Operação cancelada. O valor informado é inválido!")
            print("===================================================")

    elif opcao == "3":
        print("\n<<<<< EXTRATO >>>>>")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("========================")
        print(f"Saldo: R$ {saldo:.2f}")
        print("========================")

    elif opcao == "4":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")