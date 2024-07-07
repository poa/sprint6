from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

import pages.base_page
from pages.base_page import BasePage


class L(pages.base_page.L):
    """Locators class

    Contains locators for web elements for order page
    """
    # fmt: off
    NEXT_BUTTON         = (By.XPATH, "//div[starts-with(@class,'Order_NextButton')]//button")
    METRO_BUTTON_1      = (By.XPATH, "//button[starts-with(@class,'Order_SelectOption') and @value='1']")
    METRO_BUTTON_9      = (By.XPATH, "//button[starts-with(@class,'Order_SelectOption') and @value='9']")

    FIRST_NAME_INPUT    = (By.XPATH, "//input[starts-with(@placeholder,'* Имя')]")
    LAST_NAME_INPUT     = (By.XPATH, "//input[starts-with(@placeholder,'* Фамилия')]")
    ADDRESS_INPUT       = (By.XPATH, "//input[starts-with(@placeholder,'* Адрес')]")
    METRO_INPUT         = (By.XPATH, "//input[starts-with(@placeholder,'* Станция')]")
    PHOTO_INPUT         = (By.XPATH, "//input[starts-with(@placeholder,'* Телефон')]")
    # fmt: off


    pass


class TD:
    """TestData class

    Contains data used for testing for order page
    """

    pass


class OrderPage(BasePage):
    PAGE_PATH = "/order"

    def __init__(self, driver):
        url = self.APP_URL + BasePage.PAGE_PATH
        BasePage.__init__(self, driver, url=url)
        self.url = self.APP_URL + self.PAGE_PATH

    def click_order_button(self, locator):
        button = self.find_present_element(locator)
        self.scroll_to_element(button)
        button.click()
        
