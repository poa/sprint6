import allure
import pytest

from pages.components import Locators as HeaderLoc
from pages.home_page import HomePage
from pages.home_page import Locators as HPLoc
from pages.order_page import OrderPage
from pages.order_page import Locators as OPLoc
from tools import DataGenerator


@allure.suite("Test order process suite")
class TestOrder:
    @allure.title("Test order process")
    @pytest.mark.parametrize(
        "order_button,metro_station,color,lease",
        [
            # fmt: off
            pytest.param(
                HPLoc.ORDER_BUTTON, OPLoc.METRO_BUTTON_1, OPLoc.COLOR_BLACK, OPLoc.LEASE_1DAY,
                id="Make order with HEADER_ORDER_BUTTON, METRO_BUTTON_1",
            ),
            pytest.param(
                HeaderLoc.ORDER_BUTTON, OPLoc.METRO_BUTTON_9, OPLoc.COLOR_GRAY, OPLoc.LEASE_7DAY,
                id="Make order with HOME_ORDER_BUTTON, METRO_BUTTON_9",
            ),
            # fmt: off
        ],
    )
    def test_order_successfully_created(self, driver, order_button, metro_station, color, lease):
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
            metro_station=metro_station,
        )
        order_page.click_next_button()

        # page two
        order_page.fill_second_order_page(
            date=data.date,
            lease=lease,
            color=color,
            comment=data.comment,
        )
        order_page.click_maker_order_button()

        # confirm page
        order_page.click_confirm_button()

        assert order_page.check_order_acceptance() is True

