import allure
from selenium.webdriver.common.by import By

from tools import PageMethods as PM


class Locators:
    """Locators class

    Contains locators for web elements for base page
    """

    # fmt: off
    ORDER_BUTTON    = (By.XPATH, "//div[starts-with(@class,'Header_Header')]//button[text()='Заказать']")

    SCOOTER_LOGO    = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO     = (By.XPATH, "//img[@alt='Yandex']")
    ZEN_PAGE_SIGN   = (By.XPATH, "//html[starts-with(@class, 'zen-page')]")

    # fmt: on


class HeaderComponent(Locators):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Click scooter logo")
    def click_scooter_logo(self):
        PM.click_element(self.driver, HeaderComponent.SCOOTER_LOGO)

    @allure.step("Click yandex logo")
    def click_yandex_logo(self):
        PM.click_element(self.driver, HeaderComponent.YANDEX_LOGO)

    @allure.step("Click header order button")
    def click_order_button(self):
        PM.click_element(self.driver, HeaderComponent.ORDER_BUTTON)

    @allure.step("Check Zen page is open")
    def check_zen_page_opened(self):
        PM.switch_to_next_window(self.driver)
        return PM.is_displayed(self.driver, HeaderComponent.ZEN_PAGE_SIGN)
