from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'parallel_dag', start_date=datetime(2023,1,15),
    schedule_interval='@daily', catchup=False
) as dag:
    
    extract_a = BashOperator(
        task_id ='extract_a',
        bash_command='sleep 1'
    )
