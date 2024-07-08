from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import pages.base_page
from pages.base_page import BasePage


class TD:
    """TestData class

    Contains data used for testing home page
    """

    # fmt: off
    important_questions = [
        {"q": "Сколько это стоит? И как оплатить?",
         "a": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
         },
        {"q": "Хочу сразу несколько самокатов! Так можно?",
         "a": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
         },
        {"q": "Как рассчитывается время аренды?",
         "a": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
         },
        {"q": "Можно ли заказать самокат прямо на сегодня?",
         "a": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
         },
        {"q": "Можно ли продлить заказ или вернуть самокат раньше?",
         "a": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
         },
        {"q": "Вы привозите зарядку вместе с самокатом?",
         "a": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
         },
        {"q": "Можно ли отменить заказ?",
         "a": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
         },
        {"q": "Я жизу за МКАДом, привезёте?",
         "a": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
         },
    ]
    # fmt: on


class L(pages.base_page.L):
    """Locators class

    Contains locators for web elements
    """

    # fmt: off
    HOME_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Home_FinishButton')]//button[text()='Заказать']")

    FAQ_LIST = (By.XPATH, "//div[starts-with(@class, 'Home_FAQ')]//div[@class='accordion__item']")
    FAQ_ELEMENT_BY_QUESTION = (By.XPATH, "//div[starts-with(@class, 'Home_FAQ')]//div[@class='accordion__item' and .//div[text()='%s']]")
    FAQ_ELEMENT_ANSWER = (By.XPATH, ".//div[@class='accordion__panel']")
    FAQ_ELEMENT_BUTTON = (By.XPATH, ".//*[@class='accordion__button']")
    # fmt: on


class HomePage(BasePage):
    PAGE_PATH = "/"

    def __init__(self, driver, keep_url=False):
        self.url = self.APP_URL + self.PAGE_PATH
        BasePage.__init__(self, driver, url=self.url, keep_url=keep_url)

    def get_faq_elements(self):
        faq_elements = self.find_present_elements(L.FAQ_LIST)
        return faq_elements

    def get_faq_element_by_question(self, question):
        faq_element = self.find_present_element(
            (L.FAQ_ELEMENT_BY_QUESTION[0], L.FAQ_ELEMENT_BY_QUESTION[1] % question)
        )

        return faq_element

    @staticmethod
    def get_faq_answer(faq_element: WebElement):
        answer = faq_element.find_element(*L.FAQ_ELEMENT_ANSWER)
        return answer

    def click_faq_element(self, faq_element: WebElement):
        self.scroll_to_element(faq_element)
        self.click_element(faq_element.find_element(*L.FAQ_ELEMENT_BUTTON))

    def click_home_order_button(self):
        self.click_element(L.HOME_ORDER_BUTTON)
