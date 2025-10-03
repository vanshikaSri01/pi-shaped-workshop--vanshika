from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is a vulnerable Flask app!"

# Insecure: eval usage
@app.route("/eval")
def run_eval():
    code = request.args.get("code")
    return str(eval(code))  # 🚨 Insecure

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
