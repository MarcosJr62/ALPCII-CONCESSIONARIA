class Pessoa():
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

class Vendedor(Pessoa):
    def __init__(self, nome, idade, cpf, celular, matricula, comissao):
        super().__init__(nome, idade, cpf, celular)
        self._matricula = matricula
        self._comissao = comissao

class Carro():
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

from datetime import datetime