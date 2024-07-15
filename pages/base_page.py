import allure

from selenium.webdriver.common.by import By

from data import TestData as TD
from pages.components import HeaderComponent
from tools import PageMethods as PM

class Locators:
    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")


class BasePage(Locators):
    PAGE_PATH = "/"

    def __init__(self, driver):
        self.driver = driver
        self.Header = HeaderComponent(self.driver)
        self.page_url = TD.APP_URL + self.PAGE_PATH

    @allure.step("Open page")
    def open_page(self):
        PM.open_page(self.driver, self.page_url)

        if PM.is_displayed(self.driver, self.ACCEPT_COOKIE_BUTTON):
            PM.click_element(self.driver, self.ACCEPT_COOKIE_BUTTON)

    @allure.step("Get current url")
    def get_current_url(self):
        return PM.get_current_url(self.driver)
