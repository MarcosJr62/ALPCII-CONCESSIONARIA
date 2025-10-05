class Pessoa():
    def __init__(self, nome,idade,cpf,celular):
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
    def email(self):
        return self._email

    @email.setter
    def cpf(self, novo_cpf):    
            self._cpf = novo_cpf

    @property
    def celular(self):
          return self._celular
    
    @celular.setter
    def celular(self, novo_celular):
        self._celular = novo_celular

    def exibir_dados(self):
        print("Exibindo dados da pessoa:")
        print(f'Nome: {self._nome}')
        print(f'Idade: {self._idade}')
        print(f'E-mail: {self._email}')
        print(f'Celular: {self._celular}')   

class Carro():
     def __init__(self, modelo, ano, preco, marca):
          self._modelo = modelo
          self._ano = ano
          self._preco = preco
          self._marca = marca