from datetime import datetime

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
