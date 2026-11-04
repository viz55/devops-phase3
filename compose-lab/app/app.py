import os
import socket

import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

MESSAGE = "Hello World!: Edited live in dev mode"


def get_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ["MARIADB_USER"],
        password=os.environ["MARIADB_PASSWORD"],
        database=os.environ["MARIADB_DATABASE"],
        connect_timeout=2,
        autocommit=True,
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/")
def index():
    hostname = socket.gethostname()
    environment = os.environ.get("APP_ENV", "unknown")
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits ("
                "id INT AUTO_INCREMENT PRIMARY KEY, "
                "host VARCHAR(64), "
                "ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            )
            cur.execute("INSERT INTO visits (host) VALUES (%s)", (hostname,))
            cur.execute("SELECT COUNT(*) FROM visits")
            total = cur.fetchone()[0]
        conn.close()
        return jsonify(message=MESSAGE, served_by=hostname, environment=environment,
                       database="connected", total_visits=total)
    except Exception as exc:
        return jsonify(message=MESSAGE, served_by=hostname, environment=environment,
                       database="unavailable", error=type(exc).__name__), 503
