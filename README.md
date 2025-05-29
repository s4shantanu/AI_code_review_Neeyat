# AI_code_review_Neeyat


This project is a student-level implementation of an **AI Code Review Agent**, built to analyze and improve complete codebases automatically. It aims to enhance code quality by refactoring, identifying issues, and generating a cleaner version of the code with detailed reports.

##  Features

- Upload full codebases (ZIP, folder path, or Git repo)
- Support for multiple programming languages (e.g., Python)
- Detects bugs, vulnerabilities, and anti-patterns
- Improves readability, performance, and code structure
- Generates side-by-side reports with before/after comparisons
- Outputs an improved project folder with refactored code

##  How It Works

1. Upload your codebase using CLI.
2. The AI reviews the code using rule-based and ML techniques.
3. A new folder is created with improved code.
4. A report is generated showing all changes and quality metrics.

##  Tech Stack

- Python (Core)
- Linting & Static Analysis tools (e.g., `pylint`, `flake8`)
- Code Refactoring libraries
- REST API support (optional)
- CLI-based interface

##  Use Cases

- Students improving project submissions
- Developers reviewing personal or team projects
- Anyone wanting quick insights into code quality

##  Requirements

- Python 3.8+
- pip for installing dependencies

```bash
pip install -r requirements.txt
