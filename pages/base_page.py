from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class TD:
    """TestData class

    Contains data used for testing base page
    """
    
    YANDEX_LOGO_DST = "https://dzen.ru/"

class L:
    """Locators class

    Contains locators for web elements for base page
    """

    # fmt: off
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Header_Header')]//button[text()='Заказать']")

    SCOOTER_LOGO           = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO         = (By.XPATH, "//img[@alt='Yandex']")

    # fmt: on


class BasePage:
    APP_URL = "https://qa-scooter.praktikum-services.ru"
    PAGE_PATH = "/"
    TIMEOUT = 10

    def __init__(self, driver, url=None, keep_url: bool = False):
        self.driver = driver
        self.url = url if url else self.APP_URL + self.PAGE_PATH

        if not keep_url:
            self.driver.get(self.url)

    def find_present_element(self, locator, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return element

    def find_present_elements(self, locator, timeout=TIMEOUT):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator), message=f"Not found: {locator}"
        )
        return elements

    def find_visible_element(self, locator, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return element

    def scroll_to_element(self, locator: WebElement | tuple[str, str], timeout=TIMEOUT):
        if isinstance(locator, tuple):
            element = self.find_present_element(locator, timeout)
        else:
            element = locator
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))

    def click_element(self, locator: WebElement | tuple[str, str], timeout=TIMEOUT):
        if isinstance(locator, tuple):
            element = self.find_present_element(locator, timeout)
        else:
            element = locator
        self.scroll_to_element(element)
        element.click()

    def fill_text_input(self, locator: WebElement | tuple[str, str], data: str, timeout=TIMEOUT):
        if isinstance(locator, tuple):
            element = self.find_present_element(locator, timeout)
        else:
            element = locator
        self.click_element(element)
        element.send_keys(data)

    def is_displayed(self, locator: WebElement | tuple[str, str], timeout=TIMEOUT):
        if isinstance(locator, tuple):
            element = self.find_present_element(locator, timeout)
        else:
            element = locator

        return element.is_displayed()

    def click_scooter_logo(self):
        self.click_element(L.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(L.YANDEX_LOGO)

    def click_header_order_button(self):
        self.click_element(L.HEADER_ORDER_BUTTON)

    def switch_to_next_window(self):
        current_window = self.driver.current_window_handle
        windows = self.driver.window_handles
        for w in windows:
            if w != current_window:
                self.driver.switch_to.window(w)
                break
            sleep(3)
