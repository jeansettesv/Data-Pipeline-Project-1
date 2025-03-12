import pandas as pd
import os

# Diretórios
INPUT_FILE = "data/extracted/transacoes.csv"  # Arquivo extraído do MinIO
OUTPUT_DIR = "data/transformed/"  # Nova pasta para armazenar arquivos transformados
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "transacoes_transformadas.csv")

def transformar_dados():
    """Carrega os dados extraídos, aplica transformações e salva um novo arquivo processado."""

    # Verificar se o arquivo de entrada existe
    if not os.path.exists(INPUT_FILE):
        print(f"⚠️ Arquivo {INPUT_FILE} não encontrado. Execute extract.py primeiro.")
        return
    
    # Criar diretório de saída se não existir
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Carregar o CSV
    df = pd.read_csv(INPUT_FILE)

    # Converter tipos de dados
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")  # Converter valor para número
    df["data_transacao"] = pd.to_datetime(df["data_transacao"], errors="coerce")  # Converter para datetime

    # Remover registros com valores inválidos
    df = df.dropna()  # Remove linhas com valores nulos
    df = df[df["valor"] > 0]  # Remove valores negativos ou zero

    # Criar colunas derivadas
    df["mes_transacao"] = df["data_transacao"].dt.strftime("%Y-%m")  # Criar coluna com Ano-Mês

    # Salvar o novo arquivo transformado
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"✅ Transformação concluída. Arquivo salvo em {OUTPUT_FILE}")

if __name__ == "__main__":
    transformar_dados()
