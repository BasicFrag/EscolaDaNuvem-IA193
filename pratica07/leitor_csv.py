import csv

def ler_csv(caminho_arquivo: str):
    with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)

        print("=== Dados do arquivo CSV ===")
        for linha in leitor:
            nome = linha["Nome"]
            idade = linha["Idade"]
            cidade = linha["Cidade"]
            print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

if __name__ == "__main__":
    ler_csv("pessoas.csv")
