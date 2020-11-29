from hamcrest import (
    assert_that,
    contains_string,
    equal_to,
)

from src.common.contextmanagers import (
    wait_for_page_to_reload,
)
from src.common.funcs import (
    get_callable_phone,
    get_callable_email,
)
from src.pages.analytics_page import AnalyticsPage
from src.pages.api_key_page import ApiKeyPage
from src.pages.brand_pages.brand_table_page import BrandTablePage
from src.pages.howto_get_api_page import HowToGetApiPage
from src.pages.lk_page import LKPage
from src.pages.main_page import MainPage
from src.pages.my_raiting_page import MyRatingPage
from src.pages.my_sales_page import MySalesPage
from src.pages.my_storage_page import MyStoragePage
from src.pages.my_table_page import MyTablePage
from src.pages.novelty_page import NoveltyPage
from src.pages.payment_page import PaymentPage
from src.pages.product_page import ProductPage


class TestLKPage:

    def test_web_ui_25_check_lk_page_locators(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.check_all_elements()

    def test_web_ui_26_check_lk_page_get_api_key(self, auth_by_paid_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_how_to_get_api_link()
        assert_that(browser.current_url, contains_string(HowToGetApiPage(browser).path),
                    'Страница "Как получить API-ключ?" не открылась')

    def test_web_ui_27_check_lk_page_enter_api_key(self, auth_by_paid_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_api_link()
        assert_that(browser.current_url, contains_string(ApiKeyPage(browser).path),
                    'Страница "API-ключ" не открылась')

    def test_web_ui_28_check_lk_trial_page_open_demo(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_demo_link()
        assert_that(browser.current_url, contains_string(AnalyticsPage(browser).path),
                    'Страница "Аналитика" не открылась')

    def test_web_ui_29_check_lk_trial_page_pay(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_payment_link()
        assert_that(browser.current_url, contains_string(PaymentPage(browser).path),
                    'Страница оплаты не открылась')

    def test_web_ui_30_check_lk_page_whats_upp(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_whatsapp_link()
        assert_that(browser.current_url, contains_string('api.whatsapp.com/send?phone=79955016154'),
                    'Страница whatsapp не открылась')

    def test_web_ui_31_check_lk_page_telegram(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_telegram_link()
        assert_that(browser.current_url, contains_string('t.me/solomonangry'),
                    'Страница t.me/solomonangry не открылась')

    def test_web_ui_32_check_lk_page_email(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.click_email_link()
        assert_that(get_callable_email(browser), equal_to('mailto:ask@wbexpert.ru'), 'Вызываемый email отличается')

    def test_web_ui_33_check_lk_page_tel(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.click_phone_link()
        assert_that(get_callable_phone(browser), equal_to('tel:79955016154'), 'Вызываемый номер отличается')

    def test_web_ui_34_check_lk_page_exit(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        with wait_for_page_to_reload(browser):
            lk_page.click_exit_btn()
        main_page = MainPage(browser)
        assert_that(browser.current_url, contains_string(main_page.path),
                    'Главная страница не открылась')
        main_page.check_header()

    def test_web_ui_35_check_lk_page_analytics(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_analysis_from_analysis_dropdown()
        assert_that(browser.current_url, contains_string(AnalyticsPage(browser).path),
                    'Страница "Аналитика" не открылась')

    def test_web_ui_36_check_lk_page_brand(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_brands_from_analysis_dropdown()
        assert_that(browser.current_url, contains_string(BrandTablePage(browser).path),
                    'Страница "Бренд" не открылась')

    def test_web_ui_37_check_lk_page_product(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_product_from_analysis_dropdown()
        assert_that(browser.current_url, contains_string(ProductPage(browser).path),
                    'Страница "Товары" не открылась')

    def test_web_ui_38_check_lk_page_new(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_new_from_analysis_dropdown()
        assert_that(browser.current_url, contains_string(NoveltyPage(browser).path),
                    'Страница "Новинки" не открылась')

    def test_web_ui_39_check_lk_page_table(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_table_from_products_dropdown()
        assert_that(browser.current_url, contains_string(MyTablePage(browser).path),
                    'Страница "Сводная" не открылась')

    def test_web_ui_40_check_lk_page_sales(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_selling_from_products_dropdown()
        assert_that(browser.current_url, contains_string(MySalesPage(browser).path),
                    'Страница "Продажи" не открылась')

    def test_web_ui_41_check_lk_page_storage(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_store_from_products_dropdown()
        assert_that(browser.current_url, contains_string(MyStoragePage(browser).path),
                    'Страница "Склад" не открылась')

    def test_web_ui_42_check_lk_page_rating(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_rating_from_products_dropdown()
        assert_that(browser.current_url, contains_string(MyRatingPage(browser).path),
                    'Страница "Рейтинг" не открылась')

    def test_web_ui_43_check_lk_page_my_api_keys(self, auth_by_trial_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.open_api_key_from_products_dropdown()
        assert_that(browser.current_url, contains_string(ApiKeyPage(browser).path),
                    'Страница "API-ключ" не открылась')

    def test_web_ui_44_check_lk_page_paid_info(self, auth_by_paid_tariff, browser):
        lk_page = LKPage(browser)
        lk_page.check_success_payment(date_to='до 30 декабря 2020 23:59 MSK')
