from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class MainPageLocators:

    class MainPageHeader(HeaderLocators):
        ...

    class DescriptionBlock:
        title = (By.XPATH, '//span[text()="Аналитика для увеличения продаж на Wildberries"]', 'заголовок "Аналитика для увеличения продаж на Wildberries"')
        advert_text = (By.XPATH, '//span[text()="Каждый день собираем продажи по всем"]', 'текст "Каждый день собираем продажи по всем"')
        advert_list = (By.XPATH, '//div[./div[text()="С помощью сервиса вы сможете"]]', 'текст "С помощью сервиса вы сможете"')
        advert_img = (By.XPATH, '//div[contains(@class, "desktopimg") and .//div[@role="img" and contains(@aria-label, "С помощью сервиса")]]', 'картинка с примером')

    class IntentionBlock:
        title = (By.XPATH, '//h2[text()="А совсем скоро..."]', 'заголовок "А совсем скоро..."')
        products_analytics = (By.XPATH, '//div[./div/div[text()="Аналитика своих товаров"]]', 'блок "Аналитика своих товаров"')
        competitor_monitoring = (By.XPATH, '//div[./div/div[text()="Мониторинг конкурентов"]]', 'блок "Мониторинг конкурентов"')

    class VideoBlock:
        video = (By.XPATH, '//div[contains(@class, "video")]', 'видео')

    class TariffsBlock:
        tariff_info = (By.XPATH, '//div[text()="15 тыс. руб. в месяц"]', 'текст "15 тыс. руб. в месяц"')
        options_text = (By.XPATH, '//div[./div[contains(text(), "Безлимитный доступ к сервису")]]', 'текст "Безлимитный доступ к сервису"')
        try_btn = (By.XPATH, '//a[text()="Попробовать бесплатно"]', 'кнопка Попробовать бесплатно')

    class MainPageFooter(Footer):
        ...


class MainPage(BasePage):
    """
    Главная страница.
    """
    def check_all_elements(self):
        self.check_header()
        assert_that(self.is_locator_displayed(MainPageLocators.DescriptionBlock.title),
                    'Не отображается заголовок "Аналитика для увеличения продаж на Wildberries"')
        assert_that(self.is_locator_displayed(MainPageLocators.DescriptionBlock.advert_text),
                    'Не отображается текст "Каждый день собираем продажи по всем"')
        assert_that(self.is_locator_displayed(MainPageLocators.DescriptionBlock.advert_list),
                    'Не отображается список "С помощью сервиса вы сможете"')
        assert_that(self.is_locator_displayed(MainPageLocators.DescriptionBlock.advert_img),
                    'Не отображается скриншот описания')
        assert_that(self.is_locator_displayed(MainPageLocators.IntentionBlock.title),
                    'Не отображается заголовок "А совсем скоро..."')
        assert_that(self.is_locator_displayed(MainPageLocators.IntentionBlock.products_analytics),
                    'Не отображается список "Аналитика своих товаров"')
        assert_that(self.is_locator_displayed(MainPageLocators.IntentionBlock.competitor_monitoring),
                    'Не отображается список "Мониторинг конкурентов"')
        assert_that(self.is_locator_displayed(MainPageLocators.VideoBlock.video),
                    'Не отображается видео с описанием')
        assert_that(self.is_locator_displayed(MainPageLocators.TariffsBlock.tariff_info),
                    'Не отображается тариф "15 тыс. руб. в месяц"')
        assert_that(self.is_locator_displayed(MainPageLocators.TariffsBlock.options_text),
                    'Не отображается текст "Безлимитный доступ к сервису"')
        assert_that(self.is_locator_displayed(MainPageLocators.TariffsBlock.try_btn),
                    'Не отображается кнопка "Попробовать бесплатно"')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageFooter.wb_logo_text),
                    'Не отображается логотип в футере')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageFooter.terms_of_use),
                    'Не отображается "Пользовательское соглашение"')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageFooter.license_agreement),
                    'Не отображается "Лицензионное соглашение"')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageFooter.privacy_policy),
                    'Не отображается "Политика конфиденциальности"')

    def check_header(self):
        self.wait_locator_displayed(MainPageLocators.MainPageHeader.block)
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageHeader.tariffs_btn),
                    'Не отображается кнопка Тарифов')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageHeader.come_in_btn),
                    'Не отображается кнопка Войти')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageHeader.registration_btn),
                    'Не отображается кнопка Регистрация')
        assert_that(self.is_locator_displayed(MainPageLocators.MainPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')

    def click_on_tarifs_in_header(self):
        self.find_element(MainPageLocators.MainPageHeader.tariffs_btn).click()

    def get_tarifs_location(self):
        return self.find_element(MainPageLocators.MainPageHeader.tariffs_btn).location.values()

    def click_on_come_in_btn_in_header(self):
        self.find_element(MainPageLocators.MainPageHeader.come_in_btn).click()

    def click_on_registration_btn_in_header(self):
        self.find_element(MainPageLocators.MainPageHeader.registration_btn).click()

    def click_on_try_btn_in_tariffs_block(self):
        self.find_element(MainPageLocators.TariffsBlock.try_btn).click()

    def click_on_terms_of_use_in_footer(self):
        self.find_element(MainPageLocators.MainPageFooter.terms_of_use).click()

    def click_on_license_agreement_in_footer(self):
        self.find_element(MainPageLocators.MainPageFooter.license_agreement).click()

    def click_on_privacy_policy_in_footer(self):
        self.find_element(MainPageLocators.MainPageFooter.privacy_policy).click()