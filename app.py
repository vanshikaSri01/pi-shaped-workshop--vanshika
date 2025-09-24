from flask import Flask
import os
app = Flask(__name__)

# ❌ Hardcoded secret (intentionally for Gitleaks demo)
API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return f"Hello, DevSecOps! 🚀<br>API_KEY = {API_KEY}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)