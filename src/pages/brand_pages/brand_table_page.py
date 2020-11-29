from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.common_table import CommonTableElements
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class BrandTablePageLocators:

    class BrandPageHeader(AuthorizedHeaderLocators):
        ...

    class BrandsTable(CommonTableElements):
        title = (By.XPATH, '//h1[text()="Выберите бренд для рассмотрения"]', 'заголовок "Выберите бренд для рассмотрения"')

        table = (By.XPATH, '//table', 'таблица брендов')

        brand_title = (By.XPATH, '//span[text()="Бренд"]', 'заголовок "Бренд"')
        brand_filter = (By.XPATH, '//tr[2]//th[1]/input[@placeholder="filter data..."]', 'фильтры для "Бренд"')
        product_amount_title = (By.XPATH, '//span[text()="Кол-во товаров"]', 'заголовок "Кол-во товаров"')
        product_amount_sort_down = (By.XPATH, '//th[2]//*[contains(@data-icon, "sort")]', 'сортировка для "Кол-во товаров"')
        product_filter = (By.XPATH, '//tr[2]//th[2]/input[@placeholder="filter data..."]', 'фильтры для "Кол-во товаров"')
        sales_title = (By.XPATH, '//span[text()="Продаж за 30 дней"]', 'заголовок "Продаж за 30 дней"')
        sales_filter = (By.XPATH, '//tr[2]//th[3]/input[@placeholder="filter data..."]', 'фильтры для "Продаж за 30 дней"')
        money_title = (By.XPATH, '//span[text()="Выручка за 30 дней"]', 'заголовок "Выручка за 30 дней"')
        money_filter = (By.XPATH, '//tr[2]//th[4]/input[@placeholder="filter data..."]', 'фильтры для "Выручка за 30 дней"')

        brand_cell = (By.XPATH, '//td[@tabindex]//a[@href]', 'клетка в таблице "Выберите бренд для рассмотрения" для бренда')
        brand_amount = (By.XPATH, '//tr[./td[@tabindex and .//a[@href]]]//td[2]/div', 'клетка в таблице "Выберите бренд для рассмотрения" для количества')
        brand_sales = (By.XPATH, '//tr[./td[@tabindex and .//a[@href]]]//td[3]/div', 'клетка в таблице "Выберите бренд для рассмотрения" для продаж')
        brand_money = (By.XPATH, '//tr[./td[@tabindex and .//a[@href]]]//td[4]/div', 'клетка в таблице "Выберите бренд для рассмотрения" для выручки')


class BrandTablePage(BasePage):
    """
    Страница "Бренд".
    """
    def __init__(self, driver):
        super().__init__(driver, '/brand/')

    def check_header_elements(self):
        self.wait_locator_displayed(BrandTablePageLocators.BrandPageHeader.block)
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_payment_assert(self, is_assert_displayed: bool):
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandPageHeader.payment_assert_text),
                    equal_to(is_assert_displayed),
                    f'Отображение текста о необходимости оплаты в хедере - должно быть {is_assert_displayed}')

    def check_all_elements(self, is_assert_displayed: bool=False):
        self.check_header_elements()
        self.check_payment_assert(is_assert_displayed=is_assert_displayed)
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.title),
                    'Не отображается заголовок "Выберите бренд для рассмотрения"')
        self.wait_locator_displayed(BrandTablePageLocators.BrandsTable.table)
        self.check_table_header()
        self.check_table_filters()
        self.check_table_pagination()

    def check_table_header(self):
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_title),
                    'Не отображается заголовок столбца Бренд')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.product_amount_title),
                    'Не отображается заголовок столбца Кол-во товаров')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.sales_title),
                    'Не отображается заголовок столбца Продаж за 30 дней')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.money_title),
                    'Не отображается заголовок столбца Выручка за 30 дней')

    def check_table_filters(self):
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_filter),
                    'Не отображается фильтр столбца Бренд')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.product_filter),
                    'Не отображается фильтр столбца Кол-во товаров')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.sales_filter),
                    'Не отображается фильтр столбца Продаж за 30 дней')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.money_filter),
                    'Не отображается фильтр столбца Выручка за 30 дней')

    def check_table_data(self):
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_cell),
                    'Не отображаются данные столбца Бренд')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_amount),
                    'Не отображаются данные столбца Кол-во товаров')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_sales),
                    'Не отображаются данные столбца Продаж за 30 дней')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.brand_money),
                    'Не отображаются данные столбца Выручка за 30 дней')

    def check_table_pagination(self):
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.first_page_btn),
                    'Не отображается стрелка пролистывания на первую страницу')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.previous_page_btn),
                    'Не отображается стрелка пролистывания на предыдущую страницу')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.current_page),
                    'Не отображается номер текущей страницы')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.last_page),
                    'Не отображается номер последней страницы')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.next_page_btn),
                    'Не отображается стрелка пролистывания на следующую страницу')
        assert_that(self.is_locator_displayed(BrandTablePageLocators.BrandsTable.last_page_btn),
                    'Не отображается стрелка пролистывания на последнюю страницу')

    def sort_down_brands_by_rise_amount_in_table(self):
        self.wait_locator_displayed(BrandTablePageLocators.BrandsTable.product_amount_sort_down)
        for _ in range(2):
            self.find_element(BrandTablePageLocators.BrandsTable.product_amount_sort_down).click()

    def click_first_brand_in_table(self):
        self.find_element(BrandTablePageLocators.BrandsTable.brand_cell).click()
