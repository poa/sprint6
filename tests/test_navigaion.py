import allure
import pytest
from data import TestData as TD
from pages.home_page import HomePage
from pages.order_page import OrderPage


@allure.suite("Test navigation scenarios")
class TestNavigation:

    @allure.title("Open order page from home with big order button")
    def test_navigation_home_to_order_with_order_button(self, driver):
        page = HomePage(driver)
        page.click_order_button()
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.APP_URL + OrderPage.PAGE_PATH)

    @allure.title("Open order page from home with header order button")
    def test_navigation_home_to_order_with_header_order_button(self, driver):
        page = HomePage(driver)
        page.Header.click_order_button()
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.APP_URL + OrderPage.PAGE_PATH)
        
    @allure.title("Open home page from order page with scooter logo")
    def test_navigation_order_to_home_scooter_logo(self, driver):
        page = OrderPage(driver)
        page.Header.click_scooter_logo()
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.APP_URL + OrderPage.PAGE_PATH)

    @allure.title("Open Yandex.Dzen with yandex logo")
    def test_navigation_home_to_dzen_yandex_logo(self, driver):
        page = HomePage(driver)
        HomePage.Header.click_yandex_logo()
        page.switch_to_next_window()
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.YANDEX_LOGO_DESTINATION)
