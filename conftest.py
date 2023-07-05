import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager as firefoxDriverManager

from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    try:
        d = webdriver.Firefox(service=firefoxService(firefoxDriverManager().install()))# always install latest drivers
    except:
        d = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    yield d
    d.quit()