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

CLIENTS_FILE = "data/source/clientes.csv"

def conectar_banco():
    """Estabelece conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conectado ao PostgreSQL!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        return None

def criar_tabela_clientes():
    """Cria a tabela clientes se ela não existir."""
    conn = conectar_banco()
    if conn is None:
        return
    
    cur = conn.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        cidade TEXT,
        data_cadastro TIMESTAMP DEFAULT NOW()
    );
    """
    
    try:
        cur.execute(query)
        conn.commit()
        print("✅ Tabela 'clientes' criada/verificada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar/verificar a tabela: {e}")
    
    cur.close()
    conn.close()

def inserir_clientes():
    """Insere os clientes no PostgreSQL."""
    conn = conectar_banco()
    if conn is None:
        return
    
    cur = conn.cursor()

    if not os.path.exists(CLIENTS_FILE):
        print(f"⚠️ Arquivo {CLIENTS_FILE} não encontrado. Execute generate_clients.py primeiro.")
        return

    df = pd.read_csv(CLIENTS_FILE)

    query = """
    INSERT INTO clientes (id, nome, email, cidade, data_cadastro)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """

    try:
        for _, row in df.iterrows():
            cur.execute(query, tuple(row))
        
        conn.commit()
        print(f"✅ {len(df)} clientes inseridos no banco!")

    except Exception as e:
        print(f"❌ Erro ao inserir clientes: {e}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    criar_tabela_clientes()  # Garante que a tabela existe antes de inserir os dados
    inserir_clientes()
