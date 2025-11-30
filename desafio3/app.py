import os
from flask import Flask
import time
import redis
import psycopg2

app = Flask(__name__)

time.sleep(10)
redis_host = os.getenv("REDIS_HOST", "localhost")
postgres_host = os.getenv("POSTGRES_HOST", "localhost")
postgres_user = os.getenv("POSTGRES_USER", "admin")
postgres_password = os.getenv("POSTGRES_PASSWORD", "senha123")
postgres_db = os.getenv("POSTGRES_DB", "appdb")


cache = redis.Redis(host=redis_host, port=6379)

postgres = psycopg2.connect(
    host=postgres_host,
    user=postgres_user,
    password=postgres_password,
    dbname=postgres_db
)
cursor = postgres.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS historico (id SERIAL PRIMARY KEY, data TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
postgres.commit()

@app.route("/")
def index():
    valor = cache.incr("visitas")
    cursor.execute("INSERT INTO historico DEFAULT VALUES")
    postgres.commit()
    return f"Visitante número: {valor}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
