import allure
import pytest
from unidecode import unidecode as translit

from data import TestData as TD
from pages.home_page import HomePage


@allure.suite(f"Test home page FAQ section")
class TestHome:
    @pytest.mark.parametrize(
        "question, answer",
        [
            pytest.param(elem["question"], elem["answer"], id=translit(elem["question"]))
            for elem in TD.important_questions
        ],
    )
    def test_faq_all_elements_are_correct(self, driver, question, answer) -> None:
        allure.dynamic.title(f"Question: {question}")
        page = HomePage(driver)

        page.open_page()
        page.click_question(question)

        assert page.check_answer(question, answer)
