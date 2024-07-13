import allure
import pytest
from unidecode import unidecode as translit

from data import TestData as TD
from pages.home_page import HomePage


@allure.suite(f"Testing home page (path={HomePage.PAGE_PATH})")
class TestHome:
    @allure.title("Testing FAQ section")
    @pytest.mark.parametrize(
        "question, answer",
        [
            pytest.param(e["question"], e["answer"], id=translit(e["question"]))
            for e in TD.important_questions
        ],
    )
    def test_faq_all_elements_are_correct(self, driver, question, answer) -> None:
        page = HomePage(driver)

        faq_element = page.get_faq_element_by_question(question)
        page.click_faq_element(faq_element)
        current_answer = page.get_faq_answer(faq_element)

        assert current_answer == answer
