import pandas as pd
import os
import random
from faker import Faker

# Configuração do Faker para gerar dados fictícios
fake = Faker()

# Arquivo de entrada e saída
TRANSACOES_FILE = "data/source/transacoes.csv"
OUTPUT_DIR = "data/database_bkp/"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "clientes.csv")

# Criar diretório se não existir
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def obter_ids_unicos():
    """Busca os IDs únicos da coluna cliente_id do arquivo transacoes.csv."""
    if not os.path.exists(TRANSACOES_FILE):
        print(f"⚠️ Arquivo {TRANSACOES_FILE} não encontrado.")
        return []

    df = pd.read_csv(TRANSACOES_FILE, usecols=["cliente_id"])
    return df["cliente_id"].drop_duplicates().tolist()

def gerar_clientes():
    """Gera clientes apenas para os IDs presentes no arquivo transacoes.csv."""
    cliente_ids = obter_ids_unicos()
    
    if not cliente_ids:
        print("⚠️ Nenhum cliente encontrado no arquivo transacoes.csv.")
        return

    dados = []
    for cliente_id in cliente_ids:
        nome = fake.name()
        email = fake.email()
        cidade = fake.city()
        data_cadastro = fake.date_this_decade()

        dados.append([cliente_id, nome, email, cidade, data_cadastro])

    df = pd.DataFrame(dados, columns=["id", "nome", "email", "cidade", "data_cadastro"])
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Arquivo de clientes gerado: {OUTPUT_FILE}")

if __name__ == "__main__":
    gerar_clientes()
