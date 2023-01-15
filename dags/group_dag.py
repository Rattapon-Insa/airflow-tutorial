from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.subdag import SubDagOperator
from subdags.subdag_downloads import subdag_downloads

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

    transfer_a = BashOperator(
        task_id='transfer_a',
        bash_command='echo transfer file a... | sleep 3'
    )

    transfer_b = BashOperator(
        task_id='transfer_b',
        bash_command='echo transfer file b... | sleep 3'
    )

    transfer_c = BashOperator(
        task_id='transfer_c',
        bash_command='echo transfer file c... | sleep 3'
    )

    downloads >> check_files >> [
        transfer_a, transfer_b, transfer_c]
