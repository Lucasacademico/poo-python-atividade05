# Sistema de Aluguel de Veículos

Este projeto implementa um sistema de aluguel de veículos que utiliza conceitos de Programação Orientada a Objetos (POO) em Python, incluindo herança, encapsulamento, métodos de classe e métodos de desconto. O sistema permite calcular o valor do aluguel para diferentes tipos de veículos, aplicar descontos e adicionar taxas adicionais dependendo das características de cada veículo.

## Estrutura do Projeto

O sistema é composto pelas seguintes classes:

- **Veiculo**: Classe base que contém atributos e métodos comuns a todos os veículos, como `nome`, `ano`, `valor_diario` e o cálculo básico do aluguel.
- **Carro**: Subclasse de `Veiculo` que adiciona o atributo `tipo_combustivel` e um método de desconto adicional caso o aluguel seja por mais de 7 dias.
- **Moto**: Subclasse de `Veiculo` que adiciona o atributo `cilindrada` e inclui um cálculo adicional para aluguel de motos com mais de 200 cilindradas.

## Funcionalidades

### Métodos e Atributos

- **Atributo de Classe `quantidade_veiculo`**: Mantém a contagem de veículos criados no sistema.
- **Métodos Getters e Setters**: Para os atributos `nome`, `ano` e `valor_diario`, garantindo validações ao definir esses valores.
- **Método `calculo_aluguel`**: Calcula o valor do aluguel com base no número de dias e na taxa diária.
- **Método `desconto`**: Aplica um desconto ao valor do aluguel, de acordo com uma porcentagem especificada.
- **Método `desconto_dias` (Carro)**: Calcula o valor do aluguel com um desconto adicional para períodos superiores a 7 dias.
- **Método `calculo_aluguel_moto` (Moto)**: Adiciona uma taxa extra ao aluguel para motos com cilindradas superiores a 200.

## Pré-requisitos

- **Python 3.8+**

## Estrutura de Arquivos

```plaintext
|-- projeto-aluguel-veiculos/
|   |-- classes/
|   |   |-- veiculo.py         # Classe Veiculo
|   |   |-- carro.py           # Classe Carro
|   |   |-- moto.py            # Classe Moto
|   |-- main.py                # Arquivo principal para criação de instâncias e testes
|   |-- README.md              # Documentação do projeto
