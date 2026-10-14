# Lab 5: Static Code Analysis — Issue Report

## Project: Supplier Purchase Order Tracker

### Objective
To identify and fix code quality, security, and formatting issues using Pylint, Bandit, and Flake8.

### Issues Identified in the Original Code

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| SQL string construction (B608) | Security — Medium | 11 | SQL query used string interpolation to insert supplier, item, and quantity values. | Replaced string interpolation with parameterized SQL placeholders (`?`). |
| Shell execution (B605) | Security — High | 21 | `os.system()` executed a shell command containing supplier input. | Removed shell execution and used `print()` for the warehouse notification. |
| Silent exception handling (B110) | Reliability — Low | 27–28 | A broad exception handler silently ignored errors. | Removed the unnecessary exception handler so unexpected database errors are visible. |
| Global statement (W0603) | Code quality | 10 | `placeOrder()` modified the module-level `order_total` variable. | Moved total tracking into `main()`. |
| Invalid function naming (C0103) | Style | 9, 16, 20, 31 | Function names did not follow Python's `snake_case` convention. | Renamed functions using `snake_case`. |
| Unused argument (W0613) | Code quality | 16 | The `remarks` argument was not used. | Removed the unused argument. |
| Missing docstrings (C0116) | Maintainability | Multiple | Functions lacked descriptions of their purpose. | Added descriptive docstrings to functions. |
| Long lines and missing whitespace | Style | 5, 11, 12, 32 | Several lines exceeded the configured line length, and an operator lacked whitespace. | Reformatted SQL and expressions and applied consistent spacing. |

### Verification

The corrected program was executed successfully and printed:

- `notifying warehouse about Acme`
- `1 540`

The Pylint, Bandit, and Flake8 after-fix reports were generated for verification. Their final findings and score must be checked before claiming that all issues are resolved.