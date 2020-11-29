from datetime import datetime, timedelta

from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.common.funcs import (
    get_str_data,
    delete_zero_in_dates,
)
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class MyTableHeaders:
    # данные обновляются ~ 6 утра (на машине с ранером время на три часа отстает)
    item = 'Показатель'
    yesterday = f'Вчера\n{get_str_data((datetime.now()-timedelta(days=1)).strftime("%d.%m"))}'
    yesterday_before_six = f'Вчера\n{get_str_data((datetime.now()-timedelta(days=2)).strftime("%d.%m"))}'
    week = (f'7 дней\nс {delete_zero_in_dates((datetime.now()-timedelta(days=7)).strftime("%d"))} '
            f'по {get_str_data((datetime.now()-timedelta(days=1)).strftime("%d.%m"))}')
    week_before_six = (f'7 дней\nс {delete_zero_in_dates((datetime.now()-timedelta(days=8)).strftime("%d"))} '
                       f'по {get_str_data((datetime.now()-timedelta(days=2)).strftime("%d.%m"))}')
    month = (f'30 дней\nс {get_str_data((datetime.now()-timedelta(days=30)).strftime("%d.%m"))} '
             f'по {get_str_data((datetime.now()-timedelta(days=1)).strftime("%d.%m"))}')
    month_before_six = (f'30 дней\nс {get_str_data((datetime.now()-timedelta(days=31)).strftime("%d.%m"))} '
                        f'по {get_str_data((datetime.now()-timedelta(days=2)).strftime("%d.%m"))}')


class MyTablePageLocators:

    class MyTablePageHeader(AuthorizedHeaderLocators):
        ...

    class Filters:
        filter_block = (By.XPATH, '//div[@class="row"]', 'блок фильтров')
        title = (By.XPATH, '//h1[text()="Сводка по моим продажам"]', 'заголовок "Сводка по моим продажам"')

        brands_text = (By.XPATH, '//span[text()="Бренды:"]', 'текст Бренды:')
        brands_all_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="все"]]', 'линк Бренды:все')
        brands_choose_btn = (By.XPATH, '//div[@id="brand_radioitems"]/div[./label[text()="выбрать"]]', 'линк Бренды:выбрать')

        categories_text = (By.XPATH, '//span[text()="Категории:"]', 'текст Категории:')
        categories_all_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="все"]]', 'линк Категории:все')
        categories_choose_btn = (By.XPATH, '//div[@id="category_radioitems"]/div[./label[text()="выбрать"]]', 'линк Категории:выбрать')

    class Table:
        table_block = (By.XPATH, '//div[@id="table_div"]', 'блок таблицы')
        header = (By.XPATH, '//div[@id="table_div"]//th', 'элемент хедера таблицы')
        data = (By.XPATH, '//div[@id="table_div"]//tbody/tr/td', 'элемент данных таблицы')


class MyTablePage(BasePage):
    """
    Страница "Мои товары".
    """
    def __init__(self, driver):
        super().__init__(driver, '/my/table/')

    def check_header_elements(self):
        self.wait_locator_displayed(MyTablePageLocators.MyTablePageHeader.block)
        assert_that(self.is_locator_displayed(MyTablePageLocators.MyTablePageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(MyTablePageLocators.MyTablePageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(MyTablePageLocators.MyTablePageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(MyTablePageLocators.MyTablePageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(MyTablePageLocators.MyTablePageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_all_elements(self):
        self.check_header_elements()
        self.wait_locator_displayed(MyTablePageLocators.Filters.filter_block)
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.title),
                    'Не отображается заголовок "Сводка по моим продажам"')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.brands_text),
                    'Не отображается текст "Бренды:"')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.brands_all_btn),
                    'Не отображается кнопка бренды все')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.brands_choose_btn),
                    'Не отображается кнопка бренды выбрать')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.categories_text),
                    'Не отображается текст "Категории:"')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.categories_all_btn),
                    'Не отображается кнопка категории все')
        assert_that(self.is_locator_displayed(MyTablePageLocators.Filters.categories_choose_btn),
                    'Не отображается кнопка категории выбрать')
        self.wait_locator_displayed(MyTablePageLocators.Table.table_block)
        titles_my_table = [t.text for t in self.find_elements(MyTablePageLocators.Table.header)]
        # данные обновляются ~ 5 утра (на машине с ранером время на три часа отстает)
        if float(datetime.now().strftime("%H:%M").replace(':', '.')) < 2:
            assert_that(titles_my_table,
                        equal_to([MyTableHeaders.item,
                                  MyTableHeaders.yesterday_before_six,
                                  MyTableHeaders.week_before_six,
                                  MyTableHeaders.month_before_six,
                                  ]), 'Заголовки в таблице "Сводка по моим продажам" не отображаются или не обновились')
        else:
            assert_that(titles_my_table,
                        equal_to([MyTableHeaders.item,
                                  MyTableHeaders.yesterday,
                                  MyTableHeaders.week,
                                  MyTableHeaders.month,
                                  ]), 'Заголовки в таблице "Сводка по моим продажам" не отображаются или не обновились')
        assert_that(self.find_elements(MyTablePageLocators.Table.data), 'Нет данных в таблице')
