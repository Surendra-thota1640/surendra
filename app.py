import os
import psycopg
from flask import Flask
from databricks.sdk import WorkspaceClient

app = Flask(__name__)

def get_connection():
    w = WorkspaceClient()
    cred = w.postgres.generate_database_credential(endpoint=os.environ["LAKEBASE_ENDPOINT"])
    conn = psycopg.connect(
        host=os.environ["PGHOST"],
        dbname=os.environ["PGDATABASE"],
        user=os.environ["PGUSER"],
        port=os.environ.get("PGPORT", 5432),
        password=cred.token,
        sslmode="require",
    )
    return conn

@app.route("/")
def home():
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT current_database(), current_user")
            db, user = cur.fetchone()
        conn.close()
        return (
            "<h1>Hello, World!</h1>"
            "<p>Connected to Lakebase!</p>"
            f"<p>Database: {db}</p>"
            f"<p>User: {user}</p>"
        )
    except Exception as e:
        return f"<h1>Hello, World!</h1><p>Lakebase connection error: {e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
