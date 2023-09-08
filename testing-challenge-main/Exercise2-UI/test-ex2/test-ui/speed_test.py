import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define the URL of the website to be tested
WEBSITE_URL = "https://es.idoven.ai/"


# Define the directory where screenshots will be saved
# SCREENSHOT_DIR = "testing-challenge-main/Exercise2-UI/test-ex2/test-ui/screenshot_dir"


# Test Case: Positive Test - Evaluate website speed using DebugBear
def test_evaluate_website_speed_positive():
    # Initialize the Selenium WebDriver (you may need to specify the path to your driver)
    driver = webdriver.Chrome()

    try:
        # Navigate to the DebugBear speed test URL
        driver.get("https://www.debugbear.com/test/website-speed")

        input_field = driver.find_element(By.NAME, "url")
        driver.save_screenshot("screenshots/search_url.png")
        input_field.clear()
        input_field.send_keys(WEBSITE_URL)
        input_field.send_keys(Keys.RETURN)

        # Wait for the test to complete
        # driver.implicitly_wait(30)
        time.sleep(100)
        driver.save_screenshot("screenshots/test_evaluate_website_speed_positive.png")

        result = driver.find_element(By.ID, "test-result")
        time.sleep(5)
        result_text = result.text
        assert result_text == "Test Result"

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main()
