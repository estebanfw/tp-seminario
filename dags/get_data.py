from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2021, 8, 26),
}

dag = DAG('getting_data', 
            default_args=default_args,
            schedule_interval='* * * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='get_data_task',
    bash_command='python /home/scripts/load_data_to_db-v2.py',
    dag=dag)