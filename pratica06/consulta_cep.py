"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""
import requests # type: ignore

def consulta_cep(valor_cep):
    resposta_get = requests.get(f"https://viacep.com.br/ws/{valor_cep}/json/")

    if resposta_get.status_code == 400 or resposta_get.json()["erro"] == "true":
        raise ValueError("Erro! Insira um CEP válido")   
    else:
        dicionario_cep: dict = resposta_get.json()
        return dicionario_cep
        

if __name__ == "__main__":
    while True:
        try:
            valor_cep = input("Insira o CEP que deseja consultar: \n").strip()
            if valor_cep == "sair":
                print("Até mais!")
                break
            dicionario_cep = consulta_cep(valor_cep)
            print(f"\nLogradouro: {dicionario_cep["logradouro"]}\nBairro: {dicionario_cep["bairro"]}\nCidade: {dicionario_cep["localidade"]}\nEstado: {dicionario_cep["uf"]}\n\n")
            break
        except ValueError as e:
            print(e)