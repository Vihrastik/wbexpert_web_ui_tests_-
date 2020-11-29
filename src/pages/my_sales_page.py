from hamcrest import (
    assert_that,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class MySalesPageLocators:

    class MySalesPageHeader(AuthorizedHeaderLocators):
        ...

    class Filters:
        filters_block = (By.XPATH, '//div[@class="row"]', 'блок фильтров')
        title = (By.XPATH, '//h1[text()="Мои продажи"]', 'заголовок "Мои продажи"')

        period_text = (By.XPATH, '//span[text()="Период:"]', 'текст Период')
        period_7_btn = (By.XPATH, '//button[@id="week"]', 'линк Период: 7 дней')
        period_14_btn = (By.XPATH, '//button[@id="2week"]', 'линк Период: 14 дней')
        period_30_btn = (By.XPATH, '//button[@id="month"]', 'линк Период: 30 дней')
        period_60_btn = (By.XPATH, '//button[@id="2month"]', 'линк Период: 60 дней')
        period_choose_btn = (By.XPATH, '//button[@id="custom"]', 'линк Период: выбрать')

        brands_text = (By.XPATH, '//span[text()="Бренды:"]', 'текст Бренды')
        brands_all_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="все"]]', 'линк Бренды все')
        brands_choose_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="выбрать"]]', 'линк Бренды выбрать')

        categories_text = (By.XPATH, '//span[text()="Категории:"]', 'текст Категории')
        categories_all_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="все"]]', 'линк Категории все')
        categories_choose_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="выбрать"]]', 'линк Категории выбрать')

        collapse_text = (By.XPATH, '//div[text()="Схлопнуть:"]', 'текст Схлопнуть')
        collapse_colors_chbx = (By.XPATH, '//input[@id="root"]', 'линк Схлопнуть: Цвета')
        collapse_measure_chbx = (By.XPATH, '//input[@id="size"]', 'линк Схлопнуть: Размеры')
        collapse_stores_chbx = (By.XPATH, '//input[@id="warehouse"]', 'линк Схлопнуть: Склады')

        download_text = (By.XPATH, '//span[text()="Скачать"]', 'текст Скачать')
        download_xls = (By.XPATH, '//button[@id="download_xls"]', 'кнопка xls')
        download_csv = (By.XPATH, '//button[@id="download_csv"]', 'кнопка csv')

    class SaleTabs:
        common_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//li[contains(@class, "nav-item")]/a[text()="Сводка"]', 'таб Сводка')
        brand_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//li[contains(@class, "nav-item")]/a[text()="Бренды"]', 'таб Бренды')
        category_tab = (By.XPATH, '//ul[contains(@class, "tabs")]//li[contains(@class, "nav-item")]/a[text()="Категории"]', 'таб Категории')

    class CommonInfo:
        common_block = (By.XPATH, '//div[@class="tab-content" and .//p[@class="summary_line"]]', 'блок Сводка')
        title = (By.XPATH, '//p[@class="summary_line"]', 'заголовок Продано N товаров на N рублей')
        graph = (By.XPATH, '//div[.//p[@class="summary_line"]]/div[@class="dash-graph"]', 'график продаж выручки по дням')
        table = (By.XPATH, '//div[@class="myItems prettyTable"]', 'таблица с товарами')

    class BrandInfo:
        brand_block = (By.XPATH, '//div[@id="brand_div"]', 'блок Бренд')
        table = (By.XPATH, '//div[@id="brand_div"]/div[@class="prettyTable"]', 'таблица с вкладышами Бренд, Продажи, Выручка')
        graph_sales_per_days = (By.XPATH, '//div[@id="brand_div"]/div[@class="dash-graph"][1]', 'график Продажи брендов по дням')
        graph_revenue_per_days = (By.XPATH, '//div[@id="brand_div"]/div[@class="dash-graph"][2]', 'график выручка брендов по дням')

    class CategoryInfo:
        category_block = (By.XPATH, '//div[@id="category_div"]', 'блок Категории')
        table = (By.XPATH, '//div[@id="category_div"]/div[@class="prettyTable"]', 'таблица с вкладышами Категории, Продажи, Выручка')
        graph_sales_per_days = (By.XPATH, '//div[@id="category_div"]/div[@class="dash-graph"][1]', 'график Продажи категорий по дням')
        graph_revenue_per_days = (By.XPATH, '//div[@id="category_div"]/div[@class="dash-graph"][2]', 'график выручка категорий по дням')


class MySalesPage(BasePage):
    """
    Страница "Мои продажи".
    """
    def __init__(self, driver):
        super().__init__(driver, '/my/sales/')

    def check_header_elements(self):
        self.wait_locator_displayed(MySalesPageLocators.MySalesPageHeader.block)
        assert_that(self.is_locator_displayed(MySalesPageLocators.MySalesPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(MySalesPageLocators.MySalesPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(MySalesPageLocators.MySalesPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(MySalesPageLocators.MySalesPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(MySalesPageLocators.MySalesPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_filters(self):
        self.wait_locator_displayed(MySalesPageLocators.Filters.filters_block)
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.title),
                    'Не отображается заголовок "Мои продажи"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_text),
                    'Не отображается текст Период')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_7_btn),
                    'Не отображается кнопка Период 7 дней')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_14_btn),
                    'Не отображается кнопка Период 14 дней')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_30_btn),
                    'Не отображается кнопка Период 30 дней')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_60_btn),
                    'Не отображается кнопка Период 60 дней')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.period_choose_btn),
                    'Не отображается кнопка Период выбрать')

        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.brands_text),
                    'Не отображается текст "Бренды:"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.brands_all_btn),
                    'Не отображается кнопка бренды все')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.brands_choose_btn),
                    'Не отображается кнопка бренды выбрать')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.categories_text),
                    'Не отображается текст "Категории:"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.categories_all_btn),
                    'Не отображается кнопка категории все')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.categories_choose_btn),
                    'Не отображается кнопка категории выбрать')

        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.collapse_text),
                    'Не отображается текст "Схлопнуть:"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.collapse_colors_chbx),
                    'Не отображается чекбокс схлопнуть цвета')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.collapse_measure_chbx),
                    'Не отображается чекбокс схлопнуть размеры')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.collapse_stores_chbx),
                    'Не отображается чекбокс схлопнуть склады')

        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.download_text),
                    'Не отображается текст "Скачать"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.download_csv),
                    'Не отображается кнопка скачать csv')
        assert_that(self.is_locator_displayed(MySalesPageLocators.Filters.download_xls),
                    'Не отображается кнопка скачать xls')

    def check_all_elements(self):
        self.check_header_elements()
        self.check_filters()

    def click_common_tab(self):
        self.find_element(MySalesPageLocators.SaleTabs.common_tab).click()

    def click_brand_tab(self):
        self.find_element(MySalesPageLocators.SaleTabs.brand_tab).click()

    def click_category_tab(self):
        self.find_element(MySalesPageLocators.SaleTabs.category_tab).click()

    def check_common_tab(self):
        self.wait_locator_displayed(MySalesPageLocators.CommonInfo.common_block)
        assert_that(self.is_locator_displayed(MySalesPageLocators.CommonInfo.title),
                    'Не отображается заголовок "Продано _ товаров на _ рублей"')
        assert_that(self.is_locator_displayed(MySalesPageLocators.CommonInfo.graph),
                    'Не отображается график продаж и выручки по дням')
        assert_that(self.is_locator_displayed(MySalesPageLocators.CommonInfo.table),
                    'Не отображается таблица продуктов с Сводке')

    def check_brand_tab(self):
        self.wait_locator_displayed(MySalesPageLocators.BrandInfo.brand_block)
        assert_that(self.is_locator_displayed(MySalesPageLocators.BrandInfo.table),
                    'Не отображается таблица брендов')
        assert_that(self.is_locator_displayed(MySalesPageLocators.BrandInfo.graph_sales_per_days),
                    'Не отображается график продажи брендов по дням')
        assert_that(self.is_locator_displayed(MySalesPageLocators.BrandInfo.graph_revenue_per_days),
                    'Не отображается график выручки брендов по дням')

    def check_category_tab(self):
        self.wait_locator_displayed(MySalesPageLocators.CategoryInfo.category_block)
        assert_that(self.is_locator_displayed(MySalesPageLocators.CategoryInfo.table),
                    'Не отображается таблица с категориями')
        assert_that(self.is_locator_displayed(MySalesPageLocators.CategoryInfo.graph_sales_per_days),
                    'Не отображается график продажи категорий по дням')
        assert_that(self.is_locator_displayed(MySalesPageLocators.CategoryInfo.graph_revenue_per_days),
                    'Не отображается график выручки категорий по дням')
