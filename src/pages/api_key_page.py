from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class ApiKeyPageLocators:

    class HowToGetApiHeader(AuthorizedHeaderLocators):
        ...

    class AddKeysBlock:
        keys_block = (By.XPATH, '//div[@id="add-control"]', 'блок api-ключи')
        title = (By.XPATH, '//h2[text()="Добавьте api-ключ в формате base64"]', 'заголовок "Добавьте api-ключ в формате base64"')
        key_input = (By.XPATH, '//input[@id="apikey-input"]', 'поле ввода api-ключ')
        add_btn = (By.XPATH, '//button[@id="apikey-add"]', 'кнопка Добавить')

    class UserKeysBlock:
        table = (By.XPATH, '//table[@id="apikey-list"]', 'таблица с добавленными ключами')


class ApiKeyPage(BasePage):
    """
    Страница "API-ключ".
    """
    def __init__(self, driver):
        super().__init__(driver, '/my/api_key/')

    def check_header_elements(self):
        self.wait_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.block)
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.HowToGetApiHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_all_elements(self):
        self.check_header_elements()
        self.wait_locator_displayed(ApiKeyPageLocators.AddKeysBlock.keys_block)
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.AddKeysBlock.title),
                    'Не отображается заголовок "Добавьте api-ключ в формате base64"')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.AddKeysBlock.key_input),
                    'Не отображается инпут ввода ключа')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.AddKeysBlock.add_btn),
                    'Не отображается кнопка Добавить')
        assert_that(self.is_locator_displayed(ApiKeyPageLocators.UserKeysBlock.table),
                    'Не отображается таблица с ключами')

    def add_new_api_key(self, api_key):
        self.find_element(ApiKeyPageLocators.AddKeysBlock.key_input).send_keys(api_key)
        self.find_element(ApiKeyPageLocators.AddKeysBlock.add_btn).click()
