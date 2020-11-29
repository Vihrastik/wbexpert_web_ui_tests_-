from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class AnalyticsPageLocators:

    class AnalyticsPageHeader(AuthorizedHeaderLocators):
        ...

    class FiltersBlock:
        date_text = (By.XPATH, '//span[@id="cnt_days"]', 'текст "Данные за 30 дней" с указанием дат')
        date_from = (By.XPATH, '//input[@aria-label="Дата начала"]', 'текст Дата начала')
        date_to = (By.XPATH, '//input[@aria-label="Дата конца"]', 'текст Дата конца')
        find_by_text_btn = (By.XPATH, '//button[@id="open"]', 'кнопка "Поиск категории по тексту"')
        find_by_list_btn = (By.XPATH, '//button[@id="open_list"]', 'кнопка "Выбор категории из списка"')

    class Tabs:
        niche_analysis = (By.XPATH, '//a[text()="Анализ ниши"]', 'ссылка Анализ ниши')
        competitor_analysis = (By.XPATH, '//a[text()="Анализ конкурентов"]', 'ссылка Анализ конкурентов')
        breakdown_by_parameters = (By.XPATH, '//a[text()="Разбивка по параметрам"]', 'ссылка Разбивка по параметрам')


class AnalyticsPage(BasePage):
    """
    Страница "Аналитика".
    """
    def __init__(self, driver):
        super().__init__(driver, '/analytics/')

    def check_header_elements(self):
        self.wait_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.block)
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_payment_assert(self, is_assert_displayed: bool):
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.AnalyticsPageHeader.payment_assert_text),
                    equal_to(is_assert_displayed),
                    f'Отображение текста о необходимости оплаты в хедере - должно быть {is_assert_displayed}')

    def check_all_elements(self, is_assert_displayed: bool=False):
        self.check_header_elements()
        self.check_payment_assert(is_assert_displayed=is_assert_displayed)
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.FiltersBlock.date_text),
                    'Не отображается количество выбранных дней')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.FiltersBlock.date_from),
                    'Не отображается инпут ввода от')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.FiltersBlock.date_to),
                    'Не отображается инпут ввода до')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.FiltersBlock.find_by_text_btn),
                    'Не отображается кнопка "Поиск категории по тексту"')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.FiltersBlock.find_by_list_btn),
                    'Не отображается кнопка "Выбор категории из списка"')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.Tabs.niche_analysis),
                    'Не отображается таб "Анализ ниши"')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.Tabs.competitor_analysis),
                    'Не отображается таб "Анализ конкурентов"')
        assert_that(self.is_locator_displayed(AnalyticsPageLocators.Tabs.breakdown_by_parameters),
                    'Не отображается таб "Разбивка по параметрам"')
