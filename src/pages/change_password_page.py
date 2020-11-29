from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class ChangePassPageLocators:

    class ChangePassPageHeader(HeaderLocators):
        ...

    class ChangePassBlock:
        title = (By.XPATH, '//h1[contains(text(), "Новый пароль")]', 'заголовок "Новый пароль"')
        form_block = (By.XPATH, '//form[@action="change"]', 'блок с телефоном')
        phone_text = (By.XPATH, '//label[@for="phone"]', 'текст Телефон')
        phone_input = (By.XPATH, '//input[@id="phone"]', 'поле Телефон')
        get_new_btn = (By.XPATH, '//button[@class="btn btn-primary"]', 'кнопка "Получить новый пароль"')
        remember_btn = (By.XPATH, '//button[@class="btn btn-link"]', 'ссылка "Вспомнил"')


class ChangePassPage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/change')

    def check_all_elements(self):
        self.wait_locator_displayed(ChangePassPageLocators.ChangePassBlock.form_block)
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassPageHeader.wb_logo_link),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassBlock.title),
                    'Не отображается заголовок "Новый пароль"')
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassBlock.phone_text),
                    'Не отображается текст "Телефон"')
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassBlock.phone_input),
                    'Не отображается инпут телефона')
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassBlock.get_new_btn),
                    'Не отображается кнопка Получить новый пароль')
        assert_that(self.is_locator_displayed(ChangePassPageLocators.ChangePassBlock.remember_btn),
                    'Не отображается кнопка Вспомнил')

    def click_get_new_btn(self):
        self.find_element(ChangePassPageLocators.ChangePassBlock.get_new_btn).click()

    def click_remember_btn(self):
        self.find_element(ChangePassPageLocators.ChangePassBlock.remember_btn).click()

    def enter_new_password(self, phone: str):
        self.find_element(ChangePassPageLocators.ChangePassBlock.phone_input).send_keys(phone)
        self.click_get_new_btn()
