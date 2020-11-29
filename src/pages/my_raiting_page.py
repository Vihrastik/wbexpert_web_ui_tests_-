from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.common_table import CommonTableElements
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class CommonTableHeaders:
    search = 'Поиск'
    my_goods = 'Мои товары'
    all_goods = 'Все товары'
    my_brands = 'Мои бренды'
    all_brands = 'Все бренды'
    my_rating = 'Мой рейтинг'
    week_changes = 'Изменение за неделю'
    month_changes = 'Изменение за месяц'
    dynamics = 'Динамика рейтинга'
    top_good = 'Топ товар'
    top_good_position = 'Позиция топ товара'
    photo = 'Фото товара'


class MyRatingPageLocators:

    class MyRatingPageHeader(AuthorizedHeaderLocators):
        ...

    class Filters:
        filters_block = (By.XPATH, '//div[@class="row"]', 'блок фильтров')
        title = (By.XPATH, '//h1[text()="Мои позиции"]', 'заголовок Мои позиции')

        brands_text = (By.XPATH, '//span[text()="Бренды:"]', 'текст Бренды')
        brands_all_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="все"]]', 'ссылка Бренды все')
        brands_choose_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="выбрать"]]', 'ссылка Бренды выбрать')

        categories_text = (By.XPATH, '//span[text()="Категории:"]', 'текст Категории')
        categories_all_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="все"]]', 'ссылка Категории все')
        categories_choose_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="выбрать"]]', 'ссылка Категории выбрать')

        download_text = (By.XPATH, '//span[text()="Скачать"]', 'текст Скачать')
        download_xls = (By.XPATH, '//button[@id="download_xls"]', 'кнопка xls')
        download_csv = (By.XPATH, '//button[@id="download_csv"]', 'кнопка csv')

    class MyRatingTabs:
        common_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//a[text()="Сводная"]', 'таб Сводная')
        competitors_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//a[text()="Мои конкуренты"]', 'таб Мои конкуренты')
        dynamics_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//a[text()="Динамика"]', 'таб Динамика')

    class CommonTable(CommonTableElements):
        ...

    class CompetitorsTable:
        table = (By.XPATH, '//div[@id="concurency_div"]/table', 'таблица Мои конкуренты')

    class DynamicsTable:
        dynamics_block = (By.XPATH, '//div[./div[@id="concurent_selector"]]', 'блок динамики')
        select_input = (By.XPATH, '//input[@id="concurent_selector"]', 'поле выбора динамики')
        graph_position_per_days = (By.XPATH, '//div[./div[@id="concurent_selector"]]//div[@class="dash-graph"][1]', 'Позиция в рейтинге по дням')
        graph_rating_per_days = (By.XPATH, '//div[./div[@id="concurent_selector"]]//div[@class="dash-graph"][2]', 'Рейтинг по дням')


class MyRatingPage(BasePage):
    """
    Страница "Мои позиции".
    """
    def __init__(self, driver):
        super().__init__(driver, '/my/rating/')

    def check_header_elements(self):
        self.wait_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.block)
        assert_that(self.is_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.MyRatingPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_filters(self):
        self.wait_locator_displayed(MyRatingPageLocators.Filters.filters_block)
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.title),
                    'Не отображается заголовок "Мои склад"')

        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.brands_text),
                    'Не отображается текст "Бренды:"')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.brands_all_btn),
                    'Не отображается кнопка бренды все')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.brands_choose_btn),
                    'Не отображается кнопка бренды выбрать')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.categories_text),
                    'Не отображается текст "Категории:"')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.categories_all_btn),
                    'Не отображается кнопка категории все')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.categories_choose_btn),
                    'Не отображается кнопка категории выбрать')

        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.download_text),
                    'Не отображается текст "Скачать"')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.download_csv),
                    'Не отображается кнопка скачать csv')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.Filters.download_xls),
                    'Не отображается кнопка скачать xls')

    def check_all_elements(self):
        self.check_header_elements()
        self.check_filters()

    def click_common_tab(self):
        self.find_element(MyRatingPageLocators.MyRatingTabs.common_tab).click()

    def click_competitors_tab(self):
        self.find_element(MyRatingPageLocators.MyRatingTabs.competitors_tab).click()

    def click_dynamics_tab(self):
        self.find_element(MyRatingPageLocators.MyRatingTabs.dynamics_tab).click()

    def check_common_tab(self):
        self.wait_locator_displayed(MyRatingPageLocators.CommonTable.block)
        titles_texts_common = [t.text for t in self.find_elements(MyRatingPageLocators.CommonTable.header_item)]
        assert_that(titles_texts_common,
                    equal_to([CommonTableHeaders.search,
                              CommonTableHeaders.my_goods,
                              CommonTableHeaders.all_goods,
                              CommonTableHeaders.my_brands,
                              CommonTableHeaders.all_brands,
                              CommonTableHeaders.my_rating,
                              CommonTableHeaders.week_changes,
                              CommonTableHeaders.month_changes,
                              CommonTableHeaders.dynamics,
                              CommonTableHeaders.top_good,
                              CommonTableHeaders.top_good_position,
                              CommonTableHeaders.photo,
                              ]), 'Отображаются не все заголовки таблицы')
        assert_that(len(self.find_elements(MyRatingPageLocators.CommonTable.filter_item)), equal_to(12),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(MyRatingPageLocators.CommonTable.data_item), 'Нет данных в таблице')

    def check_competitors_tab(self):
        self.wait_locator_displayed(MyRatingPageLocators.CompetitorsTable.table)

    def check_dynamics_tab(self):
        self.wait_locator_displayed(MyRatingPageLocators.DynamicsTable.dynamics_block)
        assert_that(self.is_locator_displayed(MyRatingPageLocators.DynamicsTable.select_input),
                    'Не отображается инпут поиска')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.DynamicsTable.graph_position_per_days),
                    'Не отображается график Позиция в рейтинге по дням')
        assert_that(self.is_locator_displayed(MyRatingPageLocators.DynamicsTable.graph_rating_per_days),
                    'Не отображается график Рейтинг по дням')
