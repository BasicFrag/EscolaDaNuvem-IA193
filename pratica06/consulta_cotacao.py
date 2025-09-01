"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests as req # type: ignore
from datetime import datetime as dt

def consulta_cotacao(codigo_moeda_entrada: str):
    resposta_get = req.get(f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda_entrada.lower().strip()}-brl")
    if resposta_get.status_code >= 400:
        raise ValueError("Erro! Código de moeda não encontrado/inválido! Tente novamente")
    else:
        resposta_dicionario: dict = resposta_get.json()[f"{codigo_moeda_entrada.upper().strip()}BRL"]
        ultima_atualizacao = dt.fromtimestamp(float(resposta_dicionario["timestamp"])).strftime("%d/%m/%Y, %H:%M:%S")
        print(f"***Cotação {resposta_dicionario["code"]}/{resposta_dicionario["codein"]} - {resposta_dicionario["name"]}***\n Valor atual: R$ {float(resposta_dicionario["bid"]):.2f}\n Máxima: R$ {(float(resposta_dicionario["high"])):.2f}\n Mínima: R$ {float(resposta_dicionario["low"]):.2f}\n Ultima atualização: {ultima_atualizacao}")
        

if __name__ == "__main__":
    while True:
        try:
            entrada_codigo: str = input("Digite o código da moeda que deseja ver a cotação: ")
            if entrada_codigo == "sair":
                print("Até mais!")
                break
            consulta_cotacao(entrada_codigo)
            break
        except ValueError as e:
            print(e)