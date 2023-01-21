from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.subdag import SubDagOperator
from subdag_downloads import subdag_downloads
from subdag_transfers import subdag_transfers

with DAG(
    'group_dag', start_date=datetime(2023, 1, 15),
    schedule_interval='@daily', catchup=False
) as dag:

    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval,
            'catchup': dag.catchup}

    downloads = SubDagOperator(
        task_id='downloads',
        subdag=subdag_downloads(dag.dag_id, 'downloads', args)
    )

    check_files = BashOperator(
        task_id='check_files',
        bash_command="echo checking files... | sleep 5 | echo checking complete.."
    )

    transfers = SubDagOperator(
        task_id = 'transfers',
        subdag=subdag_downloads(dag.dag_id, 'transfers', args)
    )

    downloads >> check_files >> transfers
