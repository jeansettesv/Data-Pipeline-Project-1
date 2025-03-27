# 🚀 Data Pipeline - MinIO & PostgreSQL

## 📌 Visão Geral
Este projeto implementa um **pipeline de dados** para processar transações fictícias.  
Os dados são armazenados no **MinIO** (como Data Lake) e carregados no **PostgreSQL**.  
O ambiente pode ser configurado **tanto com Docker quanto com scripts manuais**.

---

## 📂 Estrutura do Projeto
```bash
meu-projeto/
├── data/                    # 📂 Diretório principal de dados
│   ├── source/              # 📂 Arquivos gerados antes do upload para o MinIO
│   ├── extracted/           # 📂 Arquivos extraídos do MinIO
│   ├── transformed/         # 📂 Arquivos transformados, prontos para carga no PostgreSQL
├── init_db/                 # 📂 Backup inicial do banco de dados
│   ├── banco_inicial_bkp.sql  # 🗄️ Arquivo SQL para restaurar a base de clientes
├── scripts/                 # 📂 Scripts do pipeline ETL
│   ├── restore_db.py         # 🔄 Restaura o banco antes de rodar o pipeline
│   ├── extract.py            # 🔄 Extrai transações do MinIO
│   ├── transform.py          # 🔄 Processa os dados extraídos
│   ├── load.py               # 🔄 Carrega transações no banco
│   ├── upload_to_minio.py    # 🔄 Envia os arquivos para o MinIO
├── utils/                    # 🛠️ Scripts auxiliares
│   ├── generate_clients.py   # 🔄 Gera clientes a partir de transacoes.csv
│   ├── load_clientes.py      # 🔄 Carrega clientes no banco
│   ├── generate_data.py      # 🔄 Gera transações fictícias
│   ├── backup_db.py          # 🔄 Cria um backup do banco
├── docker-compose.yml        # 🐳 Configuração para rodar no Docker
├── README.md                 # 📄 Documentação do projeto
```
---

## ⚙️ **Configuração e Uso**

### 🔹 **Opção 1: Configuração via Docker**
Se quiser rodar tudo com Docker, basta executar:

```bash
docker-compose up -d
```
✅ Isso iniciará o PostgreSQL e o MinIO automaticamente, com os clientes já carregados no banco.

---

### 🔹 **Opção 2: Configuração Manual**
Caso prefira rodar sem Docker, siga os passos:

1️⃣ Restaurar o banco de dados (opcional se usar Docker)

```bash
python scripts/restore_db.py
```
📌 Isso restaura um backup do banco contendo a tabela de clientes.
⚠️ Não execute este comando se tiver gerado novos dados de transações, pois o backup ficaria desatualizado!

2️⃣ Rodar o pipeline de ETL

```bash
python scripts/upload_to_minio.py  # Envia o arquivo de transações da pasta source para o MinIO
python scripts/extract.py          # Extrai o arquivo transações do MinIO e salva em .csv
python scripts/transform.py        # Processa e transforma os dados extraídos e salva em .csv
python scripts/load.py             # Carrega as transações transformadas no banco de dados
python scripts/create_enriched_table.py  # Cria a tabela transacoes_enriquecidas com JOIN entre clientes e transações
python scripts/export_parquet.py   # Exporta os dados enriquecidos em formato .parquet
```
📌 Ao final deste processo, será gerado o arquivo `transacoes_enriquecidas.parquet` na pasta `data/transformed/`.

3️⃣ Caso queira mudar os dados

Se quiser modificar os dados e reiniciar o pipeline, execute os scripts abaixo antes de rodar o ETL novamente:

```bash
python utils/generate_data.py     # Gera um novo arquivo transacoes.csv com transações fictícias  
python utils/generate_clients.py  # Gera um novo arquivo clientes.csv baseado nos IDs do arquivo de transações  
python utils/load_clientes.py     # Carrega os novos clientes no banco  
python utils/backup_db.py         # (Opcional) Gera um novo backup do banco apenas com os clientes recém-carregados  
```
📌 Depois, volte para a etapa do pipeline de ETL ou restaure o backup antes de prosseguir.

---

## 📦 Exportação Final

Após carregar os dados no banco, o script `export_parquet.py` exporta a tabela `transacoes_enriquecidas` em formato `.parquet` para a pasta `data/transformed/`.  
Esse arquivo pode ser enviado para uma camada de analytics como **Databricks, BigQuery ou Amazon Athena**.


