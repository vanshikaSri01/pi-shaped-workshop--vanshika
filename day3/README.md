# CI/CD-Based Secure Coding & Code Scanning Lab

Title: CI/CD-Based Secure Coding & Code Scanning with Bandit, Semgrep, Gitleaks & OWASP ZAP

## Objective
Build and execute a GitLab pipeline that runs Bandit, Semgrep, Gitleaks and OWASP ZAP to detect insecure coding patterns, secrets, and runtime vulnerabilities (DAST).

## Repo contents
- `app.py` — sample Flask app with intentional issues.
- `vulnerable_module.py` — demonstrates insecure `eval`.
- `requirements.txt` — includes intentionally old packages.
- `semgrep.yml` — semgrep rules for this lab.
- `gitleaks.toml` — simple gitleaks rule.
- `bandit.yml` — optional Bandit config.
- `.gitlab-ci.yml` — CI pipeline that runs scans and saves reports as artifacts.

## How the pipeline works
Stages:
1. **smoke** — prepare DB.
2. **bandit_scan** — SAST run using Bandit. Outputs `bandit-report.html` and `bandit-report.json`.
3. **semgrep_scan** — additional SAST/pattern detection. Outputs `semgrep-report.json` and `semgrep-report.txt`.
4. **gitleaks_scan** — secrets scanning. Outputs `gitleaks-report.json`.
5. **zap_scan** — DAST using OWASP ZAP scanning the running Flask app. Outputs `zap-report.html`.
6. **generate_report** — aggregation / artifact availability.

Reports are saved as GitLab job artifacts — download them from the pipeline UI.

## Setup & test locally (quick)
1. Create virtualenv: `python -m venv .venv && source .venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Initialize DB: `python - <<'PY'\nimport sqlite3\nconn=sqlite3.connect('example.db')\nconn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')\nconn.execute(\"INSERT OR IGNORE INTO users (id,name) VALUES (1,'alice')\")\nconn.commit(); conn.close()\nPY`
4. Run app: `python app.py`
5. Quick checks:
   - `curl "http://127.0.0.1:5000/?q=test"`
   - `curl "http://127.0.0.1:5000/eval?expr=2+2"`

## How to run the scans locally (optional)
- Bandit: `bandit -r . -f html -o bandit-report.html`
- Semgrep: `semgrep --config semgrep.yml --output semgrep-report.txt`
- Gitleaks: `gitleaks detect --source . --report-path gitleaks-report.json`
- ZAP: easiest with docker `docker run -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:5000 -r zap-report.html`

## Fix one identified issue (exercise)
We will fix the hardcoded secret in `app.py` and move to an environment variable.

Before change (vulnerable):
```python
APP_SECRET = "SUPER_SECRET_API_KEY_12345"
