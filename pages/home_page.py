import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from tools import PageMethods as PM


class Locators:
    """Locators class

    Contains locators for web elements
    """

    # fmt: off
    ORDER_BUTTON = (
    By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]//button[text()='Заказать']")

    FAQ_LIST = (By.XPATH, "//div[starts-with(@class, 'Home_FAQ')]//div[@class='accordion__item']")
    FAQ_ELEMENT_BY_QUESTION = (By.XPATH,
                               "//div[starts-with(@class, 'Home_FAQ')]//div[@class='accordion__item' and .//div[text()='%s']]")
    FAQ_ELEMENT_ANSWER = (By.XPATH, ".//div[@class='accordion__panel']")
    FAQ_ELEMENT_BUTTON = (By.XPATH, ".//*[@class='accordion__button']")
    # fmt: on


class HomePage(BasePage, Locators):
    PAGE_PATH = "/"

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Get FAQ element by {question}")
    def get_faq_element_by_question(self, question):
        faq_element = PM.find_present_element(
            self.driver,
            (self.FAQ_ELEMENT_BY_QUESTION[0], self.FAQ_ELEMENT_BY_QUESTION[1] % question),
        )
        return faq_element

    @allure.step("Click to FAQ element")
    def click_faq_element(self, faq_element):
        PM.scroll_to_element(faq_element)
        PM.click_element(self.driver, faq_element.find_element(*self.FAQ_ELEMENT_BUTTON))

    @allure.step("Get FAQ element answer text")
    def get_faq_answer(self, faq_element):
        answer_element = faq_element.find_element(*self.FAQ_ELEMENT_ANSWER)
        return answer_element.text

    @allure.step("Click Order button on Home page")
    def click_order_button(self):
        PM.click_element(self.driver, self.ORDER_BUTTON)
