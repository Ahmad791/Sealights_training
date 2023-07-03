from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import selenium.common.exceptions as e

@pytest.mark.group1
def test_1(driver: WebDriver):
    driver.get("https://practicetestautomation.com/practice-test-login/")# go to webpage

    #Fill elements and submit
    try:
        driver.find_element(By.ID,"username").send_keys("student")
        driver.find_element(By.NAME,"password").send_keys("Password123")
        driver.find_element(By.XPATH,"//button[@class='btn']").click()
    except e.NoSuchElementException:
        raise "Error locating elements"

    #verfiy logged in successfuly
    assert driver.current_url=="https://practicetestautomation.com/logged-in-successfully/","Can't log in"


