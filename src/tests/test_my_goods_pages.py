from src.pages.api_key_page import ApiKeyPage
from src.pages.my_raiting_page import MyRatingPage
from src.pages.my_sales_page import MySalesPage
from src.pages.my_storage_page import MyStoragePage
from src.pages.my_table_page import MyTablePage


class TestMyTablePage:

    def test_web_ui_53_check_my_table_page_locators(self, auth_by_trial_tariff, browser):
        my_table_page = MyTablePage(browser)
        my_table_page.open()
        my_table_page.wait_preloader_to_hide()
        my_table_page.check_all_elements()


class TestMySalesPage:

    def test_web_ui_54_check_my_sales_page_locators(self, auth_by_trial_tariff, browser):
        my_sales_page = MySalesPage(browser)
        my_sales_page.open()
        my_sales_page.wait_preloader_to_hide()
        my_sales_page.check_all_elements()
        my_sales_page.click_common_tab()
        my_sales_page.check_common_tab()
        my_sales_page.click_brand_tab()
        my_sales_page.check_brand_tab()
        my_sales_page.click_category_tab()
        my_sales_page.check_category_tab()


class TestMyStoragePage:

    def test_web_ui_55_check_my_storage_page_locators(self, auth_by_trial_tariff, browser):
        my_storage_page = MyStoragePage(browser)
        my_storage_page.open()
        my_storage_page.wait_preloader_to_hide()
        my_storage_page.check_all_elements()


class TestMyRatingPage:

    def test_web_ui_56_check_my_rating_page_locators(self, auth_by_trial_tariff, browser):
        my_rating_page = MyRatingPage(browser)
        my_rating_page.open()
        my_rating_page.wait_preloader_to_hide()
        my_rating_page.check_all_elements()
        my_rating_page.click_common_tab()
        my_rating_page.check_common_tab()
        my_rating_page.click_competitors_tab()
        my_rating_page.click_competitors_tab()
        my_rating_page.click_dynamics_tab()
        my_rating_page.check_dynamics_tab()


class TestApiKeyPage:

    def test_web_ui_57_check_my_api_key_page_locators(self, auth_by_trial_tariff, browser):
        api_key_page = ApiKeyPage(browser)
        api_key_page.open()
        api_key_page.wait_preloader_to_hide()
        api_key_page.check_all_elements()
