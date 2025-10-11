from constante import FORMAS_PAGAMENTO
from pessoas import Cliente, Vendedor
from carros import Carro
from vendas import Venda

def escolher_forma_pagamento():
    print("\nFormas de pagamento disponíveis:")
    for i, f in enumerate(FORMAS_PAGAMENTO):
        print(f"{i + 1}. {f}")
    try:
        opcao = int(input("Escolha uma opção: "))
        if 1 <= opcao <= len(FORMAS_PAGAMENTO):
            return FORMAS_PAGAMENTO[opcao - 1]
        else:
            print("Opção inválida. Será usada 'Pix' por padrão.")
            return "Pix"
    except ValueError:
        print("Erro: digite apenas números.")
        return "Pix"


def cadastrar_cliente(lista_clientes):
    while True:
        nome = input("Nome do cliente: ").strip()
        if nome:
            break
        print("Erro: o nome não pode ficar em branco.")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Erro: a idade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Erro: digite apenas números para a idade.")

    while True:
        cpf = input("CPF: ").strip()
        if cpf:
            break
        print("Erro: o CPF não pode ficar em branco.")

    while True:
        celular = input("Celular: ").strip()
        if celular:
            break
        print("Erro: o celular não pode ficar em branco.")

    cliente = Cliente(nome, idade, cpf, celular)
    lista_clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")


def cadastrar_vendedor(lista_vendedores):
    while True:
        nome = input("Nome do vendedor: ").strip()
        if nome:
            break
        print("Erro: o nome não pode ficar em branco.")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Erro: a idade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Erro: digite apenas números para a idade.")

    while True:
        cpf = input("CPF: ").strip()
        if cpf:
            break
        print("Erro: o CPF não pode ficar em branco.")

    while True:
        celular = input("Celular: ").strip()
        if celular:
            break
        print("Erro: o celular não pode ficar em branco.")

    while True:
        matricula = input("Matrícula: ").strip()
        if matricula:
            break
        print("Erro: a matrícula não pode ficar em branco.")

    while True:
        try:
            comissao = float(input("Comissão (%): "))
            if comissao < 0:
                print("Erro: a comissão não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Erro: digite apenas números para a comissão.")

    vendedor = Vendedor(nome, idade, cpf, celular, matricula, comissao)
    lista_vendedores.append(vendedor)
    print(f"Vendedor {nome} cadastrado com sucesso!")


def cadastrar_carro(lista_carros):
    while True:
        marca = input("Marca: ").strip()
        if marca:
            break
        print("Erro: a marca não pode ficar em branco.")

    while True:
        modelo = input("Modelo: ").strip()
        if modelo:
            break
        print("Erro: o modelo não pode ficar em branco.")

    while True:
        try:
            ano = int(input("Ano: "))
            if ano < 1886:
                print("Erro: o primeiro carro foi criado em 1886.")
            else:
                break
        except ValueError:
            print("Erro: digite apenas números para o ano.")

    while True:
        try:
            preco = float(input("Preço: "))
            if preco < 0:
                print("Erro: o preço não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Erro: digite apenas números para o preço.")

    carro = Carro(marca, modelo, ano, preco)
    lista_carros.append(carro)
    print(f"Carro {marca} {modelo} cadastrado com sucesso!")


def listar_clientes(lista_clientes):
    if not lista_clientes:
        print("Nenhum cliente cadastrado.")
        return
    for cliente in lista_clientes:
        cliente.exibir_dados()


def listar_carros(lista_carros):
    if not lista_carros:
        print("Nenhum carro cadastrado.")
        return
    for carro in lista_carros:
        carro.exibir_dados()


def realizar_venda(lista_clientes, lista_vendedores, lista_carros, lista_vendas):
    if not lista_clientes or not lista_vendedores or not lista_carros:
        print("Cadastre clientes, vendedores e carros antes de realizar a venda.")
        return

    try:
        for i, cliente in enumerate(lista_clientes):
            print(f"{i + 1}. {cliente.nome}")
        cliente_idx = int(input("Escolha o cliente: ")) - 1
        cliente = lista_clientes[cliente_idx]

        for i, vendedor in enumerate(lista_vendedores):
            print(f"{i + 1}. {vendedor.nome}")
        vendedor_idx = int(input("Escolha o vendedor: ")) - 1
        vendedor = lista_vendedores[vendedor_idx]

        carros_disponiveis = [carro for carro in lista_carros if not carro.vendido]
        if not carros_disponiveis:
            print("Nenhum carro disponível para venda.")
            return

        for i, carro in enumerate(carros_disponiveis):
            print(f"{i + 1}. {carro.marca} {carro.modelo} ({carro.ano}) - R${carro.preco:,.2f}")
        carro_idx = int(input("Escolha o carro: ")) - 1
        carro = carros_disponiveis[carro_idx]

        forma_pagamento = escolher_forma_pagamento()

        venda = Venda(cliente, vendedor, carro, forma_pagamento)
        if venda.realizar_venda():
            lista_vendas.append(venda)
    except (ValueError, IndexError):
        print("Erro: opção inválida.")


def listar_vendas(lista_vendas):
    if not lista_vendas:
        print("Nenhuma venda realizada.")
        return
    for venda in lista_vendas:
        venda.exibir_dados_venda()


def gerar_nota(lista_vendas):
    if not lista_vendas:
        print("Nenhuma venda realizada.")
        return
    for i, venda in enumerate(lista_vendas):
        print(f"{i + 1}. {venda._cliente.nome} comprou {venda._carro.modelo}")
    try:
        escolha = int(input("Escolha a venda para gerar nota fiscal: ")) - 1
        if 0 <= escolha < len(lista_vendas):
            lista_vendas[escolha].gerar_nota_fiscal_txt()
        else:
            print("Opção inválida.")
    except ValueError:
        print("Erro: digite apenas números.")


def exibir_menu():
    print("\n--- Menu da Concessionária ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Vendedor")
    print("3. Cadastrar Carro")
    print("4. Listar Clientes")
    print("5. Listar Carros")
    print("6. Realizar Venda")
    print("7. Listar Vendas")
    print("8. Gerar Nota Fiscal")
    print("9. Sair")
