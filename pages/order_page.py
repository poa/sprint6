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
    # first order page
    FIRST_NAME_INPUT    = (By.XPATH, "//input[starts-with(@placeholder,'* Имя')]")
    LAST_NAME_INPUT     = (By.XPATH, "//input[starts-with(@placeholder,'* Фамилия')]")
    ADDRESS_INPUT       = (By.XPATH, "//input[starts-with(@placeholder,'* Адрес')]")
    METRO_INPUT         = (By.XPATH, "//input[starts-with(@placeholder,'* Станция')]")
    PHONE_INPUT         = (By.XPATH, "//input[starts-with(@placeholder,'* Телефон')]")
    METRO_BUTTON_1      = (By.XPATH, "//button[starts-with(@class,'Order_SelectOption') and @value='1']")
    METRO_BUTTON_9      = (By.XPATH, "//button[starts-with(@class,'Order_SelectOption') and @value='9']")
    NEXT_BUTTON         = (By.XPATH, "//div[starts-with(@class,'Order_NextButton')]//button")

    # second order page
    START_DATE          = (By.XPATH, "//input[starts-with(@placeholder,'* Когда')]")
    START_DATE_SELECT   = (By.XPATH, "//div[contains(@class,'react-datepicker__day--selected')]")
    LEASE               = (By.XPATH, "//div[@class='Dropdown-control']")
    LEASE_1DAY          = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    LEASE_7DAY          = (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")
    COLOR_BLACK         = (By.ID, "black")
    COLOR_GRAY          = (By.ID, "grey")
    COMMENT_INPUT       = (By.XPATH, "//input[starts-with(@placeholder,'Комментарий')]")

    MAKE_ORDER_BUTTON   = (By.XPATH, "//div[starts-with(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON      = (By.XPATH, "//div[starts-with(@class,'Order_Buttons')]//button[text()='Да']")

    # success page
    ORDER_ACCEPTED      = (By.XPATH, f"//div[starts-with(@class,'Order_ModalHeader') and text()='Заказ оформлен']")
    STATUS_BUTTON       = (By.XPATH, "//div[starts-with(@class,'Order_NextButton')]//button")
    # fmt: on


class OrderPage(BasePage):
    PAGE_PATH = "/order"

    def __init__(self, driver, start_from_home=False):
        url = self.APP_URL + (BasePage.PAGE_PATH if start_from_home else self.PAGE_PATH)
        BasePage.__init__(self, driver, url=url)
        self.url = self.APP_URL + self.PAGE_PATH
