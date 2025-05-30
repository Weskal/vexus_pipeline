import sys
import os

# Adding the absolute path of the "scripts" folder to sys.path (only if necessary)
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

# Define the default arguments for the DAG
with DAG(
    'vexus_pipeline',
    start_date=datetime(2025, 5, 20, 20, 0),  # generates files and ingestion starting from 26/05/2025 at 8pm
    schedule_interval='0 20 * * *',           # Every day at 8pm
    catchup=True  
) as dag:
    
    # Creating the first task to execute the fake data generator, and save these data in CSV files inside the raw_data folder
    fake_data_generator = PythonOperator(
        task_id='fake_data_generator',
        python_callable=gerar_pedidos_excel,
        op_kwargs={'execution_date_str': '{{ ds }}'}
    )
    
    # Creating the second task to execute the ingestion of the CSV files into the SQL Server database
    sql_ingestion = PythonOperator(
        task_id='sql_ingestion',
        python_callable=ingestions_csv
    )
    
    fake_data_generator >> sql_ingestion