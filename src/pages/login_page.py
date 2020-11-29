from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.common.contextmanagers import (
    wait_for_page_to_reload,
)
from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class LoginPageLocators:

    class LoginPageHeader(HeaderLocators):
        ...

    class AuthBlock(Footer):
        title = (By.XPATH, '//h1[contains(text(), "Авторизация")]', 'заголовок Авторизация')
        form_block = (By.XPATH, '//form[@action="login"]', 'блок авторизации с телефоном и паролем')
        phone_text = (By.XPATH, '//label[@for="phone"]', 'текст Телефон')
        phone_input = (By.XPATH, '//input[@id="phone"]', 'инпут Пароль')
        pass_text = (By.XPATH, '//label[@for="password"]', 'текст Пароль')
        pass_input = (By.XPATH, '//input[@id="password"]', 'инпут Пароль')
        submit_btn = (By.XPATH, '//button[@type="submit"]', 'кнопка Войти')
        forget_pass_btn = (By.XPATH, '//button[@id="change"]', 'ссылка Забыли пароль?')

        error_msg = (By.XPATH, '//div[contains(text(), "Неверный телефон или пароль")]', 'ошибка "Неверный телефон или пароль"')


class LoginPage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/login')

    def check_all_elements(self):
        assert_that(self.is_locator_displayed(LoginPageLocators.LoginPageHeader.wb_logo_link),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.title),
                    'Не отображается заголовок "Авторизация"')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.phone_text),
                    'Не отображается текст "Телефон"')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.phone_input),
                    'Не отображается инпут для телефона')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.pass_text),
                    'Не отображается заголовок "Пароль"')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.pass_input),
                    'Не отображается инпут для пароля')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.submit_btn),
                    'Не отображается кнопка Войти')
        assert_that(self.is_locator_displayed(LoginPageLocators.AuthBlock.forget_pass_btn),
                    'Не отображается ссылка "Забыли пароль?"')

    def log_in(self, browser: WebDriver, login: str, password: str):
        self.wait_locator_displayed(LoginPageLocators.AuthBlock.form_block)
        self.fill_login_field(login)
        self.fill_password_field(password)
        with wait_for_page_to_reload(browser):
            self.click_submit_btn()

    def fill_login_field(self, login: str):
        self.find_element(LoginPageLocators.AuthBlock.phone_input).send_keys(login)

    def fill_password_field(self, password: str):
        self.find_element(LoginPageLocators.AuthBlock.pass_input).send_keys(password)

    def click_submit_btn(self):
        self.find_element(LoginPageLocators.AuthBlock.submit_btn).click()

    def is_error_msg_displayed(self) -> bool:
        return self.is_locator_displayed(LoginPageLocators.AuthBlock.error_msg)

    def click_forget_pass_btn(self):
        self.find_element(LoginPageLocators.AuthBlock.forget_pass_btn).click()
