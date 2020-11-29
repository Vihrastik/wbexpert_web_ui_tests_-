from hamcrest import assert_that
from selenium.webdriver.common.by import By

from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class TermsOfUsePageLocators:

    class TermsOfUsePageHeader(HeaderLocators):
        ...

    class DescriptionBlock:
        title = (By.XPATH, '//span[text()="Правила пользования сайтом WBexpert.ru"]', 'заголовок "Правила пользования сайтом WBexpert.ru"')
        text = (By.XPATH, '//ol', 'текст "Правила пользования сайтом WBexpert.ru"')

    class TermsOfUsePageFooter(Footer):
        ...


class TermsOfUsePage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/docs/offer')

    def check_all_elements(self):

        self.wait_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageHeader.block)
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageHeader.tariffs_btn),
                    'Не отображается кнопка Тарифов')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageHeader.come_in_btn),
                    'Не отображается кнопка Войти')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageHeader.registration_btn),
                    'Не отображается кнопка Регистрация')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.DescriptionBlock.title),
                    'Не отображается заголовок "Правила пользования сайтом WBexpert.ru"')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.DescriptionBlock.text),
                    'Не отображаются блоки текста')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageFooter.wb_logo_text),
                    'Не отображается логотип в футере')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageFooter.terms_of_use),
                    'Не отображается "Пользовательское соглашение"')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageFooter.license_agreement),
                    'Не отображается "Лицензионное соглашение"')
        assert_that(self.is_locator_displayed(TermsOfUsePageLocators.TermsOfUsePageFooter.privacy_policy),
                    'Не отображается "Политика конфиденциальности"')
