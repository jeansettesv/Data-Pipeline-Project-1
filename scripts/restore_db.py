import os
import subprocess

# Configuração do banco
DB_NAME = "engenhariadedados1"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
BACKUP_FILE = "init_db/banco_inicial_bkp.sql"

def banco_existe():
    """Verifica se o banco de dados já existe."""
    comando = f'psql -U {DB_USER} -h {DB_HOST} -tAc "SELECT 1 FROM pg_database WHERE datname = \'{DB_NAME}\';"'
    resultado = subprocess.run(comando, shell=True, env={**os.environ, "PGPASSWORD": DB_PASSWORD}, capture_output=True, text=True)

    return resultado.stdout.strip() == "1"

def criar_banco():
    """Cria o banco de dados se ele não existir."""
    if banco_existe():
        print(f"✅ O banco {DB_NAME} já existe.")
    else:
        print(f"📂 Criando o banco {DB_NAME}...")
        comando = f'psql -U {DB_USER} -h {DB_HOST} -c "CREATE DATABASE {DB_NAME};"'
        resultado = subprocess.run(comando, shell=True, env={**os.environ, "PGPASSWORD": DB_PASSWORD}, capture_output=True, text=True)

        if resultado.returncode == 0:
            print("✅ Banco criado com sucesso!")
        else:
            print(f"❌ Erro ao criar o banco: {resultado.stderr}")

def restaurar_banco():
    """Restaura o banco de dados a partir do backup SQL."""
    if not os.path.exists(BACKUP_FILE):
        print(f"⚠️ Arquivo {BACKUP_FILE} não encontrado.")
        return
    
    criar_banco()

    print(f"🔄 Restaurando o banco de dados a partir de {BACKUP_FILE}...")
    comando = f"psql -U {DB_USER} -h {DB_HOST} -d {DB_NAME} -f {BACKUP_FILE}"
    resultado = subprocess.run(comando, shell=True, env={**os.environ, "PGPASSWORD": DB_PASSWORD}, capture_output=True, text=True)

    if resultado.returncode == 0:
        print("✅ Banco restaurado com sucesso!")
    else:
        print(f"❌ Erro ao restaurar o banco: {resultado.stderr}")

if __name__ == "__main__":
    restaurar_banco()
