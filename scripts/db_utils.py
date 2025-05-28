import os
os.environ['LD_LIBRARY_PATH'] = '/opt/microsoft/msodbcsql18/lib64'
import pyodbc
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')

def carregar_produtos_sql():
    print(f"{datetime.now()} - Iniciando conexão com o banco...")
    
    try:

        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};'
            f'SERVER={server};'  
            f'DATABASE={database};'
            f'UID={user};'
            f'PWD={password};'
            'Encrypt=no;'  
            'TrustServerCertificate=yes;'  
            'Connection Timeout=30;'  
            'Login Timeout=30'  
        )
        
        print(f"{datetime.now()} - Conexão estabelecida com sucesso!")
        
        with conn.cursor() as cursor:
            print(f"{datetime.now()} - Executando consulta...")
            cursor.execute("""
                SELECT 
                    ID_PRODUTO as id_produto, 
                    CAST(PRECO AS FLOAT) as preco
                FROM PRODUTOS
            """)
            
            rows = cursor.fetchall()
            print(f"{datetime.now()} - {len(rows)} registros encontrados.")
            
            def converter_preco(valor):
                try:
                    return float(str(valor).replace(',', '.'))
                except ValueError:
                    print(f"Erro ao converter preço: {valor}")
                    return 0.0
            
            return [
                {
                    "id_produto": row.id_produto,
                    "preco": converter_preco(row.preco)
                }
                for row in rows
            ]
            
    except pyodbc.Error as e:
        print(f"{datetime.now()} - ERRO DE CONEXÃO: {str(e)}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print(f"{datetime.now()} - Conexão fechada.")