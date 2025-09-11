import json

def escrever_json(caminho_arquivo: str):
    pessoa = {
        "nome": "Ana Silva",
        "idade": 28,
        "cidade": "São Paulo"
    }


    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_json:
        json.dump(pessoa, arquivo_json, ensure_ascii=False, indent=4)

    print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")


def ler_json(caminho_arquivo: str):
  
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados = json.load(arquivo_json)

    print("=== Dados do JSON ===")
    print(f"Nome: {dados['nome']}")
    print(f"Idade: {dados['idade']}")
    print(f"Cidade: {dados['cidade']}")


arquivo = "pessoa.json"
escrever_json(arquivo)
ler_json(arquivo)
