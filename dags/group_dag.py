from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from group.group_downloads import download_tasks
from group.group_transfers import transfer_tasks

with DAG(
    'group_dag', start_date=datetime(2023, 1, 15),
    schedule_interval='@daily', catchup=False
) as dag:

    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval,
            'catchup': dag.catchup}

    downloads = download_tasks()

    check_files = BashOperator(
        task_id='check_files',
        bash_command="echo checking files... | sleep 5 | echo checking complete.."
    )

    transfers = transfer_tasks()

    downloads >> check_files >> transfers
