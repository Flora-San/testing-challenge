import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define the URL of the website to be tested
WEBSITE_URL = "https://es.idoven.ai/"


@pytest.fixture
def browser(request):
    # Initialize the Selenium WebDriver (you may need to specify the path to your driver)
    driver = webdriver.Chrome()

    # Make the WebDriver instance available to the test function
    request.cls.driver = driver
    yield driver

    # Clean up after the test is done
    driver.quit()


# Test Case: Positive Test - Evaluate website speed using DebugBear
@pytest.mark.usefixtures("browser")
class TestEvaluateWebsiteSpeed:
    def test_evaluate_website_speed_positive(self):
        # Navigate to the DebugBear speed test URL
        self.driver.get("https://www.debugbear.com/test/website-speed")

        # Find the input field, enter the website URL, and take a screenshot
        input_field = self.driver.find_element(By.NAME, "url")
        input_field.clear()
        input_field.send_keys(WEBSITE_URL)
        input_field.send_keys(Keys.RETURN)
        time.sleep(100)  # Wait for the test to complete
        self.driver.save_screenshot("screenshots/test_evaluate_website_speed_positive.png")

        # Find the result element by ID and verify its text
        result = self.driver.find_element(By.ID, "test-result")
        result_text = result.text
        assert result_text == "Test Result"

    def test_evaluate_website_speed_negative_invalid_url(self):
        # Navigate to the DebugBear speed test URL
        self.driver.get("https://www.debugbear.com/test/website-speed")

        # Find the input field and enter an invalid URL, then take a screenshot
        input_field = self.driver.find_element(By.NAME, "url")
        input_field.clear()
        input_field.send_keys("invalid-url")  # Replace with an invalid URL
        input_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for the error message to appear
        self.driver.save_screenshot("screenshots/test_evaluate_website_speed_negative.png")

        # Find the error message element and verify its presence
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message")
        assert error_message.is_displayed()

    def test_evaluate_website_speed_elements_present(self):
        # Navigate to the DebugBear speed test URL
        self.driver.get("https://www.debugbear.com/test/website-speed")

        # Find the input field, enter the website URL, and take a screenshot
        input_field = self.driver.find_element(By.NAME, "url")
        input_field.clear()
        input_field.send_keys(WEBSITE_URL)
        input_field.send_keys(Keys.RETURN)
        time.sleep(100)  # Wait for the test to complete
        self.driver.save_screenshot("screenshots/test_evaluate_website_speed_elements.png")

        # Find and verify the presence of specific elements on the results page
        assert self.driver.find_element(By.ID, "test-result").is_displayed()
        # assert self.driver.find_element(By.ID, "performance-score").is_displayed()

    def test_open_new_window_and_switch(self):
        # Open a new window using JavaScript
        self.driver.get("https://www.debugbear.com/test/website-speed")

        # Find the input field, enter the website URL, and take a screenshot
        input_field = self.driver.find_element(By.NAME, "url")
        input_field.clear()
        input_field.send_keys(WEBSITE_URL)
        input_field.send_keys(Keys.RETURN)
        time.sleep(90)

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Navigate to a different URL in the new window
        self.driver.get("https://www.debugbear.com/test/website-speed/7tfLDbz7/overview#test-result")

        # Perform actions in the new window (e.g., interacting with elements)
        # For example, you can find elements and make assertions here

        # Switch back to the original window
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Perform actions in the original window (e.g., continue with your test)


if __name__ == "__main__":
    pytest.main()
