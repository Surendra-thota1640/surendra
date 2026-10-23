from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>Welcome to my Databricks App.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
