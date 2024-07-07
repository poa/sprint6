import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.order_page import OrderPage, L
from tools import DataGenerator


class TestOrder:
    @pytest.mark.parametrize(
        "order_button,metro_station,color,lease",
        [
            # fmt: off
            pytest.param(
                L.HEADER_ORDER_BUTTON, L.METRO_BUTTON_1, L.COLOR_BLACK, L.LEASE_1DAY,
                id="Make order with HEADER_ORDER_BUTTON, METRO_BUTTON_1",
            ),
            pytest.param(
                L.BOTTOM_ORDER_BUTTON, L.METRO_BUTTON_9, L.COLOR_GRAY, L.LEASE_7DAY,
                id="Make order with BOTTOM_ORDER_BUTTON, METRO_BUTTON_9",
            )
            # fmt: off
        ],
    )
    def test_order_successfully_created(self, driver, order_button, metro_station, color, lease):
        page = OrderPage(driver, start_from_home=True)
        data = DataGenerator()
        page.click_element(order_button)
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

    def test_navigation_order_to_home(self, driver):
        page = OrderPage(driver)
        page.click_element(L.NAVI_LOGO)

        assert driver.current_url == page.APP_URL + HomePage.PAGE_PATH

    def test_navigation_yandex_to_dzen(self, driver):
        page = OrderPage(driver)
        page.click_element(L.NAVI_YANDEX)
        WebDriverWait(driver, page.TIMEOUT).until(EC.number_of_windows_to_be(2))
        current_window = driver.current_window_handle
        windows = driver.window_handles
        for w in windows:
            if w != current_window:
                driver.switch_to.window(w)
                break
            time.sleep(3)

        assert driver.current_url.startswith("https://dzen.ru/")
