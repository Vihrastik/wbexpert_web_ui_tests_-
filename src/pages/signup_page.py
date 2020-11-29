from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.header import HeaderLocators
from src.pages.page import BasePage


class SignUpPageLocators:

    class SignUpPageHeader(HeaderLocators):
        ...

    class RegistrationBlock:
        block = (By.XPATH, '//div[./h1]', 'блок регистрации')

        title = (By.XPATH, '//h1[text()="Заявка на подключение"]', 'заголовок "Заявка на подключение"')
        recall_info = (By.XPATH, '//p[text()="Наш аналитик свяжется с вами и договорится о "]', 'текст "Наш аналитик свяжется с вами и договорится о "')
        name_text = (By.XPATH, '//label[text()="Как вас зовут?"]', 'подпись "Как вас зовут?"')
        name_input = (By.XPATH, '//input[@id="name"]', 'поле ввода "Как вас зовут?"')
        phone_text = (By.XPATH, '//label[text()="Ваш телефон"]', 'подпись "Ваш телефон"')
        phone_input = (By.XPATH, '//input[@id="phone"]', 'поле ввода "Ваш телефон"')
        offer_chbx = (By.XPATH, '//input[@type="checkbox"]', 'чекбокс "Я прочитал и принимаю (...)"')
        offer_chbx_text = (By.XPATH, '//label[@id="forcheckbox"]', 'текст "Я прочитал и принимаю (...)"')
        term_of_use_link = (By.XPATH, '//a[text()="Правила пользования Сайтом"]', 'ссылка "Правила пользования Сайтом"')
        privacy_link = (By.XPATH, '//a[text()="Политику конфиденциальности"]', 'ссылка "Политику конфиденциальности"')
        license_link = (By.XPATH, '//a[text()="Лицензионное соглашение"]', 'ссылка "Лицензионное соглашение"')
        submit_btn = (By.XPATH, '//button[@id="success-btn"]', 'кнопка "Дайте мне доступ"')

    class SuccessBlock:
        message = (By.XPATH, '//div[@class="alert alert-success"]', 'сообщение "Пользователь зарегистрирован. Пароль отправлен в СМС сообщении, Вы можете авторизоваться на сайте." и ссылка "Вернуться на главную страницу"')
        return_btn = (By.XPATH, '//p[@id="back"]/a', 'ссылка "Вернуться на главную страницу"')


class SignUpPage(BasePage):
    """
    Страница "Заявка на подключение".
    """
    def __init__(self, driver):
        super().__init__(driver, '/signup')

    def check_all_elements(self):
        self.wait_locator_displayed(SignUpPageLocators.RegistrationBlock.block)
        assert_that(self.is_locator_displayed(SignUpPageLocators.SignUpPageHeader.wb_logo_link),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.title),
                    'Не отображается заголовок "Заявка на подключение"')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.recall_info),
                    'Не отображается текст "Наш аналитик свяжется с вами и договорится о "')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.name_text),
                    'Не отображается текст "Как вас зовут?"')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.name_input),
                    'Не отображается инпут имени')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.phone_text),
                    'Не отображается текст "Ваш телефон"')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.phone_input),
                    'Не отображается инпут телефона')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.offer_chbx),
                    'Не отображается чекбокс согласия с политиками')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.offer_chbx_text),
                    'Не отображается текст Я прочитал и принимаю Правила пользования Сайтом, Лицензионное соглашение, '
                    'и Политику конфиденциальности')
        assert_that(self.is_locator_displayed(SignUpPageLocators.RegistrationBlock.submit_btn),
                    'Не отображается кнопка Дайте мне доступ')

    def fill_name_input_field(self, name: str):
        self.find_element(SignUpPageLocators.RegistrationBlock.name_input).send_keys(name)

    def fill_phone_input_field(self, phone: str):
        self.find_element(SignUpPageLocators.RegistrationBlock.phone_input).send_keys(phone)

    def click_submit_btn(self):
        self.find_element(SignUpPageLocators.RegistrationBlock.submit_btn).click()

    def is_error_displayed_in_phone_input(self) -> bool:
        return 'invalid' in self.find_element(SignUpPageLocators.RegistrationBlock.phone_input).get_attribute('class')

    def is_checkbox_red(self) -> bool:
        return ('color: rgb(220, 53, 69)' in
                self.find_element(SignUpPageLocators.RegistrationBlock.offer_chbx_text).get_attribute('style'))

    def register_user(self, name: str, phone: str):
        self.wait_locator_displayed(SignUpPageLocators.RegistrationBlock.block)
        self.fill_name_input_field(name=name)
        self.fill_phone_input_field(phone=phone)
        self.find_element(SignUpPageLocators.RegistrationBlock.offer_chbx).click()
        self.click_submit_btn()

    def check_success_block_elements(self):
        self.wait_locator_displayed(SignUpPageLocators.SuccessBlock.message)
        assert_that(self.is_locator_displayed(SignUpPageLocators.SuccessBlock.return_btn),
                    'Не отображается сообщение об успешной регистрации')

    def click_return_btn_in_success_block(self):
        self.find_element(SignUpPageLocators.SuccessBlock.return_btn).click()

    def click_term_of_use_link(self):
        self.find_element(SignUpPageLocators.RegistrationBlock.term_of_use_link).click()

    def click_privacy_link(self):
        self.find_element(SignUpPageLocators.RegistrationBlock.privacy_link).click()

    def click_license_link(self):
        self.find_element(SignUpPageLocators.RegistrationBlock.license_link).click()