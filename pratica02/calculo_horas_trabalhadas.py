"""6- Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:


    Número do funcionário (numero_funcionario).

    Quantidade de horas trabalhadas (horas_trabalhadas).

    Valor recebido por hora (valor_por_hora).

Francisco Pessanha para Intrutor Bruno: Faltei essa aula. Como assim "um número com duas casas decimais"? 

"""

numero_funcionario: int = int(input("Insira o número do funcionário: "))
horas_trabalhadas: int = int(input("Insira a quantidade de horas trabalhadas: "))
valor_hora: float = float(input("Insira o valor da hora trabalhada: R$ "))
salario: float = valor_hora * horas_trabalhadas
print(f"Salário: R$ {salario:.2f}")