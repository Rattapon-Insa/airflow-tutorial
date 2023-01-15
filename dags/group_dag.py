from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'group_dag', start_date=datetime(2023,1,15),
    schedule_interval='@daily', catchup=False
) as dag:

    download_a = BashOperator(
        task_id = 'download_a',
        bash_command="echo I will sleep for 3 sec | sleep 3"
    )

    download_b = BashOperator(
        task_id = 'download_b',
        bash_command="echo I will sleep for 3 sec | sleep 3"
    )

    download_c = BashOperator(
        task_id = 'download_c',
        bash_command="echo I will sleep for 3 sec | sleep 3"
    )

    check_files = BashOperator(
        task_id = 'check_files',
        bash_command="echo checking files... | sleep 5 | echo checking complete.."
    )

    transfer_a = BashOperator(
        task_id = 'transfer_a',
        bash_command = 'echo transfer file a... | sleep 3'
    )

    transfer_b = BashOperator(
        task_id = 'transfer_b',
        bash_command = 'echo transfer file b... | sleep 3'
    )

    transfer_c = BashOperator(
        task_id = 'transfer_c',
        bash_command = 'echo transfer file c... | sleep 3'
    )

    [download_a, download_b, download_c] >> check_files >> [transfer_a, transfer_b, transfer_c]
