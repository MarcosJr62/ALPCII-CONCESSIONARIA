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
