from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    APP_URL = "https://qa-scooter.praktikum-services.ru"
    TIMEOUT = 10

    def __init__(self, driver, url=APP_URL):
        self.driver = driver
        self.driver.get(url)

    def find_present_element(self, locator, timeout=TIMEOUT):
        result = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return result

    def find_present_elements(self, locator, timeout=TIMEOUT):
        result = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator), message=f"Not found: {locator}"
        )
        return result

    def find_visible_element(self, locator, timeout=TIMEOUT):
        result = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return result

    def scroll_to_element(self, element: WebElement, timeout=TIMEOUT):
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
