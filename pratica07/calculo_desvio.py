import csv
import pandas as pd

def analisar_log_csv(caminho_arquivo: str):
    
    with open(caminho_arquivo, newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        linhas = [linha for linha in leitor]

    
    df = pd.DataFrame(linhas)

    
    df["tempo_execucao"] = df["tempo_execucao"].astype(float)


    media = df["tempo_execucao"].mean()
    desvio = df["tempo_execucao"].std()

    print(f"Quantidade de execuções: {len(df)}")
    print(f"Média do tempo de execução: {media:.2f} segundos")
    print(f"Desvio padrão: {desvio:.2f} segundos")


if __name__ == "__main__":
    analisar_log_csv("treinamento.csv")
