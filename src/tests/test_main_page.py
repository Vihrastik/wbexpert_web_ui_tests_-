from hamcrest import (
    assert_that,
    contains_string,
)

from src.common.contextmanagers import (
    wait_for_new_window,
    wait_for_page_to_reload,
)
from src.common.funcs import wait_in_view
from src.pages.docs.license_page import LicensePage
from src.pages.docs.privacy_policy_page import PrivacyPolicyPage
from src.pages.docs.terms_of_use_page import TermsOfUsePage
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.pages.signup_page import SignUpPage


class TestMainPage:

    def test_web_ui_1_check_main_page_locators(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.check_all_elements()

    def test_web_ui_2_check_main_page_price(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_on_tarifs_in_header()
        wait_in_view(main_page.get_tarifs_location(), browser.get_window_position(), browser.get_window_size())

    def test_web_ui_3_check_main_page_auth_link(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_page_to_reload(browser):
            main_page.click_on_come_in_btn_in_header()
        assert_that(browser.current_url, contains_string(LoginPage(browser).path), 'Страница логина не открылась')

    def test_web_ui_4_check_main_page_registration_link(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_page_to_reload(browser):
            main_page.click_on_registration_btn_in_header()
        assert_that(browser.current_url, contains_string(SignUpPage(browser).path), 'Страница авторизации не открылась')

    def test_web_ui_5_check_main_page_try_free_link(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_page_to_reload(browser):
            main_page.click_on_try_btn_in_tariffs_block()
        assert_that(browser.current_url, contains_string(SignUpPage(browser).path), 'Страница авторизации не открылась')

    def test_web_ui_6_check_main_page_terms_of_use(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_new_window(browser):
            main_page.click_on_terms_of_use_in_footer()
        assert_that(browser.current_url, contains_string(TermsOfUsePage(browser).path),
                    'Страница "Пользовательское соглашение" не открылась')

    def test_web_ui_7_check_main_page_license(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_new_window(browser):
            main_page.click_on_license_agreement_in_footer()
        assert_that(browser.current_url, contains_string(LicensePage(browser).path),
                    'Страница "Лицензионное соглашение" не открылась')

    def test_web_ui_8_check_main_page_confidentiality(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        with wait_for_new_window(browser):
            main_page.click_on_privacy_policy_in_footer()
        assert_that(browser.current_url, contains_string(PrivacyPolicyPage(browser).path),
                    'Страница "Политика конфиденциальности" не открылась')
