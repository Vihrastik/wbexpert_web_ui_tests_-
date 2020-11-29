from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class PrivacyPolicyPageLocators:

    class PrivacyPolicyPageHeader(HeaderLocators):
        ...

    class DescriptionBlock:
        title = (By.XPATH, '//span[text()="Политика конфиденциальности WBexpert.ru"]', 'заголовок "Политика конфиденциальности WBexpert.ru"')
        text = (By.XPATH, '//ol', 'текст "Политика конфиденциальности WBexpert.ru"')

    class PrivacyPolicyPageFooter(Footer):
        ...


class PrivacyPolicyPage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/docs/privacy')

    def check_all_elements(self):
        self.wait_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageHeader.block)
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageHeader.tariffs_btn),
                    'Не отображается кнопка Тарифов')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageHeader.come_in_btn),
                    'Не отображается кнопка Войти')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageHeader.registration_btn),
                    'Не отображается кнопка Регистрация')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.DescriptionBlock.title),
                    'Не отображается заголовок "Политика конфиденциальности WBexpert.ru"')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.DescriptionBlock.text),
                    'Не отображаются блоки текста')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageFooter.wb_logo_text),
                    'Не отображается логотип в футере')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageFooter.terms_of_use),
                    'Не отображается "Пользовательское соглашение"')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageFooter.license_agreement),
                    'Не отображается "Лицензионное соглашение"')
        assert_that(self.is_locator_displayed(PrivacyPolicyPageLocators.PrivacyPolicyPageFooter.privacy_policy),
                    'Не отображается "Политика конфиденциальности"')
