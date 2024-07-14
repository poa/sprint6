import allure
import pytest

from pages.components import Locators as HeaderLoc
from pages.home_page import HomePage
from pages.home_page import Locators as HPLoc
from pages.order_page import OrderPage
from tools import DataGenerator


@allure.suite("Test order process suite")
class TestOrder:
    @pytest.mark.parametrize(
        "order_button",
        [
            pytest.param(HPLoc.ORDER_BUTTON, id="Home page order button"),
            pytest.param(HeaderLoc.ORDER_BUTTON, id="Header order button"),
        ],
    )
    def test_order_successfully_created(self, driver, order_button):
        allure.dynamic.title(f"Test order process for {order_button}")

        data = DataGenerator()
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        home_page.open_page()
        home_page.click_order_button(order_button)

        # page one
        order_page.fill_first_order_page(
            first_name=data.first_name,
            last_name=data.last_name,
            address=data.address,
            phone=data.phone,
            metro_station=data.metro_station,
        )
        order_page.click_next_button()

        # page two
        order_page.fill_second_order_page(
            date=data.date,
            lease=data.lease_period,
            color=data.scooter_color,
            comment=data.comment,
        )
        order_page.click_maker_order_button()

        # confirm page
        order_page.click_confirm_button()

        assert order_page.check_order_acceptance() is True
