"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. 
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros: valor_conta (float): O valor total da conta 
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""

def valor_gorjeta(valor_conta: float, porcentagem_gorjeta: float):
    resultado = valor_conta * (porcentagem_gorjeta / 100)
    return resultado
try:
    valor_conta = float(input("Insira o conta:\n"))
    porcentagem_gorjeta = float(input("Insira a porcentagem de gorjeta desejada:\n"))
except ValueError:
    print(ValueError.__notes__)
    print("Valor inválido! Campos vazios ou caracteres alfabéticos não são permitidos!")