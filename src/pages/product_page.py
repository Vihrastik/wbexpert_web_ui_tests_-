from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.common_table import CommonTableElements
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class ProductTableHeaders:
    id = 'ID'
    image = 'Изображение'
    category = 'Категория'
    brand = 'Бренд'
    provider = 'Поставщик'
    price = 'Цена'
    discount = 'Скидка'
    name = 'Название'
    description = 'Описание'
    saled = 'Продано'
    revenue = 'Выручка'
    delivered = 'Поставлено'
    reviews = 'Отзывов'


class ProductPageLocators:

    class ProductPageHeader(AuthorizedHeaderLocators):
        ...

    class Filters:
        filter_block = (By.XPATH, '//div[@class="row"]', 'блок фильтров')
        vendor_code_input = (By.XPATH, '//input[@placeholder="Введите артикул товара"]', 'поле "Введите артикул товара"')
        find_btn = (By.XPATH, '//button[@class="btn btn-primary"]', 'кнопка "Найти"')

    class ProductTable(CommonTableElements):
        block = (By.XPATH, '//div[@id="hits_items_table_morda"]', 'блок таблицы')


class ProductPage(BasePage):
    """
    Страница "Товары".
    """
    def __init__(self, driver):
        super().__init__(driver, '/product/')

    def check_header_elements(self):
        self.wait_locator_displayed(ProductPageLocators.ProductPageHeader.block)
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_payment_assert(self, is_assert_displayed: bool):
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductPageHeader.payment_assert_text),
                    equal_to(is_assert_displayed),
                    f'Отображение текста о необходимости оплаты в хедере - должно быть {is_assert_displayed}')

    def check_filters_elements(self):
        self.wait_locator_displayed(ProductPageLocators.Filters.filter_block)
        assert_that(self.is_locator_displayed(ProductPageLocators.Filters.vendor_code_input),
                    'Не отображается инпут поиска')
        assert_that(self.is_locator_displayed(ProductPageLocators.Filters.find_btn),
                    'Не отображается кнопка Найти')

    def check_products_table(self):
        self.wait_locator_displayed(ProductPageLocators.ProductTable.block)
        titles_products_table = [t.text for t in self.find_elements(ProductPageLocators.ProductTable.header_item)]
        assert_that(titles_products_table,
                    equal_to([ProductTableHeaders.id,
                              ProductTableHeaders.image,
                              ProductTableHeaders.category,
                              ProductTableHeaders.brand,
                              ProductTableHeaders.provider,
                              ProductTableHeaders.price,
                              ProductTableHeaders.discount,
                              ProductTableHeaders.name,
                              ProductTableHeaders.description,
                              ProductTableHeaders.saled,
                              ProductTableHeaders.revenue,
                              ProductTableHeaders.delivered,
                              ProductTableHeaders.reviews,
                              ]), 'Отображаются не все заголовки таблицы')
        assert_that(len(self.find_elements(ProductPageLocators.ProductTable.filter_item)), equal_to(13),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(ProductPageLocators.ProductTable.data_item), 'Нет данных в таблице')

    def check_product_table_pagination(self):
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductTable.first_page_btn),
                    'Не отображается стрелка пролистывания на первую страницу')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductTable.previous_page_btn),
                    'Не отображается стрелка пролистывания на предыдущую страницу')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductTable.current_page),
                    'Не отображается номер текущей страницы')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductTable.next_page_btn),
                    'Не отображается стрелка пролистывания на следующую страницу')
        assert_that(self.is_locator_displayed(ProductPageLocators.ProductTable.last_page_btn),
                    'Не отображается стрелка пролистывания на последнюю страницу')

    def check_all_elements(self, is_assert_displayed: bool=False):
        self.check_header_elements()
        self.check_payment_assert(is_assert_displayed=is_assert_displayed)
        self.check_filters_elements()
        self.check_products_table()
        self.check_product_table_pagination()
