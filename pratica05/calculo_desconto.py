def calcular_desconto(preco_original: float,percentual_desconto: float):
    valor_desconto = preco_original * (percentual_desconto / 100)

    preco_final = preco_original - valor_desconto


    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto aplicado: {percentual_desconto:.2f}%")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")



if __name__ == "__main__":
    preco_original = float(input("Informe o preço do produto: "))
    percentual_desconto = float(input("Informe o percentual de desconto (%): "))
    calcular_desconto(preco_original,percentual_desconto)