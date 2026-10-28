# Static Code Analysis — Reflection

## 1. What did you learn from this lab?

I learned how to use Pylint, Bandit, and Flake8 to improve Python code quality, security, and formatting. Pylint helped identify naming problems, missing docstrings, and unsafe coding practices. Bandit detected potentially insecure patterns, while Flake8 identified formatting and style violations.

## 2. What issues did you identify and fix?

I fixed several issues, including a mutable default argument, missing docstrings, inconsistent naming conventions, broad exception handling, a hardcoded password, an insecure temporary-file function, and unsafe shell command execution. I also corrected formatting issues and improved blood-group compatibility handling.

## 3. How did you verify your fixes?

I ran all three static analysis tools before and after modifying the code. The original Pylint score was 4.81/10, and the final score was 10.00/10. Bandit initially reported four findings and reported zero findings after the changes. Flake8 initially reported four violations and reported none after the fixes. I also executed the updated Python program to check that it ran without a traceback.

## 4. Why is static code analysis important?

Static code analysis helps identify potential bugs, security weaknesses, and style violations without requiring the program to execute during the analysis. It improves maintainability, readability, and consistency and helps developers identify problems earlier.

## 5. What challenges did you face?

One challenge was understanding the different warnings reported by the three tools and deciding how to fix them without unnecessarily changing the program's behavior. I also encountered a Windows PowerShell restriction while activating the virtual environment and resolved it by activating the environment through Command Prompt.

## Conclusion

This lab helped me understand how static analysis tools complement one another. Using Pylint, Bandit, and Flake8 together made it easier to identify and fix code-quality, security, and formatting issues. The final results demonstrated an improvement in the analyzed code.
