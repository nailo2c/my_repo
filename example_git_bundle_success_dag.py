from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

def _on_success(context):
    print(">>> SUCCESS CALLBACK TRIGGERED <<<")

default_args = {
    "owner": "airflow",
    "retries": 0,
}

with DAG(
    dag_id="git_bundle_success_demo",
    default_args=default_args,
    start_date=days_ago(1),
    schedule=None,
    on_success_callback=_on_success,
    catchup=False,
) as dag:
    BashOperator(
        task_id="always_succeed",
        bash_command="echo 'simulating success' && exit 0",
    )