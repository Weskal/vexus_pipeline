import pyodbc
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')

def ingestions_csv():
    
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
    
    cursor = conn.cursor()
    
    raw_data_path = '../raw_data'
    arquivos = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]
    
    for arquivo in arquivos:
        try:
            
            df = pd.read_csv(os.path.join(raw_data_path, arquivo))

            for _, row in df.iterrows():
                ordem = row['ordem_venda']
                produto = row['id_produto']

                # Verify if the combination of ORDEM_VENDA + ID_PRODUTO already exists
                cursor.execute("""
                    SELECT 1 FROM SALESORDER 
                    WHERE ORDEM_VENDA = ? AND ID_PRODUTO = ?
                """, ordem, produto)

                if cursor.fetchone():
                    
                    continue

                # Secure insertion with transaction
                cursor.execute("""
                    INSERT INTO SALESORDER (ORDEM_VENDA, ID_PRODUTO, QTD, PRECO_TOTAL_PRODUTO, PRECO_FINAL, DATA_PEDIDO)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, ordem, produto, row['quantidade'], row['preco_total_produto'], row['preco_final'], row['data_pedido'])

            conn.commit()

      
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")
            conn.rollback()

    conn.close()
