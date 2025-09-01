"""4- Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:


    Distância percorrida: 300 km

    Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


"""

distancia_percorrida: int = 300
combustivel_gasto: int = 25

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"""### Calculadora de consumo médio de combustível
--------------------------------
Distância percorrida: {distancia_percorrida} km

Combustível gasto: {combustivel_gasto} litros
--------------------------------

Consumo médio (km/l): {consumo_medio:.2f}
""")