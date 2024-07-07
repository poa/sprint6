import pytest

from pages.order_page import OrderPage, L
from tools import DataGenerator


class TestOrder:
    @pytest.mark.parametrize(
        "order_button,metro_station",
        [
            pytest.param(L.HEADER_ORDER_BUTTON, L.METRO_1, id="Make order with HEADER_ORDER_BUTTON"),
            pytest.param(L.BOTTOM_ORDER_BUTTON, L.METRO_2,  id="Make order with BOTTOM_ORDER_BUTTON"),
        ],
    )
    def test_order_successfully_created(self, driver, order_button, metro_station):
        page = OrderPage(driver)
        data = DataGenerator()
        page.click_order_button(order_button)
