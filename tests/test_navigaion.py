import pytest
from pages.base_page import TD as BasePageTD
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestNavigation:

    @pytest.mark.parametrize(
        "order_button", ["click_header_order_button", "click_home_order_button"]
    )
    def test_navigation_home_to_order(self, driver, order_button):
        page = HomePage(driver)
        page.__getattribute__(order_button)()

        assert driver.current_url == page.APP_URL + OrderPage.PAGE_PATH

    def test_navigation_order_to_home_scooter_logo(self, driver):
        page = OrderPage(driver)
        page.click_scooter_logo()

        assert driver.current_url == page.APP_URL + HomePage.PAGE_PATH

    def test_navigation_home_to_dzen_yandex_logo(self, driver):
        page = HomePage(driver)
        page.click_yandex_logo()
        page.switch_to_next_window()

        assert driver.current_url.startswith(BasePageTD.YANDEX_LOGO_DST)
