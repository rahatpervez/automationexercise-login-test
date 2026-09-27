"""
Automated test: Login to AutomationExercise.com
Author: Md. Rahat Pervez

Steps automated:
1. Launch the website
2. Navigate to the Login page
3. Enter registered email and password
4. Submit the login form
5. Verify the login was successful
"""

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---- Replace with the account you created manually ----
EMAIL = "rahatparvez.official@gmail.com"
PASSWORD = "parvez.507"

BASE_URL = "https://www.automationexercise.com/"


def setup_driver():
    """Set up and return an undetected Chrome WebDriver instance
    (avoids the site's 'One moment, please...' bot-check page)."""
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options, version_main=153)
    return driver


def test_login():
    driver = setup_driver()
    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Launch the website
        driver.get(BASE_URL)
        time.sleep(3)  # give the anti-bot check page a moment to clear
        print("Step 1: Website launched ->", driver.title)

        # Step 2: Navigate to the Login page
        signup_login_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
        )
        signup_login_link.click()
        print("Step 2: Navigated to Login page")

        # Step 3: Enter registered email and password
        email_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))
        )
        password_field = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")

        email_field.clear()
        email_field.send_keys(EMAIL)
        password_field.clear()
        password_field.send_keys(PASSWORD)
        print("Step 3: Entered email and password")

        # Step 4: Submit the login form
        login_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
        login_button.click()
        print("Step 4: Login form submitted")

        # Step 5: Verify login was successful
        logged_in_text = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]"))
        )
        print("Step 5: SUCCESS ->", logged_in_text.text)
        assert "Logged in as" in logged_in_text.text

    except Exception as e:
        print("TEST FAILED:", e)
        raise

    finally:
        time.sleep(3)  # pause so you can see the final page before it closes
        driver.quit()


if __name__ == "__main__":
    test_login()