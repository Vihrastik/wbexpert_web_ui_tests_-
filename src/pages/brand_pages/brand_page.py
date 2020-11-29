from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.brand_pages.brand_table_page import (
    BrandTablePage,
    BrandTablePageLocators,
)


class TableSalesHeaders:
    category = 'Категория'
    products = 'Товаров'
    sales_30 = 'Продажи (30 дней)'
    money_30 = 'Выручка (30 дней)'
    share_of_goods = 'Доля от товаров'
    share_withount_sales = 'Доля от продаж'
    share_of_proceeds = 'Доля от выручки'
    amount_rank = 'Ранк по количеству'
    sale_rank = 'Ранк по продажам'
    proceeds_rank = 'Ранк по выручке'
    competitors = 'Конкурентов в категории'


class TableListingHeaders:
    url = 'URL'
    goods_all = 'Товаров в листинге (всего)'
    position = 'Позиция первого предмета в листинге'
    top_item = 'Верхний товар'


class TableHitsHeaders:
    vendor_code = 'Артикул'
    photo = 'Фото'
    brand = 'Бренд'
    name = 'Название'
    price = 'Цена'
    sales_30 = 'Покупок 30 дней'
    money_30 = 'Выручка руб. за 30 дней'


class BrandPageLocators:

    class BrandPageHeader(BrandTablePageLocators.BrandsTable):
        ...

    class BrandInfo:
        title = (By.XPATH, '//h3', 'заголовок с названием бренда')
        logo = (By.XPATH, '//div[@class="row"]//img', 'логотип бренда')
        wb_link = (By.XPATH, '//div[@class="row"]//a', 'ссылка на wb')
        products_title = (By.XPATH, '//h5[text()="Товаров"]', 'заголовок "Товаров"')
        products_count = (By.XPATH, '//div[./h5[text()="Товаров"]]/h4', 'количество "Товаров"')
        sales_title = (By.XPATH, '//h5[text()="Продаж за 30 дней"]', 'заголовок "Продаж за 30 дней"')
        sales_count = (By.XPATH, '//div[./h5[text()="Продаж за 30 дней"]]/h4', 'количество "Продаж за 30 дней"')
        money_title = (By.XPATH, '//h5[text()="Выручка за 30 дней"]', 'заголовок "Выручка за 30 дней"')
        money_count = (By.XPATH, '//div[./h5[text()="Выручка за 30 дней"]]/h4', 'количество "Выручка за 30 дней"')
        products_without_sales_title = (By.XPATH, '//h5[text()="Товаров без продаж"]', 'заголовок "Товаров без продаж"')
        products_without_sales_count = (By.XPATH, '//div[./h5[text()="Товаров без продаж"]]/h4', 'количество "Товаров без продаж"')

    class TableSales:
        block = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="category"]]', 'блок таблицы продаж')
        header_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="category"]]//span[@class="column-header-name"]', 'элемент заголовка в таблице продаж')
        filter_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="category"]]//input[@placeholder="filter data..."]', 'элемент фильтра в таблице продаж')
        data_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="category"]]//td[@data-dash-row]', 'элемент выдачи в таблице продаж')

    class TableListing:
        block = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="base_url"]]', 'блок таблицы листинга')
        header_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="base_url"]]//span[@class="column-header-name"]', 'элемент заголовка в таблице листинга')
        filter_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="base_url"]]//input[@placeholder="filter data..."]', 'элемент фильтра в таблице листинга')
        data_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="base_url"]]//td[@data-dash-row]', 'элемент выдачи в таблице листинга')

    class TableHits:
        block = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="id_url"]]', 'блок таблицы Хиты продаж')
        header_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="id_url"]]//span[@class="column-header-name"]', 'элемент заголовка в таблице Хиты продаж')
        filter_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="id_url"]]//input[@placeholder="filter data..."]', 'элемент фильтра в таблице Хиты продаж')
        data_item = (By.XPATH, '//table[./tbody/tr/th[@data-dash-column="id_url"]]//td[@data-dash-row]', 'элемент выдачи в таблице Хиты продаж')


class BrandPage(BrandTablePage):
    """
    Страница конкретного бренда.
    """

    def check_brand_elements(self, is_assert_displayed: bool):
        self.check_header_elements()
        self.check_payment_assert(is_assert_displayed=is_assert_displayed)
        self.check_brand_info()
        self.check_table_sales()
        self.check_table_listing()
        self.check_table_hits()

    def check_brand_info(self):
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.title),
                    'Не отображается заголовок с названием бренда')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.logo),
                    'Не отображается логотип бренда')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.wb_link),
                    'Не отображается ссылка на вайлдберриз')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.products_title),
                    'Не отображается заголовок "Товаров"')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.products_count),
                    'Не отображается количество товаров')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.sales_title),
                    'Не отображается заголовок "Продаж за 30 дней"')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.sales_count),
                    'Не отображается количество продаж за 30 дней')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.money_title),
                    'Не отображается заголовок "Выручка за 30 дней"')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.money_count),
                    'Не отображается количество выручки за 30 дней')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.products_without_sales_title),
                    'Не отображается заголовок "Товаров без продаж"')
        assert_that(self.is_locator_displayed(BrandPageLocators.BrandInfo.products_without_sales_count),
                    'Не отображается количество товаров без продаж')

    def check_table_listing(self):
        self.wait_locator_displayed(BrandPageLocators.TableListing.block)
        titles_texts_listing = [t.text for t in self.find_elements(BrandPageLocators.TableListing.header_item)]
        assert_that(any([header for header in [TableListingHeaders.url,
                                               TableListingHeaders.goods_all,
                                               TableListingHeaders.position,
                                               TableListingHeaders.top_item,
                                               ] if header in titles_texts_listing]),
                    'Заголовки таблицы с листингом изменились:')
        assert_that(len(self.find_elements(BrandPageLocators.TableListing.filter_item)), equal_to(6),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(BrandPageLocators.TableListing.data_item), 'Нет данных в таблице')

    def check_table_sales(self):
        self.wait_locator_displayed(BrandPageLocators.TableSales.block)
        titles_texts_sales = [t.text for t in self.find_elements(BrandPageLocators.TableSales.header_item)]
        assert_that(titles_texts_sales,
                    equal_to([TableSalesHeaders.category,
                              TableSalesHeaders.products,
                              TableSalesHeaders.sales_30,
                              TableSalesHeaders.money_30,
                              TableSalesHeaders.share_of_goods,
                              TableSalesHeaders.share_withount_sales,
                              TableSalesHeaders.share_of_proceeds,
                              TableSalesHeaders.amount_rank,
                              TableSalesHeaders.sale_rank,
                              TableSalesHeaders.proceeds_rank,
                              TableSalesHeaders.competitors,
                              ]), 'Заголовки таблицы с продажами изменились:')
        assert_that(len(self.find_elements(BrandPageLocators.TableSales.filter_item)), equal_to(11),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(BrandPageLocators.TableSales.data_item), 'Нет данных в таблице')

    def check_table_hits(self):
        self.wait_locator_displayed(BrandPageLocators.TableHits.block)
        titles_texts_hits = [t.text for t in self.find_elements(BrandPageLocators.TableHits.header_item)]
        assert_that(titles_texts_hits,
                    equal_to([TableHitsHeaders.vendor_code,
                              TableHitsHeaders.photo,
                              TableHitsHeaders.brand,
                              TableHitsHeaders.name,
                              TableHitsHeaders.price,
                              TableHitsHeaders.sales_30,
                              TableHitsHeaders.money_30,
                              ]), 'Заголовки таблицы с хитами изменились:')
        assert_that(len(self.find_elements(BrandPageLocators.TableHits.filter_item)), equal_to(7),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(BrandPageLocators.TableHits.data_item), 'Нет данных в таблице')
