from datetime import datetime, timezone

from airflow.sdk import dag, task


@dag(
    dag_id="hello_demo",
    schedule=None,
    start_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
    catchup=False,
    tags=["demo"],
)
def hello_demo():
    @task
    def hello() -> str:
        message = "Airflow 3.3.1 demo is running"
        print(message)
        return message

    hello()


hello_demo()
