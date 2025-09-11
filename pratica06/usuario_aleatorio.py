import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("=== Perfil de Usuário Aleatório ===")
        print(f"Nome : {nome}")
        print(f"Email: {email}")
        print(f"País : {pais}")
    else:
        print("Erro ao acessar a API. Código:", resposta.status_code)


if __name__ == "__main__":
    gerar_usuario()
