import pytest
from unidecode import unidecode as translit

from pages.home_page import HomePage, TD


class TestHome:
    @pytest.mark.parametrize(
        "question, answer",
        [pytest.param(e["q"], e["a"], id=translit(e["q"])) for e in TD.important_questions],
    )
    def test_faq_all_elements_are_correct(self, driver, question, answer) -> None:
        page = HomePage(driver)
        faq_element = page.get_faq_element_by_question(question)
        page.scroll_to_element(faq_element)
        page.click_faq_element(faq_element)
        assert page.get_faq_answer(faq_element).text == answer


