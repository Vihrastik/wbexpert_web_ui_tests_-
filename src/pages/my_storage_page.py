from hamcrest import (
    assert_that,
    equal_to,
    contains_string,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.common_table import CommonTableElements
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class StorageTableHeaders:
    photo = 'Фото'
    vendor_code = 'Артикул'
    brand = 'Бренд'
    name = 'Название'
    size = 'Размер'
    store = 'Склад'
    discount = 'Скидка'
    price = 'Цена'
    remainder = 'Остаток'
    end_date = 'Закончится через (дней)'
    active = 'Активен'


class MyStoragePageLocators:

    class MyStoragePageHeader(AuthorizedHeaderLocators):
        ...

    class Filters:
        filters_block = (By.XPATH, '//div[@class="row"]', 'блок фильтров')

        title = (By.XPATH, '//h1[text()="Мой склад"]', 'заголовок Мой склад')

        brands_text = (By.XPATH, '//span[text()="Бренды:"]', 'текст Бренды:')
        brands_all_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="все"]]', 'линк Бренды:все')
        brands_choose_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="выбрать"]]', 'линк Бренды:выбрать')

        categories_text = (By.XPATH, '//span[text()="Категории:"]', 'текст Категории:')
        categories_all_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="все"]]', 'линк Категории:все')
        categories_choose_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="выбрать"]]', 'линк Категории:выбрать')

        storages_text = (By.XPATH, '//span[text()="Склады:"]', 'текст Склады:')
        storages_all_btn = (By.XPATH, '//div[@id="wh_radioitems"]/div[./label[text()="все"]]', 'линк Склады:все')
        storages_choose_btn = (By.XPATH, '//div[@id="wh_radioitems"]/div[./label[text()="выбрать"]]', 'линк Склады:выбрать')

        collapse_text = (By.XPATH, '//div[text()="Схлопнуть:"]', 'текст Схлопнуть: ')
        collapse_colors_chbx = (By.XPATH, '//input[@id="root"]', 'линк Схлопнуть: Цвета')
        collapse_measure_chbx = (By.XPATH, '//input[@id="size"]', 'линк Схлопнуть: Размеры')
        collapse_stores_chbx = (By.XPATH, '//input[@id="warehouse"]', 'линк Схлопнуть: Склады')

        download_text = (By.XPATH, '//span[text()="Скачать"]', 'текст Скачать')
        download_xls = (By.XPATH, '//button[@id="download_xls"]', 'кнопка xls')
        download_csv = (By.XPATH, '//button[@id="download_csv"]', 'кнопка csv')

    class StorageTable(CommonTableElements):
        last_update = (By.XPATH, '//h4', 'последнее обновление')


class MyStoragePage(BasePage):
    """
    Страница "Мои склад".
    """
    def __init__(self, driver):
        super().__init__(driver, '/my/storage/')

    def check_header_elements(self):
        self.wait_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.block)
        assert_that(self.is_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.MyStoragePageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_filters(self):
        self.wait_locator_displayed(MyStoragePageLocators.Filters.filters_block)
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.title),
                    'Не отображается заголовок "Мои склад"')

        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.brands_text),
                    'Не отображается текст "Бренды:"')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.brands_all_btn),
                    'Не отображается кнопка бренды все')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.brands_choose_btn),
                    'Не отображается кнопка бренды выбрать')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.categories_text),
                    'Не отображается текст "Категории:"')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.categories_all_btn),
                    'Не отображается кнопка категории все')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.categories_choose_btn),
                    'Не отображается кнопка категории выбрать')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.storages_text),
                    'Не отображается текст "Склады:"')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.storages_all_btn),
                    'Не отображается кнопка склады все')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.storages_choose_btn),
                    'Не отображается кнопка склады выбрать')

        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.collapse_text),
                    'Не отображается текст "Схлопнуть:"')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.collapse_colors_chbx),
                    'Не отображается чекбокс схлопнуть цвета')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.collapse_measure_chbx),
                    'Не отображается чекбокс схлопнуть размеры')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.collapse_stores_chbx),
                    'Не отображается чекбокс схлопнуть склады')

        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.download_text),
                    'Не отображается текст "Скачать"')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.download_csv),
                    'Не отображается кнопка скачать csv')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.Filters.download_xls),
                    'Не отображается кнопка скачать xls')

    def check_storage_table(self):
        self.wait_locator_displayed(MyStoragePageLocators.StorageTable.block)
        assert_that(self.find_element(MyStoragePageLocators.StorageTable.last_update).text,
                    contains_string('Дата последнего обновления'),
                    'Не отображается заголовок "Дата последнего обновления"')
        titles_texts_storage = [t.text for t in self.find_elements(MyStoragePageLocators.StorageTable.header_item)]
        assert_that(titles_texts_storage,
                    equal_to([StorageTableHeaders.photo,
                              StorageTableHeaders.vendor_code,
                              StorageTableHeaders.brand,
                              StorageTableHeaders.name,
                              StorageTableHeaders.size,
                              StorageTableHeaders.store,
                              StorageTableHeaders.price,
                              StorageTableHeaders.discount,
                              StorageTableHeaders.remainder,
                              StorageTableHeaders.end_date,
                              StorageTableHeaders.active,
                              ]), 'Отображаются не все заголовки таблицы')
        assert_that(len(self.find_elements(MyStoragePageLocators.StorageTable.filter_item)), equal_to(11),
                    'Отображаются не все фильтры под хедерами')
        assert_that(self.find_elements(MyStoragePageLocators.StorageTable.data_item), 'Нет данных в таблице')

    def check_product_table_pagination(self):
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.first_page_btn),
                    'Не отображается стрелка пролистывания на первую страницу')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.previous_page_btn),
                    'Не отображается стрелка пролистывания на предыдущую страницу')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.current_page),
                    'Не отображается номер текущей страницы')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.last_page),
                    'Не отображается номер последней страницы')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.next_page_btn),
                    'Не отображается стрелка пролистывания на следующую страницу')
        assert_that(self.is_locator_displayed(MyStoragePageLocators.StorageTable.last_page_btn),
                    'Не отображается стрелка пролистывания на последнюю страницу')

    def check_all_elements(self):
        self.check_header_elements()
        self.check_filters()
        self.wait_locator_displayed(MyStoragePageLocators.StorageTable.block)
        self.check_storage_table()
        self.check_product_table_pagination()
