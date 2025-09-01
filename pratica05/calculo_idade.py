from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias, considerando apenas anos de 365 dias.
    :param ano_nascimento: Ano de nascimento da pessoa (ex.: 1995)
    :return: Idade aproximada em dias
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias



ano = int(input("Informe o ano de nascimento: "))
print(f"Idade aproximada em dias: {calcular_idade_em_dias(ano)} dias")
