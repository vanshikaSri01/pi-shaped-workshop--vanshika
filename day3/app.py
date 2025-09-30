# app.py
from flask import Flask, request, jsonify
import sqlite3
import os
from vulnerable_module import dangerous_function

app = Flask(__name__)

# Intentionally hardcoded secret (vulnerability to detect with Gitleaks)
APP_SECRET = "SUPER_SECRET_API_KEY_12345"

def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def hello():
    # Insecure: exposes secret in endpoint response (intentional)
    return jsonify(message="Hello insecure world", secret=APP_SECRET)

@app.route("/search")
def search():
    # Insecure SQL construction (SQL injection risk)
    q = request.args.get("q", "")
    conn = get_db_connection()
    # vulnerable concatenation
    cursor = conn.execute("SELECT id, name from users WHERE name LIKE '%" + q + "%'")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(results=[dict(r) for r in rows])

@app.route("/eval")
def run_eval():
    # Dangerous: insecure eval of user input
    expr = request.args.get("expr", "1+1")
    result = dangerous_function(expr)  # uses eval inside vulnerable_module.py
    return jsonify(result=result)

if __name__ == "__main__":
    # debug True intentionally to simulate developer mistake
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
