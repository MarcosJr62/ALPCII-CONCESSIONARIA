from funcoes import * 

def main():
    lista_clientes = []
    lista_vendedores = []
    lista_carros = []
    lista_vendas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente(lista_clientes)
        elif opcao == "2":
            cadastrar_vendedor(lista_vendedores)
        elif opcao == "3":
            cadastrar_carro(lista_carros)
        elif opcao == "4":
            listar_clientes(lista_clientes)
        elif opcao == "5":
            listar_carros(lista_carros)
        elif opcao == "6":
            realizar_venda(lista_clientes, lista_vendedores, lista_carros, lista_vendas)
        elif opcao == "7":
            listar_vendas(lista_vendas)
        elif opcao == "8":
            gerar_nota(lista_vendas)
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
