# Static Code Analysis — Issue Report

## Project
Blood Donation Management

## Tools Used
- Pylint — code quality
- Bandit — security analysis
- Flake8 — code style and formatting

## Issues Identified and Fixes Applied

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug / code quality | 17 | `notes=[]` shares the same list across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Assertion used for validation | Security / robustness | 18 | Assertions can be disabled when Python runs in optimized mode. | Replaced the assertion with an explicit `ValueError` check. |
| Hardcoded password | Security | 5 | A demo password was stored directly in source code. | Read the value from the `BLOOD_BANK_OFFICER_PASSWORD` environment variable. |
| Insecure temporary-file path | Security | 60 | `tempfile.mktemp()` can expose a race condition. | Used `tempfile.NamedTemporaryFile()` to create the temporary file safely. |
| Shell command execution | Security | 65 | `os.system()` built a command using phone-list input. | Removed external command execution and made the helper validate and return the phone list. |
| Broad exception handling | Code quality | 45 | `except Exception` catches unrelated errors. | Added explicit handling for unknown blood groups. |
| Missing docstrings | Code quality | Multiple | The module and functions lacked explanatory docstrings. | Added module and function docstrings. |
| Naming conventions | Code quality | Multiple | Function and parameter names used camelCase. | Changed names to snake_case and updated their call sites. |
| Formatting violations | Style | 7, 58, 80, 81 | Long lines, excess blank lines, inline-comment spacing, and missing operator whitespace. | Reformatted the code to satisfy Flake8. |

## Verification Results

| Tool | Before | After |
|---|---|---|
| Pylint | 4.81/10 | 10.00/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 4 reported violations | 0 reported violations |

The updated program was executed successfully, and the three static-analysis tools were run again after the fixes.