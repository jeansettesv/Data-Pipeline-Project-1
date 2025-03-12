import pandas as pd
import random
import os
from datetime import datetime, timedelta

SOURCE_DIR = "source_data/"
FILE_NAME = "dados_ficticios.csv"

# Criar diretório source_data se não existir
if not os.path.exists(SOURCE_DIR):
    os.makedirs(SOURCE_DIR)

# Gerar dados fictícios
def gerar_dados():
    clientes = list(range(1, 11))  # 10 IDs de clientes fictícios
    tipos = ["compra", "venda"]
    
    data = []
    for _ in range(50):  # Gerar 50 transações
        cliente_id = random.choice(clientes)
        valor = round(random.uniform(10, 500), 2)  # Valores aleatórios entre 10 e 500
        tipo = random.choice(tipos)
        data_transacao = datetime.now() - timedelta(days=random.randint(1, 30))

        data.append([cliente_id, valor, tipo, data_transacao.strftime("%Y-%m-%d %H:%M:%S")])

    df = pd.DataFrame(data, columns=["cliente_id", "valor", "tipo", "data_transacao"])
    df.to_csv(os.path.join(SOURCE_DIR, FILE_NAME), index=False)

    print(f"✅ Arquivo gerado: {os.path.join(SOURCE_DIR, FILE_NAME)}")

if __name__ == "__main__":
    gerar_dados()
