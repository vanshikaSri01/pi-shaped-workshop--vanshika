## 🔐 Core Security Concepts

### 1. What is the difference between SAST, DAST, and secrets scanning, and why should all be part of a CI/CD pipeline?

- **SAST (Static Application Security Testing):**  
  Analyzes source code, bytecode, or binaries **before running** the application. Helps identify vulnerabilities like SQL injection, hardcoded credentials, or insecure function usage early in the dev cycle.

- **DAST (Dynamic Application Security Testing):**  
  Tests the application **while it is running**. Simulates real-world attacks (like XSS, authentication bypass, etc.) without access to source code.

- **Secrets Scanning:**  
  Detects **sensitive information** (API keys, tokens, passwords, certificates) that may have been accidentally committed to version control.

✅ Combining these three gives defense in depth:
- **SAST** finds insecure code before deployment.  
- **DAST** finds runtime/external attack surfaces.  
- **Secrets scanning** prevents accidental exposure of credentials.

---

### 2. Why is storing secrets in code dangerous? What’s a secure alternative?

- **Danger of storing secrets in code:**  
  - Risk of **leaking** credentials in Git history or public repos.  
  - If compromised, attackers can gain unauthorized access to databases, APIs, or cloud infrastructure.  

- **Secure alternatives:**  
  - Use a **secrets manager** (e.g., HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager).  
  - Use **environment variables** injected at runtime (never stored in source control).  
  - CI/CD platforms often provide secure **secret storage** (e.g., GitHub Actions Secrets, GitLab CI/CD Variables).  

---

### 3. How does adding these scans to a pipeline help enforce Shift-Left Security?

- **Shift-Left Security** means catching issues **earlier** in the SDLC (Software Development Life Cycle).  
- By running SAST, DAST, and secrets scans directly in CI/CD:  
  - Developers get **fast feedback** on vulnerabilities.  
  - Security is automated and not postponed until later stages.  
  - Fixing issues early is **cheaper and faster** than fixing them in production.  

---

### 4. If a scan fails in your pipeline, what is the next step for a developer or DevOps engineer?

1. **Review the report** to understand the vulnerability (severity, location, impact).  
2. **Fix the issue** in the source code or configuration (e.g., sanitize inputs, remove hardcoded secrets, apply secure defaults).  
3. **Commit and push the fix**, triggering a new pipeline run.  
4. **Re-run scans** to validate the issue is resolved.  
5. If false positives occur, **tune the rules or suppress safely** (with justifications).  

---

🚀 **In summary:**  
Adding SAST, DAST, and secrets scanning to CI/CD enforces continuous, automated security checks, helping organizations adopt **DevSecOps** practices and minimize security risks.
