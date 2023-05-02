from getpass import getpass
def menu():
    opcao = 1
    valorTotal = 0
    while opcao != 0:
        print("| CÓDIGO ||     PRODUTO     || VALOR R$  |")
        print("|----------------------------------------|")
        print("|  100   || Cachorro Quente ||  R$ 1,70  |")
        print("|----------------------------------------|")
        print("|  101   ||  Bauru Simples  ||  R$ 2,30  |")
        print("|----------------------------------------|")
        print("|  102   ||  Bauru com Ovo  ||  R$ 2,60  |")
        print("|----------------------------------------|")
        print("|  103   ||  Hamburguer     ||  R$ 2,40  |")
        print("|----------------------------------------|")
        print("|  0     ||  Sair           ||           |")
        print("|----------------------------------------|")
        opcao = int(input("Escolha ou Opção: "))
        if opcao == 100:
            quant = int(input("informe a quantidade: "))
            total = quant * 1.70
            print("Voce escolhheu",quant,"Cachorros-Quentes, valor à pagar = R$",total)
            print("------------------------------------------------------------")
            valorTotal += total
        elif opcao == 101:
            quant = int(input("informe a quantidade: "))
            total = quant * 2.30
            print("Voce escolhheu", quant, "Baurus Simples, valor à pagar = R$", total)
            print("------------------------------------------------------------")
            valorTotal += total
        elif opcao == 102:
            quant = int(input("informe a quantidade: "))
            total = quant * 2.60
            print("Voce escolhheu", quant, "Baurus com Ovo, valor à pagar = R$", total)
            print("------------------------------------------------------------")
            valorTotal += total
        elif opcao == 103:
            quant = int(input("informe a quantidade: "))
            total = quant * 2.40
            print("Voce escolhheu", quant, "Hamburgueres, valor à pagar = R$", total)
            print("------------------------------------------------------------")
            valorTotal += total

    return valorTotal    

login = "ifpe"
senha = "1234"

num_tentativas = 3
tentativas = 0

while True:

    entrar_login = input("LOGIN: ")
    entrar_senha = getpass("Digite sua senha: ")
    #entrar_senha = input("SENHA: ")

    if entrar_login == login and entrar_senha == senha:
        print("Login efetuado com sucesso.")
        valorTotal = menu()
        break
    else:
        tentativas += 1
        print("Login ou senha incorreta.")
        if tentativas == num_tentativas:
            print("____Número de tentativas excedido.____")
            break
print("------------------------------------------------------------")
print(f"Valor total do pedido: R$ { valorTotal }")
print("Muito obrigado pela preferência!")
print("------------------------------------------------------------")