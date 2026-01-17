from airflow import DAG
from airflow.operators.bash import BashOperator
import logging

# Add a test comment
def _on_success(context):
    logging.getLogger().warning(">>> SUCCESS CALLBACK TRIGGERED VERSION 3 <<<")

def _on_failure(context):
    logging.getLogger().warning(">>> FAILURE CALLBACK TRIGGERED VERSION 4 <<<")

default_args = {
    "owner": "airflow",
    "retries": 0,
}

with DAG(
    dag_id="git_bundle_success_demo",
    default_args=default_args,
    schedule=None,
    on_success_callback=_on_success,
    on_failure_callback=_on_failure,
    catchup=False,
) as dag:
    BashOperator(
        # task_id="always_succeed",
        # bash_command="echo 'simulating success' && exit 0",
        task_id="always_fail",
        bash_command="echo 'simulating failure' && exit 1",
    )
