# DevSecOps Sample App

This is a simple Flask app with an intentionally hardcoded secret for practicing **Shift-Left Security** with **Gitleaks**.

## Core Concepts

### Shift-Left Security
- **Definition:** Integrating security checks early in the software development lifecycle.
- **Importance in DevSecOps:**
  - Detect vulnerabilities before production.
  - Reduce the cost and effort of fixing issues.
  - Make security part of the development culture.

---

### Detecting Secrets Early in CI/CD
- **Purpose:** Prevent API keys, passwords, and tokens from reaching production.
- **Benefits:**
  - Minimize risk of data leaks or breaches.
  - Avoid emergency secret rotations.
  - Improve overall application security.

---

### Secure Secret Storage Strategies
- Use **environment variables** instead of hardcoding secrets.
- Use **Secrets Managers** (e.g., HashiCorp Vault, AWS Secrets Manager, Azure Key Vault).
- Store **encrypted configuration files** and decrypt at runtime.
- Inject secrets dynamically during CI/CD pipeline execution.

---

### Potential Exposure & Prevention

- **Exposure scenarios:**
  - Secrets committed to unscanned branches.
  - Secrets present in logs or third-party dependencies.
  - Dynamically generated secrets logged insecurely.

- **Prevention strategies:**
  - Scan all branches and pull requests, not just `main`.
  - Avoid printing secrets in logs.
  - Rotate secrets regularly and enforce access control.
  - Combine automated scanning with manual review for sensitive areas.

---
```
