import random
import string

from hamcrest import (
    assert_that,
    contains_string,
)

from src.common.consts import UserData
from src.common.contextmanagers import (
    wait_for_page_to_reload,
)
from src.pages.change_password_page import ChangePassPage
from src.pages.lk_page import LKPage
from src.pages.login_page import LoginPage


class TestLoginPage:

    def test_web_ui_9_check_auth_page_locators(self, browser):
        auth_page = LoginPage(browser)
        auth_page.open()
        auth_page.check_all_elements()

    def test_web_ui_10_check_auth_page_authorization(self, browser):
        auth_page = LoginPage(browser)
        auth_page.open()
        auth_page.log_in(browser=browser,
                         login=UserData.trial_tariff.value.login,
                         password=UserData.trial_tariff.value.password)
        assert_that(browser.current_url, contains_string(LKPage(browser).path),
                    'Страница "Личный кабинет" не открылась')

    def test_web_ui_11_auth_page_empty_field_error(self, browser):
        auth_page = LoginPage(browser)
        auth_page.open()
        auth_page.fill_login_field(login=UserData.trial_tariff.value.login)
        auth_page.click_submit_btn()
        assert_that(browser.current_url, contains_string(LoginPage(browser).path),
                    'Пользователь авторизован без пароля')

    def test_web_ui_12_auth_page_authorization_error(self, browser):
        auth_page = LoginPage(browser)
        auth_page.open()
        auth_page.fill_login_field(login=str(random.randint(9100000000, 9109999999)))
        auth_page.fill_password_field(password=''.join(random.choice(string.ascii_lowercase) for _ in range(5)))
        auth_page.click_submit_btn()
        assert_that(auth_page.is_error_msg_displayed(), 'Не отображается ошибка "Неверный телефон или пароль"')

    def test_web_ui_13_check_auth_page_change_pass_link(self, browser):
        auth_page = LoginPage(browser)
        auth_page.open()
        with wait_for_page_to_reload(browser):
            auth_page.click_forget_pass_btn()
        assert_that(browser.current_url, contains_string(ChangePassPage(browser).path),
                    'Страница "Новый пароль" не открылась')
