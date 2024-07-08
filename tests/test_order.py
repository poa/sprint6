import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage, L
from tools import DataGenerator


class TestOrder:
    @pytest.mark.parametrize(
        "order_button,metro_station,color,lease",
        [
            # fmt: off
            pytest.param(
                "click_header_order_button", L.METRO_BUTTON_1, L.COLOR_BLACK, L.LEASE_1DAY,
                id="Make order with HEADER_ORDER_BUTTON, METRO_BUTTON_1",
            ),
            pytest.param(
                "click_home_order_button", L.METRO_BUTTON_9, L.COLOR_GRAY, L.LEASE_7DAY,
                id="Make order with HOME_ORDER_BUTTON, METRO_BUTTON_9",
            )
            # fmt: off
        ],
    )
    def test_order_successfully_created(self, driver, order_button, metro_station, color, lease):
        data = DataGenerator()
        home_page = HomePage(driver)
        home_page.__getattribute__(order_button)()
        page = OrderPage(driver, keep_url=True)

        # page one
        page.fill_text_input(L.FIRST_NAME_INPUT, data.first_name)
        page.fill_text_input(L.LAST_NAME_INPUT, data.last_name)
        page.fill_text_input(L.ADDRESS_INPUT, data.address)
        page.fill_text_input(L.PHONE_INPUT, data.phone)
        page.click_element(L.METRO_INPUT)
        page.click_element(metro_station)
        page.click_element(L.NEXT_BUTTON)

        # page two
        page.fill_text_input(L.START_DATE, data.date)
        page.click_element(L.START_DATE_SELECT)
        page.click_element(L.LEASE)
        page.click_element(lease)
        page.click_element(color)
        page.fill_text_input(L.COMMENT_INPUT, data.comment)
        page.click_element(L.MAKE_ORDER_BUTTON)

        # confirm page
        page.click_element(L.CONFIRM_BUTTON)

        assert page.is_displayed(L.ORDER_ACCEPTED) is True

