import sys
import os

# Adiciona o caminho absoluto da pasta "scripts" ao sys.path
scripts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts'))
sys.path.append(scripts_path)

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from fake_data_generator import gerar_pedidos_excel
from ingestion import ingestions_csv
import pandas as pd
import pyodbc



with DAG(
    'vexus_pipeline',
    start_date=datetime(2025, 5, 20, 20, 0),  # gera arquivos e faz a ingestão a partir de 26/05/2025 às 20h
    schedule_interval='0 20 * * *',           # todo dia às 20h
    catchup=True  
) as dag:
    
    fake_data_generator = PythonOperator(
        task_id='fake_data_generator',
        python_callable=gerar_pedidos_excel,
        op_kwargs={'execution_date_str': '{{ ds }}'}
    )
    
    sql_ingestion = PythonOperator(
        task_id='sql_ingestion',
        python_callable=ingestions_csv
    )
    
    fake_data_generator >> sql_ingestion