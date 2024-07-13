from selenium.webdriver.common.by import By

from data import TestData as TD
from pages.base_page import BasePage


class Locators:
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


class OrderPage(BasePage, Locators):
    PAGE_PATH = "/order"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
