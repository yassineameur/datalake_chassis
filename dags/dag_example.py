"""
This file contain a very simple dag definition. This tak is composed of two simpke tasks:
 - task 1: it pushed a boolean
 - task 2: receives that boolean.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import python_operator


dag = DAG('test_dag', schedule_interval=timedelta(minutes=5), start_date=datetime(2018, 4, 18))


def print_hello_1(**kwargs):
    return True


def print_hello_2(**kwargs):
    task_instance = kwargs.get('task_instance')

    task_instance.xcom_pull('task_1')


task_1 = python_operator.PythonOperator(
    task_id='task_1',
    python_callable=print_hello_1,
    provide_context=True,
    dag=dag
)

task_2 = python_operator.PythonOperator(
    task_id='task_2',
    python_callable=print_hello_2,
    provide_context=True,
    dag=dag
)


task_1 >> task_2
