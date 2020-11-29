import random
import string

import pytest
from hamcrest import (
    assert_that,
    contains_string,
)

from src.common.contextmanagers import (
    wait_for_page_to_reload,
    wait_for_new_window,
)
from src.pages.docs.license_page import LicensePage
from src.pages.docs.privacy_policy_page import PrivacyPolicyPage
from src.pages.docs.terms_of_use_page import TermsOfUsePage
from src.pages.main_page import MainPage
from src.pages.signup_page import SignUpPage


class TestSignUpPage:

    def test_web_ui_17_check_registration_page_locators(self, browser):
        signup_page = SignUpPage(browser)
        signup_page.open()
        signup_page.check_all_elements()

    def test_web_ui_18_registration_page_empty_field_error(self, browser):
        signup_page = SignUpPage(browser)
        signup_page.open()
        signup_page.fill_name_input_field(name=''.join(random.choice(string.ascii_lowercase) for _ in range(5)))
        signup_page.fill_phone_input_field(phone='')
        signup_page.click_submit_btn()
        assert_that(signup_page.is_error_displayed_in_phone_input(),
                    'Не отображается восклицательный знак у незаполненого поля')

    def test_web_ui_19_registration_page_docs_chbx_unchecked(self, browser):
        signup_page = SignUpPage(browser)
        signup_page.open()
        signup_page.fill_name_input_field(name=''.join(random.choice(string.ascii_lowercase) for _ in range(5)))
        signup_page.fill_phone_input_field(phone=str(random.randint(9100000000, 9109999999)))
        signup_page.click_submit_btn()
        assert_that(signup_page.is_checkbox_red(), 'Текст чекбокса не красный')

    def test_web_ui_20_check_registration_page_success_reg(self, browser):
        signup_page = SignUpPage(browser)
        signup_page.open()
        signup_page.register_user(name='Test', phone=str(random.randint(9900000000, 9909999999)))
        signup_page.check_success_block_elements()
        with wait_for_page_to_reload(browser):
            signup_page.click_return_btn_in_success_block()
        assert_that(browser.current_url, contains_string(MainPage(browser).path), 'Главная страница не открылась')

    @pytest.mark.skip
    def test_web_ui_21_check_registration_page_links(self, browser):
        signup_page = SignUpPage(browser)
        signup_page.open()
        with wait_for_new_window(browser):
            signup_page.click_term_of_use_link()
        assert_that(browser.current_url, contains_string(TermsOfUsePage(browser).path),
                    'Страница "Правила пользования Сайтом" не открылась')
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        with wait_for_new_window(browser):
            signup_page.click_license_link()
        assert_that(browser.current_url, contains_string(LicensePage(browser).path),
                    'Страница "Лицензионное соглашение" не открылась')
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        with wait_for_new_window(browser):
            signup_page.click_privacy_link()
        assert_that(browser.current_url, contains_string(PrivacyPolicyPage(browser).path),
                    'Страница "Политику конфиденциальности" не открылась')
