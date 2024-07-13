from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData as TD
from tools import PageMethods as PM


class Locators:
    """Locators class

    Contains locators for web elements for base page
    """

    # fmt: off
    ORDER_BUTTON    = (By.XPATH, "//div[starts-with(@class,'Header_Header')]//button[text()='Заказать']")

    SCOOTER_LOGO    = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO     = (By.XPATH, "//img[@alt='Yandex']")

    # fmt: on


class HeaderComponent(Locators):

    @staticmethod
    def click_scooter_logo(driver):
        PM.click_element(driver, HeaderComponent.SCOOTER_LOGO)

    @staticmethod
    def click_yandex_logo(driver):
        PM.click_element(driver, HeaderComponent.YANDEX_LOGO)

    @staticmethod
    def click_header_order_button(driver):
        PM.click_element(driver, HeaderComponent.ORDER_BUTTON)

    @staticmethod
    def check_yandex_logo_action(driver):
        HeaderComponent.click_yandex_logo()
        PM.switch_to_next_window(driver)
        driver.wait.until()
    