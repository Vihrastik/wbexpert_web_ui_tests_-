from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.footer import Footer
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class LKPagePageLocators:

    class LKPageHeader(AuthorizedHeaderLocators):
        ...

    class ServicesBlock:
        title = (By.XPATH, '//h1[text()="Доступ к сервисам"]', 'заголовок "Доступ к сервисам"')
        products_info_row = (By.XPATH, '//div[contains(@class, "row") and .//*[text()="Мои товары"]]', 'сервис Мои товары')
        api_link = (By.XPATH, '//div[contains(@class, "row")]//a[@href="/my/api_key/"]', 'ссылка "API-ключ"')
        how_to_get_api_link = (By.XPATH, '//a[@href="https://wbexpert.ru/howto/api-key"]', 'ссылка "Как получить API-ключ?"')
        analysis_info_row = (By.XPATH, '//div[contains(@class, "row") and .//*[text()="Конкурентный анализ"]]', 'сервис Конкурентный анализ')
        demo_link = (By.XPATH, '//a[@href="/analytics"]', 'ссылка "демо-данным"')
        payment_link = (By.XPATH, '//a[@href="/payment"]', 'ссылка "Оплатить картой"')

        full_access_text = (By.XPATH, '//span[@class="text-success"]', 'текст о полном доступе')
        access_date_text = (By.XPATH, '//div[./span[@class="text-success"]]/div', 'дата полного доступа')

    class ContactsBlock:
        whatsapp_link = (By.XPATH, '//div[contains(@class, "row")]/div/div//a[contains(@href, "whatsapp")]', 'ссылка WhatsApp')
        telegram_link = (By.XPATH, '//div[contains(@class, "row")]/div/div//a[contains(@href, "t.me")]', 'ссылка Telegram')
        email_link = (By.XPATH, '//div[contains(@class, "row")]/div/div//a[contains(@href, "ask@wbexpert.ru")]', 'ссылка E-mail')
        phone_link = (By.XPATH, '//div[contains(@class, "row")]/div/div//a[contains(@href, "tel")]', 'ссылка Телефон')

    class LKPageFooter(Footer):
        email_link = (By.XPATH, '//footer//a[contains(@href, "ask@wbexpert.ru")]', 'ссылка email в футере')
        phone_link = (By.XPATH, '//footer//*[text()="+7(995)501-61-54"]', 'ссылка контакты в футере')


class LKPage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/lk')

    def check_all_elements(self):
        self.wait_locator_displayed(LKPagePageLocators.LKPageHeader.block)
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageHeader.phone),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ServicesBlock.title),
                    'Не отображается заголовок "Доступ к сервисам"')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ServicesBlock.products_info_row),
                    'Не отображается блок "Мои товары"')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ServicesBlock.analysis_info_row),
                    'Не отображается блок "Конкурентный анализ"')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ContactsBlock.whatsapp_link),
                    'Не отображается whatsapp')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ContactsBlock.telegram_link),
                    'Не отображается telegram')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ContactsBlock.email_link),
                    'Не отображается email')
        assert_that(self.is_locator_displayed(LKPagePageLocators.ContactsBlock.phone_link),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.wb_logo_text),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.email_link),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.phone_link),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.terms_of_use),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.license_agreement),
                    'Не отображается телефон')
        assert_that(self.is_locator_displayed(LKPagePageLocators.LKPageFooter.privacy_policy),
                    'Не отображается телефон')

    def click_how_to_get_api_link(self):
        self.find_element(LKPagePageLocators.ServicesBlock.how_to_get_api_link).click()

    def click_api_link(self):
        self.find_element(LKPagePageLocators.ServicesBlock.api_link).click()

    def click_demo_link(self):
        self.find_element(LKPagePageLocators.ServicesBlock.demo_link).click()

    def click_payment_link(self):
        self.find_element(LKPagePageLocators.ServicesBlock.payment_link).click()

    def click_whatsapp_link(self):
        self.find_element(LKPagePageLocators.ContactsBlock.whatsapp_link).click()

    def click_telegram_link(self):
        self.find_element(LKPagePageLocators.ContactsBlock.telegram_link).click()

    def click_email_link(self):
        self.find_element(LKPagePageLocators.ContactsBlock.email_link).click()

    def click_phone_link(self):
        self.find_element(LKPagePageLocators.ContactsBlock.phone_link).click()

    def click_exit_btn(self):
        self.find_element(LKPagePageLocators.LKPageHeader.exit_btn).click()

    def open_analysis_from_analysis_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.analysis_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.analysis).click()

    def open_brands_from_analysis_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.analysis_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.brands).click()

    def open_product_from_analysis_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.analysis_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.products).click()

    def open_new_from_analysis_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.analysis_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.new).click()

    def open_table_from_products_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.products_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.table).click()

    def open_selling_from_products_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.products_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.selling).click()

    def open_store_from_products_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.products_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.store).click()

    def open_rating_from_products_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.products_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.rating).click()

    def open_api_key_from_products_dropdown(self):
        self.find_element(LKPagePageLocators.LKPageHeader.products_dropdown).click()
        self.find_element(LKPagePageLocators.LKPageHeader.api_key).click()

    def check_success_payment(self, date_to):
        assert_that(self.is_locator_displayed(LKPagePageLocators.ServicesBlock.full_access_text),
                    'Не отображается текст "полный доступ"')
        date_text = self.find_element(LKPagePageLocators.ServicesBlock.access_date_text)
        assert_that(date_text.text, equal_to(date_to), 'Не совпадает текст окончания оплаты')
