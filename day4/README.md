# 🔐 Secure CI/CD Pipeline – Core Concepts

## 📌 Pipeline Integration

### Why is it important to run **Trivy scans** (for OS packages and dependencies) as part of the CI/CD pipeline instead of only scanning after deployment?  
- Running Trivy during CI/CD ensures that vulnerable OS packages, libraries, or base images are identified **before the application is deployed**.  
- This prevents insecure images from ever reaching production, reducing the attack surface.  
- If scanning only happens after deployment, attackers may already exploit critical CVEs before fixes are applied.  

### Why is it important to run **security scans (SAST, dependency scanning, DAST)** directly in the CI/CD pipeline instead of only during production?  
- Shifting security **left** catches issues earlier when fixes are cheaper and faster.  
- Developers receive immediate feedback and can remediate before merging to main.  
- Production-only scanning delays detection, increases risk, and creates firefighting scenarios instead of proactive prevention.  

---

## 🛠 Tool Roles

Each tool plays a unique role in the pipeline and complements the others:

| Tool          | Type of Scan                | Example Detection |
|---------------|-----------------------------|-------------------|
| **Bandit**    | SAST (Static Analysis for Python) | Hardcoded passwords, use of `eval()` |
| **Semgrep**   | SAST + Policy-as-Code       | Missing input validation, weak regex validation |
| **Trivy**     | Dependency + Container Scan | Vulnerable Python/OS libraries, insecure base images |
| **OWASP ZAP** | DAST (Dynamic App Testing)  | SQL Injection, XSS, missing security headers |

👉 Together, they cover **code quality, dependencies, container security, and runtime vulnerabilities**.  

---

## 👨‍💻 Developer Actionability

### If **Trivy** reports a **HIGH severity vulnerability** in a base image:  
- Update to the latest patched image (`FROM python:3.10-slim` → `FROM python:3.10.14-slim`).  
- Rebuild and retest the application.  
- If no fix exists, apply temporary mitigations (e.g., WAF, reduced privileges) and track for patch updates.  

### If **Bandit** flags **hardcoded secrets**:  
- Remove secrets from source code immediately.  
- Store secrets securely in environment variables or a secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager, GitHub Secrets).  
- Rotate any leaked credentials without delay.  

---
