import random

from hamcrest import (
    assert_that,
    contains_string,
)

from src.common.contextmanagers import (
    wait_for_page_to_reload,
)
from src.pages.change_password_page import ChangePassPage
from src.pages.login_page import LoginPage


class TestChangePassPage:

    def test_web_ui_22_check_change_pass_page_locators(self, browser):
        change_pass_page = ChangePassPage(browser)
        change_pass_page.open()
        change_pass_page.check_all_elements()

    def test_web_ui_23_check_change_pass_page_cancel_link(self, browser):
        change_pass_page = ChangePassPage(browser)
        change_pass_page.open()
        with wait_for_page_to_reload(browser):
            change_pass_page.click_remember_btn()
        assert_that(browser.current_url, contains_string(LoginPage(browser).path),
                    'Страница "Авторизация" не открылась')

    def test_web_ui_24_change_pass_page_success_change(self, browser):
        change_pass_page = ChangePassPage(browser)
        change_pass_page.open()
        with wait_for_page_to_reload(browser):
            change_pass_page.enter_new_password(phone=str(random.randint(9900000000, 9909999999)))
        assert_that(browser.current_url, contains_string(LoginPage(browser).path),
                    'Страница "Авторизация" не открылась')
