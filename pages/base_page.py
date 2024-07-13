import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData as TD
from pages.components import HeaderComponent
from tools import PageMethods as PM


class BasePage:
    PAGE_PATH = "/"

    Header = HeaderComponent

    def __init__(self, driver):
        self.driver = driver
        self.page_url = TD.APP_URL + self.PAGE_PATH
        PM.open_page(driver, self.page_url)

    def get_current_url(self):
        return PM.get_current_url(self.driver)

    @allure.step("Switch to next tab")
    def switch_to_next_window(self):
        PM.switch_to_next_window(self.driver)
