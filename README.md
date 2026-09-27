# AutomationExercise Login Test

Automated Selenium test that logs into [automationexercise.com](https://www.automationexercise.com/) using a manually-created account, and verifies the login was successful.

## What it does
1. Launches the website
2. Navigates to the Login page
3. Enters the registered email and password
4. Submits the login form
5. Verifies "Logged in as [Name]" appears, confirming successful login

## How to run
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python test_login.py
```

## Notes
- Uses `undetected-chromedriver` instead of plain Selenium, since automationexercise.com shows a bot-detection "One moment, please..." page to standard Selenium-controlled Chrome.
- Update the `EMAIL` and `PASSWORD` constants in `test_login.py` with your own account (create one manually first via the site's Signup page).