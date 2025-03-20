import psycopg2

# Configuração do banco de dados
DB_CONFIG = {
    "dbname": "engenhariadedados1",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

def conectar_banco():
    """Estabelece conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Conectado ao PostgreSQL!")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        return None

def criar_tabela_enriquecida():
    """Cria a tabela transacoes_enriquecidas a partir do JOIN entre clientes e transacoes."""
    conn = conectar_banco()
    if conn is None:
        return
    
    cur = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS transacoes_enriquecidas AS
    SELECT 
        t.transacao_id, 
        c.nome, 
        c.email, 
        c.cidade, 
        t.valor, 
        t.tipo, 
        t.categoria, 
        t.metodo_pagamento, 
        t.data_transacao, 
        t.mes_transacao
    FROM transacoes t
    JOIN clientes c ON t.cliente_id = c.id;
    """

    try:
        cur.execute(query)
        conn.commit()
        print("✅ Tabela 'transacoes_enriquecidas' criada com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao criar a tabela: {e}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    criar_tabela_enriquecida()
