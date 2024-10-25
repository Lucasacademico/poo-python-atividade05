from classes.veiculo import Veiculo
from classes.carro import Carro
from classes.moto import Moto


# Cria uma instância de Veiculo
veiculo_generico = Veiculo(nome="Veículo Genérico", ano=2020, valor_diario=100)

# Testa o cálculo de aluguel para Veiculo com e sem cupom de desconto
print("Aluguel sem cupom:", veiculo_generico.calculo_aluguel(dias=5))  # Esperado: 500
print("Aluguel com cupom de 20%:", veiculo_generico.calculo_aluguel(dias=5, cupom=20))  # Esperado: 400

# Cria uma instância de Carro
carro = Carro(nome="Sedan", ano=2021, valor_diario=150, tipo_combustivel="Gasolina")

# Testa o cálculo de aluguel para Carro com e sem cupom
print("Aluguel de carro sem desconto:", carro.calculo_aluguel(dias=3))  # Esperado: 450
print("Aluguel de carro com desconto de 15%:", carro.desconto(dias=3, porcentagem=15))  # Esperado: 382.5

# Testa o desconto adicional para aluguéis de Carro superiores a 7 dias
print("Desconto para 10 dias de aluguel de carro com 10%:", carro.desconto_dias(dias=10, porcentagem=10))  # Aplicação do desconto adicional

# Cria uma instância de Moto
moto = Moto(nome="Moto Esportiva", ano=2022, valor_diario=80, cilindrada=250)

# Testa o cálculo de aluguel para Moto, considerando o adicional para cilindradas > 200
print("Aluguel de moto com cilindrada > 200:", moto.calculo_aluguel_moto(dias=5, cilindradas=150))  # Esperado: aluguel com adicional de 10%

# Testa o cálculo de aluguel para Moto com cilindrada <= 200
moto_pequena = Moto(nome="Moto Básica", ano=2022, valor_diario=80, cilindrada=150)
print("Aluguel de moto com cilindrada <= 200:", moto_pequena.calculo_aluguel_moto(dias=5, cilindradas=250))  # Esperado: aluguel sem adicional

# Verifica a contagem de veículos criados
print("Quantidade total de veículos:", Veiculo.quantidade_veiculo)  # Deve exibir o número total de instâncias criadas

print("Quantidade total de veículos:", Veiculo.obter_quantidade_veiculos())