import csv

def criar_csv(caminho_arquivo: str):
    
    dados = [
        {"Nome": "Ana Silva", "Idade": 28, "Cidade": "São Paulo"},
        {"Nome": "Carlos Souza", "Idade": 35, "Cidade": "Rio de Janeiro"},
        {"Nome": "Mariana Oliveira", "Idade": 22, "Cidade": "Belo Horizonte"},
    ]

   
    colunas = ["Nome", "Idade", "Cidade"]

   
    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        
        escritor.writeheader()

        escritor.writerows(dados)

    print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")

if __name__ == '__main__':
    criar_csv("pessoas.csv")
