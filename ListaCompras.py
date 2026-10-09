lista_compras = {} #esse cara tem que começar vazio, pois vou adicionando itens ao longo do programa

def menu():
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Listar itens")
    print("3. Marcar item como comprado")
    print("4. Remover item")
    print("5. Sair")

def ler_inteiro_positivo(mensagem):
    #vai pedir um numero inteiro > 0 ate o usuario acertar
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um número maior que 0")
        except ValueError:
            print("Digite um número inteiro válido! ")

def adicionar_item():
    produto = input("Qual produto você quer adicionar? ").strip().lower()

    if not produto: #caso digite um nome vazio
        print("O nome não pode ser vazio! ")
        return

    if produto in lista_compras:
        print('O produto já está no estoque')
        return
    
    else:
        quantidade = ler_inteiro_positivo("Quantidade: ")
        lista_compras[produto] = {"quantidade":quantidade, "comprado": False}
        print("Produto adicionado com sucesso! ")


def listar_itens():

    if not lista_compras:
        print("Estoque vazio")
        return
    
    else:
        print("\nSua lista:")
        for nome, dados in lista_compras.items(): #percorre nome (chave), dados (quantidade e comprado)
            marca = "x" if dados["comprado"] else " " #vai marcar x se comprado e espaco se nao
            print(f"[{marca}] {nome} - quantidade: {dados['quantidade']}")


def marcar_comprado():
    produto = str(input("Insira o produto que deseja marcar: ")).strip().lower()

    if produto not in lista_compras:
        print("Esse produto não está na lista! ")
    elif lista_compras[produto]["comprado"]:
        print("Esse produto já estava marcado como comprado! ")
    else:
        lista_compras[produto]["comprado"] = True
        print("Produto marcado como comprado! ")

def remover_item():
    produto = str(input("Nome do produto: ")).strip().lower()

    if produto not in lista_compras:
        print("Esse produto não existe no estoque")
    else:
        del lista_compras[produto]
        print('Produto removido com sucesso! ')

def main(): 
    while(True):
        menu()
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            adicionar_item()
        elif opcao == 2:
            listar_itens()
        elif opcao == 3:
            marcar_comprado()
        elif opcao == 4:
            remover_item()
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha um número de 1 até 5.")


main()