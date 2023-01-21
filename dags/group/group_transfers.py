from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def transfer_tasks():
    with TaskGroup('transfers', tooltip='Transfer tasks') as group:


        transfer_a = BashOperator(
        task_id='transfer_a',
        bash_command='sleep 10'
        )

        transfer_b = BashOperator(
        task_id='transfer_b',
        bash_command='sleep 10'
        )

        transfer_c = BashOperator(
        task_id='transfer_c',
        bash_command='sleep 10'
        )

        return group
