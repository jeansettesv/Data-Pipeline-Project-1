import psycopg2
import pandas as pd
import os

# Configuração do banco de dados
DB_CONFIG = {
    "dbname": "engenhariadedados1",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

INPUT_FILE = "data/transformed/transacoes_transformadas.csv"  # Arquivo processado

# Criar conexão com o banco de dados
def conectar_banco():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conectado ao PostgreSQL!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        return None

# Criar tabela se não existir
def criar_tabela():
    conn = conectar_banco()
    if conn is None:
        return
    
    cur = conn.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS transacoes (
        transacao_id VARCHAR(50) PRIMARY KEY,
        cliente_id INT,
        valor NUMERIC,
        tipo TEXT,
        categoria TEXT,
        metodo_pagamento TEXT,
        data_transacao TIMESTAMP,
        mes_transacao TEXT
    );
    """
    
    try:
        cur.execute(query)
        conn.commit()
        print("✅ Tabela 'transacoes' criada/verificada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar a tabela: {e}")
    
    cur.close()
    conn.close()

# Inserir dados no banco com overwrite
def inserir_dados():
    conn = conectar_banco()
    if conn is None:
        return
    
    cur = conn.cursor()

    if not os.path.exists(INPUT_FILE):
        print(f"⚠️ Arquivo {INPUT_FILE} não encontrado. Execute transform.py primeiro.")
        return

    df = pd.read_csv(INPUT_FILE)

    try:
        # 🔄 Remover dados antigos (overwrite)
        print("🗑️ Limpando a tabela 'transacoes' antes da nova inserção...")
        cur.execute("TRUNCATE TABLE transacoes;")
        conn.commit()

        # Inserção dos novos dados
        query = """
        INSERT INTO transacoes (transacao_id, cliente_id, valor, tipo, categoria, metodo_pagamento, data_transacao, mes_transacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        for _, row in df.iterrows():
            cur.execute(query, tuple(row))
        
        conn.commit()
        print(f"✅ {len(df)} registros inseridos no banco!")

    except Exception as e:
        print(f"❌ Erro ao inserir os dados: {e}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    criar_tabela()
    inserir_dados()
