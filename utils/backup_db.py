import os
import subprocess

# Configurações do backup
BACKUP_DIR = "init_db/"
BACKUP_FILE = os.path.join(BACKUP_DIR, "banco_inicial_bkp.sql")
DB_NAME = "engenhariadedados1"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
EXCLUDE_TABLES = ["transacoes"]

def criar_backup():
    """Gera um backup do banco de dados PostgreSQL, excluindo a tabela de transações."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    exclude_cmd = " ".join([f"--exclude-table={table}" for table in EXCLUDE_TABLES])

    # Definir variável de ambiente PGPASSWORD e chamar pg_dump usando subprocess
    comando = f'pg_dump -U {DB_USER} -h {DB_HOST} -d {DB_NAME} {exclude_cmd} -f {BACKUP_FILE}'
    
    print(f"📂 Criando backup do banco em: {BACKUP_FILE}")
    
    resultado = subprocess.run(comando, shell=True, env={**os.environ, "PGPASSWORD": DB_PASSWORD})

    if resultado.returncode == 0:
        print("✅ Backup criado com sucesso!")
    else:
        print(f"❌ Erro ao criar o backup. Código de erro: {resultado.returncode}")

if __name__ == "__main__":
    criar_backup()
