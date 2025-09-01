"""
3- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

< 30: classificacao = "Sobrepeso"

Para os demais cenários: classificacao = "Obeso"

"""

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
mensagem = ""
imc = peso / (altura ** 2)

# Permitir a inserção de altura em centímetros
if altura > 100: 
    altura = altura / 100
    imc = peso / (altura ** 2)

if imc < 18.5:
    mensagem ="Abaixo do peso"
elif imc < 25:
    mensagem = "Peso normal"
elif imc < 30:
    mensagem = "Sobrepeso"
else:
    mensagem = "Obeso"


print(f"{imc:.2f}",'->',mensagem)