import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager as firefoxDriverManager


@pytest.fixture
def driver():
    d = webdriver.Firefox(service=firefoxService(firefoxDriverManager().install()))# always install latest drivers
    yield d
    d.quit()