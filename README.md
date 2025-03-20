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

---

## ⚙️ **Configuração e Uso**

### 🔹 **Opção 1: Configuração via Docker**
Se quiser rodar tudo com Docker, basta executar:

```bash
docker-compose up -d
```
### 🔹 **Opção 2: Configuração Manual**
Caso prefira rodar sem Docker, siga os passos:

1️⃣ Restaurar o banco de dados (opcional se usar Docker)

```bash
python scripts/restore_db.py
```

2️⃣ Gerar e carregar os dados manualmente

```bash
python utils/generate_clients.py  # Gera clientes.csv
python utils/load_clientes.py     # Carrega clientes no banco
python utils/generate_data.py     # Gera transacoes fictícias
```

3️⃣ Rodar o pipeline de ETL

```bash
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```


