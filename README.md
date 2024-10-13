# API Automation Framework in Python

## Description
This project is an automation framework for testing APIs using Python and pytest, integrated with CI/CD using GitHub Actions.

## Features
- API Testing: Validate RESTful APIs using Pytest.
- CI/CD: Intergrate with GitHub Actions for Automated Testing and deployment
- Reporting: Generate detailed HTML reports of test execution.

## API Testing
- Validate RESTful APIs using Pytest.
- Supports GET, POST, PUT, DELETE operations.
- Ensure schema validation, status code checks, response validation.
- Handle authentication (e.g., API tokens) seamlessly in tests.

## CI/CD Integration
- GitHub Actions used for automated testing and deployment.
- Trigger tests on code push or pull requests.

## Reporting
- Generate detailed HTML reports of test execution with pytest-html.
- Include test summaries, passed/failed test details, logs, and timestamps.
- Easily shareable reports to analyze issues and monitor test progress.
- Example report: ```reports/Test_Execution_Report.html.```

## Installation
To install the necessary dependencies, run:
```bash 
pip install -r requirements.txt
```

Run the test using:
```bash
pytest -v -s --html=reports/Test_Execution_Report.html
```

Auther Name - Prashant Farakate