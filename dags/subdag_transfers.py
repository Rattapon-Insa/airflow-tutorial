from airflow import DAG
from airflow.operators.bash import BashOperator

def subdag_transfers(parent_dag_id, child_dag_id, args):
    with DAG(f"{parent_dag_id}.{child_dag_id}",
        start_date=args['start_date'],
        schedule_interval=args['schedule_interval'],
        catchup=args['catchup']) as dag:


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

        return dag
