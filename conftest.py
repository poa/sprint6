import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
