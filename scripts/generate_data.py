import pandas as pd
import random
import os
import uuid
from datetime import datetime, timedelta

SOURCE_DIR = "data/source/"
FILE_NAME = "transacoes.csv"  # Nome fixo para garantir substituição automática no MinIO

# Criar diretório data/source se não existir
if not os.path.exists(SOURCE_DIR):
    os.makedirs(SOURCE_DIR)

# Gerar dados fictícios mais realistas
def gerar_dados(num_linhas=10000):  # Geramos 10.000 por padrão
    clientes = list(range(1, 101))  # 100 IDs de clientes fictícios
    categorias = ["eletrônicos", "vestuário", "alimentação", "automotivo", "livros"]
    metodos_pagamento = ["cartão de crédito", "PIX", "boleto", "transferência"]
    tipos = ["compra", "venda"]
    
    data = []
    for _ in range(num_linhas):  # Geramos 10.000 transações
        transacao_id = str(uuid.uuid4())[:8]  # ID único
        cliente_id = random.choice(clientes)
        valor = round(random.uniform(10, 5000), 2)  # Valores aleatórios
        tipo = random.choice(tipos)
        categoria = random.choice(categorias)
        metodo_pagamento = random.choice(metodos_pagamento)
        data_transacao = datetime.now() - timedelta(days=random.randint(1, 60))

        data.append([
            transacao_id, cliente_id, valor, tipo, categoria, metodo_pagamento,
            data_transacao.strftime("%Y-%m-%d %H:%M:%S")
        ])

    df = pd.DataFrame(data, columns=[
        "transacao_id", "cliente_id", "valor", "tipo", "categoria", "metodo_pagamento", "data_transacao"
    ])
    
    df.to_csv(os.path.join(SOURCE_DIR, FILE_NAME), index=False)

    print(f"✅ Arquivo gerado: {os.path.join(SOURCE_DIR, FILE_NAME)} com {num_linhas} linhas.")

if __name__ == "__main__":
    gerar_dados()
