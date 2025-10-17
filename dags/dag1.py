from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import random

# Define Python functions
def print_welcome():
    print("Welcome from Hasnaa!")

def generate_random_number():
    num = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(num))
    print(f"Random number {num} saved to /tmp/random.txt")

# Define DAG
with DAG(
    dag_id="Airflow_Depi",
    start_date=datetime(2025, 10, 17),
    schedule_interval=None,
    catchup=False,
) as dag:

    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    task2 = PythonOperator(
        task_id="print_welcome",
        python_callable=print_welcome
    )

    task3 = PythonOperator(
        task_id="generate_random_number",
        python_callable=generate_random_number
    )

    task1 >> task2 >> task3
