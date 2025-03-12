import boto3
import os

# Configuração do MinIO
s3 = boto3.client(
    's3',
    endpoint_url="http://127.0.0.1:9000",  # MinIO rodando localmente
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

BUCKET_NAME = "meu-projeto"
SOURCE_DIR = "source_data/"

def upload_para_minio():
    """Faz upload de todos os arquivos do diretório source_data/ para o MinIO."""
    if not os.path.exists(SOURCE_DIR):
        print("⚠️ Diretório source_data/ não encontrado.")
        return

    arquivos = os.listdir(SOURCE_DIR)
    if not arquivos:
        print("⚠️ Nenhum arquivo encontrado em source_data/.")
        return

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(SOURCE_DIR, arquivo)
        chave_minio = f"dados/{arquivo}"  # Armazena no bucket dentro da "pasta" dados/

        try:
            s3.upload_file(caminho_arquivo, BUCKET_NAME, chave_minio)
            print(f"📤 Upload concluído: {chave_minio}")
        except Exception as e:
            print(f"❌ Erro ao enviar {arquivo} para o MinIO: {e}")

if __name__ == "__main__":
    upload_para_minio()
