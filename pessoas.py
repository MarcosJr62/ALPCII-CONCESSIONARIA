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
    def __init__(self, nome, idade, cpf, celular, ):
        super().__init__(nome, idade, cpf, celular)

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
