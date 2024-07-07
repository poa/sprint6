from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class L:
    """Locators class

    Contains locators for web elements for base page
    """

    # fmt: off
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Header_Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]//button[text()='Заказать']")
    # fmt: on


class BasePage:
    APP_URL = "https://qa-scooter.praktikum-services.ru"
    PAGE_PATH = "/"
    TIMEOUT = 10

    def __init__(self, driver, url=None):
        self.driver = driver

        self.url = url if url else self.APP_URL + self.PAGE_PATH

        self.driver.get(self.url)

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
        
    def wait_for_url_change(self, location, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(location))
