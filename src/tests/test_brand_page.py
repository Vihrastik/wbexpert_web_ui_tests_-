from src.common.contextmanagers import (
    wait_for_new_window,
)
from src.pages.brand_pages.brand_page import BrandPage
from src.pages.brand_pages.brand_table_page import BrandTablePage


class TestBrandTablePage:

    def test_web_ui_47_check_brand_page_locators(self, auth_by_paid_tariff, browser):
        brand_page = BrandTablePage(browser)
        brand_page.open()
        brand_page.wait_preloader_to_hide()
        brand_page.check_all_elements(is_assert_displayed=False)

    def test_web_ui_48_check_brand_page_trial_message(self, auth_by_trial_tariff, browser):
        brand_page = BrandTablePage(browser)
        brand_page.open()
        brand_page.wait_preloader_to_hide()
        brand_page.check_all_elements(is_assert_displayed=True)

    def test_web_ui_58_check_brand_page_big_brand(self, auth_by_paid_tariff, browser):
        brand_table_page = BrandTablePage(browser)
        brand_table_page.open()
        brand_table_page.sort_down_brands_by_rise_amount_in_table()
        with wait_for_new_window(browser):
            brand_table_page.click_first_brand_in_table()
        brand_page = BrandPage(browser)
        brand_page.wait_preloader_to_hide()
        brand_page.check_brand_elements(is_assert_displayed=False)
