"""2- Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:


    Nome do produto: "Camiseta"

    Preço original: R$ 50.00

    Porcentagem de desconto: 20% 

O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


"""

nome_do_produto: str = "Camiseta"
preco_original: float = 50.0
porcentagem_desconto: float = 0.2

preco_descontado: float = preco_original * (1 - porcentagem_desconto)
print(f"""### Cálculo de desconto ###
--------------------------------
Nome do produto: {nome_do_produto}

Preço original: R$ {preco_original:.2f}

Porcentagem de desconto: {porcentagem_desconto*100:.0f}%
--------------------------------

Preço final: R$ {preco_descontado:.2f}""") 