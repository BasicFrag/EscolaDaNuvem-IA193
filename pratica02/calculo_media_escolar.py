"""3- Calculadora de Média Escolar 

Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:


    Nota 1: 7.5

    Nota 2: 8.0

    Nota 3: 6.5 

O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

primeira_nota: float = 7.5
segunda_nota: float = 8.0
terceira_nota: float = 6.5

media_aritimetica = (primeira_nota + segunda_nota + terceira_nota) / 3
print(f"""### Cálculo da média escolar ###
--------------------------------
Nota 1: {primeira_nota}
Nota 2: {segunda_nota}
Nota 3: {terceira_nota}
--------------------------------

Média escolar: {media_aritimetica:.2f}""")