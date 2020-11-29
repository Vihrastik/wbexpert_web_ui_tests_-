from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class LicensePageLocators:

    class LicensePageHeader(HeaderLocators):
        ...

    class DescriptionBlock:
        title = (By.XPATH, '//span[text()="Лицензионное соглашение WBexpert.ru"]', 'заголовок "Лицензионное соглашение WBexpert.ru"')
        text = (By.XPATH, '//ol', 'текст "Лицензионное соглашение WBexpert.ru"')

    class LicensePageFooter(Footer):
        ...


class LicensePage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/docs/license')

    def check_all_elements(self):
        self.wait_locator_displayed(LicensePageLocators.LicensePageHeader.block)
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageHeader.tariffs_btn),
                    'Не отображается кнопка Тарифов')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageHeader.come_in_btn),
                    'Не отображается кнопка Войти')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageHeader.registration_btn),
                    'Не отображается кнопка Регистрация')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(LicensePageLocators.DescriptionBlock.title),
                    'Не отображается заголовок "Лицензионное соглашение WBexpert.ru"')
        assert_that(self.is_locator_displayed(LicensePageLocators.DescriptionBlock.text),
                    'Не отображаются блоки текста')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageFooter.wb_logo_text),
                    'Не отображается логотип в футере')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageFooter.terms_of_use),
                    'Не отображается "Пользовательское соглашение"')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageFooter.license_agreement),
                    'Не отображается "Лицензионное соглашение"')
        assert_that(self.is_locator_displayed(LicensePageLocators.LicensePageFooter.privacy_policy),
                    'Не отображается "Политика конфиденциальности"')
