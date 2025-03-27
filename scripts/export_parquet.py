from sqlalchemy import create_engine
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

# Configuração
DB_URI = "postgresql://postgres:admin@localhost:5432/engenhariadedados1"
OUTPUT_FOLDER = "data/transformed"
OUTPUT_FILE = "transacoes_enriquecidas.parquet"

def exportar_para_parquet():
    print("📦 Conectando ao PostgreSQL com SQLAlchemy...")
    engine = create_engine(DB_URI)

    try:
        df = pd.read_sql_query("SELECT * FROM transacoes_enriquecidas", engine)
    except Exception as e:
        print(f"❌ Erro ao consultar o banco: {e}")
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)

    try:
        table = pa.Table.from_pandas(df)
        pq.write_table(table, output_path)
        print(f"✅ Arquivo Parquet salvo com sucesso em: {output_path.replace(os.sep, '/')}")
    except Exception as e:
        print(f"❌ Erro ao salvar Parquet: {e}")

if __name__ == "__main__":
    exportar_para_parquet()
