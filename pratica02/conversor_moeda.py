"""1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:


    Valor em reais: R$ 100.00

    Taxa do dólar: R$ 5.60

    Taxa do euro: R$ 6.60 

O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

Francisco Pessanha para Instrutor Bruno: Faltei essa aula. Eu entendi que era sem o uso de entrada do usuário. É isso mesmo?

"""
valor_em_reais: float = 100.00
taxa_dolar: float = 5.60
taxa_euro: float = 6.60

conversao_dolar = valor_em_reais * taxa_dolar
conversao_euro = valor_em_reais * taxa_euro

print(f"""### Conversão de Moedas ###
-----------------------------------      
Valor em reais: R$ {valor_em_reais:.2f}

Taxa do dólar: R$ {taxa_dolar:.2f}

Taxa do euro: R$ {taxa_euro:.2f}
-----------------------------------

Valor em dólares: US$ {conversao_dolar:.2f}
Valor em euros: € {conversao_euro:.2f}

""")