import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
