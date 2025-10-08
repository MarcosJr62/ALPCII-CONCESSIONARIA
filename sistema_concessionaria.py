from datetime import datetime

#------------------- CLASSES -------------------

class Pessoa:
    def __init__(self, nome, idade, cpf, celular):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._celular = celular

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade não pode ser negativa.")
        else:
            self._idade = nova_idade

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, novo_celular):
        self._celular = novo_celular

    def exibir_dados(self):
        print("\n--- Dados da Pessoa ---")
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"CPF: {self._cpf}")
        print(f"Celular: {self._celular}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, celular, forma_pagamento):
        super().__init__(nome, idade, cpf, celular)
        self._forma_pagamento = forma_pagamento

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

class Vendedor(Pessoa):
    def __init__(self, nome, idade, cpf, celular, matricula, comissao):
        super().__init__(nome, idade, cpf, celular)
        self._matricula = matricula
        self._comissao = comissao

    @property
    def matricula(self):
        return self._matricula

    @property
    def comissao(self):
        return self._comissao

class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._preco = preco
        self._vendido = False

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nova_marca):
        self._marca = nova_marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self._modelo = novo_modelo

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        if novo_ano < 1886:
            print("Ano inválido. O primeiro carro foi criado em 1886.")
        else:
            self._ano = novo_ano

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            print("Preço não pode ser negativo.")
        else:
            self._preco = novo_preco

    @property
    def vendido(self):
        return self._vendido

    @vendido.setter
    def vendido(self, status):
        self._vendido = status

    def exibir_dados(self):
        print("\n--- Dados do Carro ---")
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Ano: {self._ano}")
        print(f"Preço: R${self._preco:,.2f}")
        print(f"Status: {'Vendido' if self._vendido else 'Disponível'}")

class Venda:
    def __init__(self, cliente, vendedor, carro, forma_pagamento):
        self._cliente = cliente
        self._vendedor = vendedor
        self._carro = carro
        self._data = datetime.now()
        self._valor_total = carro.preco
        self._forma_pagamento = forma_pagamento

    def realizar_venda(self):
        if self._carro.vendido:
            print("Erro: Esse carro já foi vendido!")
            return False
        else:
            self._carro.vendido = True
            print("Venda realizada com sucesso!")
            return True

    def exibir_dados_venda(self):
        print("\n--- Dados da Venda ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Vendedor: {self._vendedor.nome}")
        print(f"Carro: {self._carro.marca} {self._carro.modelo} ({self._carro.ano})")
        print(f"Valor Total: R${self._valor_total:,.2f}")
        print(f"Forma de Pagamento: {self._forma_pagamento}")
        print(f"Data da Venda: {self._data.strftime('%d/%m/%Y %H:%M:%S')}")

    def gerar_nota_fiscal_txt(self):
        nome_arquivo = f"nota_{self._cliente.nome}_{self._carro.modelo}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("--- NOTA FISCAL ---\n\n")
            arquivo.write(f"Cliente: {self._cliente.nome}\n")
            arquivo.write(f"Vendedor: {self._vendedor.nome}\n")
            arquivo.write(f"Carro: {self._carro.marca} {self._carro.modelo} ({self._carro.ano})\n")
            arquivo.write(f"Valor Total: R${self._valor_total:,.2f}\n")
            arquivo.write(f"Forma de Pagamento: {self._forma_pagamento}\n")
            arquivo.write(f"Data da Venda: {self._data.strftime('%d/%m/%Y %H:%M:%S')}\n")
            arquivo.write("\nObrigado por comprar conosco!")
        print(f"Nota fiscal gerada: {nome_arquivo}")

#------------------- FUNÇÕES -------------------

def cadastrar_cliente(lista_clientes):
    nome = input("Nome do cliente: ").strip()
    idade = int(input("Idade: "))
    cpf = input("CPF: ").strip()
    celular = input("Celular: ").strip()
    forma_pagamento = input("Forma de pagamento: ").strip()

    cliente = Cliente(nome, idade, cpf, celular, forma_pagamento)
    lista_clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def cadastrar_vendedor(lista_vendedores):
    nome = input("Nome do vendedor: ").strip()
    idade = int(input("Idade: "))
    cpf = input("CPF: ").strip()
    celular = input("Celular: ").strip()
    matricula = input("Matrícula: ").strip()
    comissao = float(input("Comissão (%): "))

    vendedor = Vendedor(nome, idade, cpf, celular, matricula, comissao)
    lista_vendedores.append(vendedor)
    print(f"Vendedor {nome} cadastrado com sucesso!")

def cadastrar_carro(lista_carros):
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    ano = int(input("Ano: "))
    preco = float(input("Preço: "))
    
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

    for i, cliente in enumerate(lista_clientes):
        print(f"{i+1}. {cliente.nome}")
    cliente_idx = int(input("Escolha o cliente: ")) - 1
    cliente = lista_clientes[cliente_idx]

    for i, vendedor in enumerate(lista_vendedores):
        print(f"{i+1}. {vendedor.nome}")
    vendedor_idx = int(input("Escolha o vendedor: ")) - 1
    vendedor = lista_vendedores[vendedor_idx]

    carros_disponiveis = [carro for carro in lista_carros if not carro.vendido]
    if not carros_disponiveis:
        print("Nenhum carro disponível para venda.")
        return
    for i, carro in enumerate(carros_disponiveis):
        print(f"{i+1}. {carro.marca} {carro.modelo} ({carro.ano}) - R${carro.preco:,.2f}")
    carro_idx = int(input("Escolha o carro: ")) - 1
    carro = carros_disponiveis[carro_idx]

    forma_pagamento = input("Forma de pagamento: ").strip()
    venda = Venda(cliente, vendedor, carro, forma_pagamento)
    if venda.realizar_venda():
        lista_vendas.append(venda)

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
        print(f"{i+1}. {venda._cliente.nome} comprou {venda._carro.modelo}")
    escolha = int(input("Escolha a venda para gerar nota fiscal: ")) - 1
    if 0 <= escolha < len(lista_vendas):
        lista_vendas[escolha].gerar_nota_fiscal_txt()
    else:
        print("Opção inválida.")

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

#------------------- MAIN -------------------

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