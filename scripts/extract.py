import boto3
import os

# Configuração do MinIO
s3 = boto3.client(
    's3',
    endpoint_url="http://127.0.0.1:9000",  # API correta do MinIO
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin"
)

BUCKET_NAME = "meu-projeto"
FOLDER_PREFIX = "dados/"  # Nome da "pasta" no MinIO
LOCAL_DIR = "data/extracted/"

def baixar_arquivos():
    """Baixa os arquivos do MinIO e salva na pasta data/extracted/."""
    
    # Criar a pasta de destino se não existir
    if not os.path.exists(LOCAL_DIR):
        os.makedirs(LOCAL_DIR)

    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=FOLDER_PREFIX)
        
        if "Contents" in response:
            for obj in response["Contents"]:
                file_name = obj["Key"]  # Nome do arquivo no MinIO
                base_name = os.path.basename(file_name)  # Remove diretórios
                local_file_path = os.path.join(LOCAL_DIR, base_name)  # Caminho correto
                
                print(f"📥 Baixando {file_name} para {local_file_path}...")
                s3.download_file(BUCKET_NAME, file_name, local_file_path)
            
            print("✅ Extração concluída!")

        else:
            print(f"⚠️ Nenhum arquivo encontrado no bucket '{BUCKET_NAME}' na pasta '{FOLDER_PREFIX}'.")

    except Exception as e:
        print(f"❌ Erro ao acessar o MinIO: {e}")

if __name__ == "__main__":
    baixar_arquivos()