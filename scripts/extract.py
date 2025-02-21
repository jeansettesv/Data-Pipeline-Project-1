import boto3
import os

# Configuração do MinIO
s3 = boto3.client(
    's3',
    endpoint_url="http://127.0.0.1:9000",  # MinIO rodando localmente
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

BUCKET_NAME = "meu-projeto"  # Nome do bucket no MinIO
LOCAL_DIR = "processed_data/"  # Pasta onde os arquivos serão baixados

def baixar_arquivos():
    """Baixa os arquivos do MinIO e salva na pasta processed_data/."""
    if not os.path.exists(LOCAL_DIR):
        os.makedirs(LOCAL_DIR)

    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if "Contents" in response:
            for obj in response["Contents"]:
                file_name = obj["Key"]
                local_file_path = os.path.join(LOCAL_DIR, file_name)

                print(f"📥 Baixando {file_name}...")
                s3.download_file(BUCKET_NAME, file_name, local_file_path)
        else:
            print(f"⚠️ Nenhum arquivo encontrado no bucket '{BUCKET_NAME}'.")
    
    except Exception as e:
        print(f"❌ Erro ao acessar o MinIO: {e}")

if __name__ == "__main__":
    baixar_arquivos()

