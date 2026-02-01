# FavQs API Tests

This project contains automated API tests for the **FavQs** public API  
(https://favqs.com/api/) implemented using **Python**, **requests**, and **pytest**.

The tests cover user creation, retrieval, and update flows using API-only
interactions, as required by the assignment.

---

## Tech Stack

- Python 3.9+
- requests
- pytest
- pytest-html
- flake8
- python-dotenv

---

## Project Structure

api_favqa_tests/
├── src/
│ ├── client/ # API client (FavQsClient)
│ ├── data/ # Request payloads
│ ├── utils/ # HTTP statuses, helpers
│ └── config.py # Base URL and API key config
├── tests/
│ └── test_user_flow.py
├── reports/ # HTML test reports (not committed)
├── .env # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md


---

## Test Scenarios

### 1. Create and Get User
- Create a new user via API
- Retrieve user information
- Verify:
  - `login` matches the created user
  - `email` is correctly stored (validated via API response structure)

### 2. Update User
- Update user `login` and `email`
- Retrieve updated user data
- Verify:
  - updated `login` value
  - successful update response from API

Each test run uses **unique user data** generated with `uuid` to avoid conflicts
between executions.

---

## Setup Instructions

### 1. Create `.env` file

Create a `.env` file in the project root and add your FavQs API key:

```env
FAVQS_API_KEY=your_api_key_here
You can generate an API key here:
https://favqs.com/api_keys

2. Create virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Run Tests
Run tests normally
pytest -v
Run tests with HTML report
pytest -v -s --html=reports/report.html --self-contained-html
After execution, open reports/report.html in a browser to view the report.

Code Quality
To run static code analysis:

flake8 .
Notes
All API calls are executed using HTTP requests only (no UI).

API key and generated reports are excluded from version control.

Test output and API responses are logged to console and included in the HTML report.

