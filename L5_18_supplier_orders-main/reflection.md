# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential security vulnerabilities, programming errors, and code-quality problems before deployment.

## 2. What are the differences between Pylint, Bandit, and Flake8?

- **Pylint:** Checks code quality, naming conventions, documentation, and potential programming errors.
- **Bandit:** Identifies potentially insecure coding patterns in Python.
- **Flake8:** Checks Python style and formatting violations.

Using these tools together provides broader coverage of code-quality and security concerns.

## 3. What issues were found and how were they fixed?

The original program contained potentially unsafe SQL string construction, shell command execution, silent exception handling, inconsistent function naming, missing docstrings, and formatting violations.

I replaced SQL string interpolation with parameterized queries, removed shell execution, eliminated unnecessary silent exception handling, improved naming conventions, added docstrings, and corrected formatting issues.

## 4. What are the benefits and limitations of static analysis?

Static analysis helps detect potential problems early, improves code consistency, and makes software easier to maintain. However, warnings require developer judgment, and static analysis cannot guarantee that a program is free of bugs. Runtime testing and code review are also necessary.