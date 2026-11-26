# Contas fixas
contas = {
    "12345": {"senha": "123456", "saldo": 1000, "historico": []},
    "67890": {"senha": "654321", "saldo": 500, "historico": []}
}

# Cédulas disponíveis
cedulas = [100, 50, 20, 10]


def formatar_moeda(valor):
    return f"R$ {valor:.2f}"


def login():
    print("\n===== LOGIN =====")

    while True:
        numero = input("Número da conta: ")
        senha = input("Senha: ")

        if numero in contas and contas[numero]["senha"] == senha:
            print("\nLogin realizado com sucesso!")
            return numero

        print("Conta ou senha inválida. Tente novamente.")


def consultar_saldo(conta):
    print(f"\nSaldo disponível: {formatar_moeda(conta['saldo'])}")


def depositar(conta):
    print("\n===== DEPÓSITO =====")

    try:
        valor = int(input("Valor do depósito: R$ "))

        if valor <= 0:
            print("Informe um valor positivo.")
            return

        conta["saldo"] += valor
        conta["historico"].append(f"Depósito: {formatar_moeda(valor)}")

        print("Depósito realizado com sucesso!")

    except ValueError:
        print("Informe um valor inteiro válido.")


def calcular_cedulas(valor):
    resultado = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        valor = valor % cedula

        if quantidade > 0:
            resultado[cedula] = quantidade

    return resultado, valor


def sacar(conta):
    print("\n===== SAQUE =====")

    try:
        valor = int(input("Valor do saque: R$ "))

        if valor <= 0:
            print("Informe um valor positivo.")
            return

        if valor > conta["saldo"]:
            print("Saque negado: saldo insuficiente.")
            return

        # Calcula a quantidade de cada cédula
        notas, resto = calcular_cedulas(valor)

        if resto != 0:
            print("Saque recusado: valor incompatível com as cédulas disponíveis.")
            return

        # Atualiza o saldo
        conta["saldo"] -= valor

        # Registra a movimentação
        conta["historico"].append(f"Saque: {formatar_moeda(valor)}")

        print("\nSaque realizado com sucesso!")
        print("Cédulas entregues:")

        for cedula, quantidade in notas.items():
            print(f"{quantidade} nota(s) de R$ {cedula}")

    except ValueError:
        print("Informe um valor inteiro válido.")


def extrato(conta):
    print("\n===== EXTRATO =====")

    if not conta["historico"]:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in conta["historico"]:
            print(movimentacao)

    print(f"\nSaldo atual: {formatar_moeda(conta['saldo'])}")


def menu():
    numero = login()
    conta = contas[numero]

    while True:
        print("\n===== CAIXA ELETRÔNICO =====")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Extrato")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            consultar_saldo(conta)

        elif opcao == "2":
            depositar(conta)

        elif opcao == "3":
            sacar(conta)

        elif opcao == "4":
            extrato(conta)

        elif opcao == "5":
            print("\nObrigado por utilizar nosso caixa eletrônico!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()