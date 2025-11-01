from celery import Celery
from db_manager import DBManager
from os import environ
from dotenv import load_dotenv

load_dotenv()


app = Celery(
    "gate",
    broker="amqp://gate:1234@localhost:5672/gate_vhost"
)

@app.task
def save(start_ip,end_ip,country_code):
    with DBManager(
        host=environ.get("postgres_host"),
        port=environ.get("postgres_port"),
        database=environ.get("postgres_database"),
        user=environ.get("postgres_user"),
        password=environ.get("postgres_password")
    ) as db:
        try:
            db.cursor.execute(
                f"insert into ip_ranges(start_ip,end_ip,country_code) values ({start_ip},{end_ip},'{country_code}');"
            )
        except Exception as e:
            print(e)
            db.connection.rollback()
