from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.____cilindrada
    
    @cilindrada.setter
    def cilindrada(self, valor):
        if not valor:
            raise ValueError("Valor inválido")
        self.____cilindrada = valor

    def calculo_aluguel_moto(self, dias, cilindradas):
        aluguel = super().calculo_aluguel(dias)
        if cilindradas > 200:      
            adicional_cc = (aluguel/100) * 10
            resultado = aluguel + adicional_cc
        else:
            resultado = aluguel
        return resultado
