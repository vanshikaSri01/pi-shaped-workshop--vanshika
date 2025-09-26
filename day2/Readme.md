## Core Security Concepts

### 1. Purpose of DAST and Its Role in Security Testing
**DAST (Dynamic Application Security Testing)** is used to identify vulnerabilities in a running application by simulating attacks from an external perspective. Unlike SAST (Static Application Security Testing), which analyzes source code, DAST tests the **application behavior in real-time**, identifying issues that only appear during execution, such as misconfigurations, authentication flaws, or runtime vulnerabilities.

DAST complements other security testing methods by providing:
- **External perspective:** Tests the application as an attacker would see it.
- **Runtime vulnerability detection:** Finds flaws that static analysis might miss.
- **Coverage of deployed environments:** Validates security in staging or production systems.

---

### 2. XSS and SQL Injection Vulnerabilities
**XSS (Cross-Site Scripting):**  
Occurs when an attacker injects malicious scripts into a web application, which are then executed in the browser of other users.  
**Impact:** Stealing session tokens, performing actions on behalf of users, or redirecting users to malicious sites.

**SQL Injection:**  
Occurs when an attacker manipulates input to execute unintended SQL queries on the database.  
**Impact:** Unauthorized access to sensitive data, data modification, or full database compromise.

---

### 3. Steps to Fix Vulnerabilities Detected by ZAP
When ZAP identifies vulnerabilities, the following steps can help remediate them:

1. **Review the report:** Understand the type, location, and severity of each issue.
2. **Prioritize fixes:** Address critical vulnerabilities first (e.g., XSS, SQL injection).
3. **Apply secure coding practices:**  
   - Use parameterized queries for database interactions.  
   - Encode or sanitize user inputs before rendering in HTML.  
   - Implement proper authentication and session management.
4. **Configure security headers:** Add HTTP headers like `Content-Security-Policy`, `X-Content-Type-Options`, and `Strict-Transport-Security`.
5. **Re-scan:** Run ZAP again to ensure vulnerabilities have been resolved.

---

### 4. Integrating ZAP in CI/CD for Shift-Left Security
Integrating ZAP scans into CI/CD pipelines supports **shift-left security** by detecting vulnerabilities **early in the development lifecycle**, reducing cost and risk:

- **Automatic scanning:** Every build or deployment triggers a security test.
- **Immediate feedback:** Developers are notified about vulnerabilities before production release.
- **Continuous improvement:** Promotes a culture of secure coding and reduces technical debt.
- **Compliance:** Ensures that security checks are consistently applied across environments.

