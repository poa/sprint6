import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tools import PageMethods as PM


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
    METRO_ITEM          = (By.XPATH, "//button[starts-with(@class,'Order_SelectOption')]//div[text()='%s']/..")
    NEXT_BUTTON         = (By.XPATH, "//div[starts-with(@class,'Order_NextButton')]//button")

    # second order page
    START_DATE          = (By.XPATH, "//input[starts-with(@placeholder,'* Когда')]")
    START_DATE_SELECT   = (By.XPATH, "//div[contains(@class,'react-datepicker__day--selected')]")
    LEASE               = (By.XPATH, "//div[@class='Dropdown-control']")
    LEASE_ITEM          = (By.XPATH, "//div[@class='Dropdown-option' and text()='%s']")
    SCOOTER_COLOR       = (By.ID, "%s")
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

    @allure.step("Fill first page: person data")
    def fill_first_order_page(self, first_name, last_name, address, phone, metro_station):
        PM.fill_text_input(self.driver, self.FIRST_NAME_INPUT, first_name)
        PM.fill_text_input(self.driver, self.LAST_NAME_INPUT, last_name)
        PM.fill_text_input(self.driver, self.ADDRESS_INPUT, address)
        PM.fill_text_input(self.driver, self.PHONE_INPUT, phone)
        PM.click_element(self.driver, self.METRO_INPUT)
        PM.click_element(self.driver, (self.METRO_ITEM[0], self.METRO_ITEM[1] % metro_station))

    @allure.step("Click Next button on first order page")
    def click_next_button(self):
        PM.click_element(self.driver, self.NEXT_BUTTON)

    @allure.step("Fill first two: scooter data")
    def fill_second_order_page(self, date, lease, color, comment):
        PM.fill_text_input(self.driver, self.START_DATE, date)
        PM.click_element(self.driver, self.START_DATE_SELECT)
        PM.click_element(self.driver, self.LEASE)
        PM.click_element(self.driver, (self.LEASE_ITEM[0], self.LEASE_ITEM[1] % lease))
        PM.click_element(self.driver, (self.SCOOTER_COLOR[0], self.SCOOTER_COLOR[1] % color))
        PM.fill_text_input(self.driver, self.COMMENT_INPUT, comment)

    @allure.step("Click Make order button on second order page")
    def click_maker_order_button(self):
        PM.click_element(self.driver, self.MAKE_ORDER_BUTTON)

    @allure.step("Click Confirm button on last order page")
    def click_confirm_button(self):
        PM.click_element(self.driver, self.CONFIRM_BUTTON)

    @allure.step("Check order acceptance status")
    def check_order_acceptance(self):
        return PM.is_displayed(self.driver, self.ORDER_ACCEPTED)
