import allure
import pytest
from data import TestData as TD
from pages.home_page import HomePage
from pages.home_page import Locators as HPLoc
from pages.order_page import OrderPage
from pages.components import Locators as HeaderLoc


@allure.suite("Test navigation scenarios")
class TestNavigation:

    @allure.title("Open order page from home with order button")
    @pytest.mark.parametrize(
        "order_button",
        [
            pytest.param(HPLoc.ORDER_BUTTON, id="Home page order button"),
            pytest.param(HeaderLoc.ORDER_BUTTON, id="Header order button"),
        ],
    )
    def test_navigation_home_to_order_with_order_button(self, driver, order_button):
        allure.dynamic.title(f"Open order page from home with {order_button}")
        page = HomePage(driver)
        page.open_page()
        page.click_order_button(order_button)
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.APP_URL + OrderPage.PAGE_PATH)

    @allure.title("Open home page from order page with scooter logo")
    def test_navigation_order_to_home_with_scooter_logo(self, driver):
        page = OrderPage(driver)
        page.open_page()
        page.Header.click_scooter_logo()
        page_current_url = page.get_current_url()

        assert page_current_url.startswith(TD.APP_URL + HomePage.PAGE_PATH)

    @allure.title("Open Yandex.Dzen with yandex logo")
    def test_navigation_home_to_dzen_yandex_logo(self, driver):
        page = HomePage(driver)
        page.open_page()
        page.Header.click_yandex_logo()

        assert page.Header.check_zen_page_opened() is True
