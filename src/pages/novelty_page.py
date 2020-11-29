from hamcrest import (
    assert_that,
    equal_to,
)
from selenium.webdriver.common.by import By

from src.pages.common_blocks.common_table import CommonTableElements
from src.pages.common_blocks.header import AuthorizedHeaderLocators
from src.pages.page import BasePage


class NoveltyTableHeaders:
    id = 'ID'
    image = 'Изображение'
    graph = 'График'
    category = 'Категория'
    brand = 'Бренд'
    provider = 'Поставщик'
    price = 'Цена'
    discount = 'Скидка'
    name = 'Название'
    sales_two_weeks = 'Продажи за 2 недели'
    revenue_two_weeks = 'Выручка за 2 недели'
    sales_month = 'Продажи за месяц'
    sales_two_month = 'Продажи за 2 месяца'
    revenue_two_month = 'Выручка за 2 месяца'
    date = 'Дата появления'
    bought = 'Куплено всего'
    sales_to_lifetime = 'Продажи месяц к lifetime'


class NoveltyPageLocators:

    class NoveltyPageHeader(AuthorizedHeaderLocators):
        payment_assert_text = (By.XPATH, '//h1[text()="Страница доступна только после покупки тарифа"]', 'предупреждение "Страница доступна только после покупки тарифа"')

    class Filters:
        block = (By.XPATH, '//div[@id="bigdiv"]', 'блок фильтров')

        category_one_text = (By.XPATH, '//p[text()="Категория1"]', 'текст Категория1')
        category_one_chbx = (By.XPATH, '//input[contains(@id, "Категория1") and @type="checkbox"]', 'чекбокс Категория1')
        category_one_dropdown = (By.XPATH, '//div[contains(@id, "Категория1")]', 'дропдаун Категория1')
        category_two_text = (By.XPATH, '//p[text()="Категория2"]', 'текст Категория2')
        category_two_chbx = (By.XPATH, '//input[contains(@id, "Категория2") and @type="checkbox"]', 'чекбокс Категория2')
        category_two_dropdown = (By.XPATH, '//div[contains(@id, "Категория2")]', 'дропдаун Категория2')
        category_three_text = (By.XPATH, '//p[text()="Категория3"]', 'текст Категория3')
        category_three_chbx = (By.XPATH, '//input[contains(@id, "Категория3") and @type="checkbox"]', 'чекбокс Категория3')
        category_three_dropdown = (By.XPATH, '//div[contains(@id, "Категория3")]', 'дропдаун Категория3')
        category_four_text = (By.XPATH, '//p[text()="Категория4"]', 'текст Категория4')
        category_four_chbx = (By.XPATH, '//input[contains(@id, "Категория4") and @type="checkbox"]', 'чекбокс Категория4')
        category_four_dropdown = (By.XPATH, '//div[contains(@id, "Категория4")]', 'дропдаун Категория4')
        category_five_text = (By.XPATH, '//p[text()="Категория5"]', 'текст Категория5')
        category_five_chbx = (By.XPATH, '//input[contains(@id, "Категория5") and @type="checkbox"]', 'чекбокс Категория5')
        category_five_dropdown = (By.XPATH, '//div[contains(@id, "Категория5")]', 'дропдаун Категория5')
        brand_text = (By.XPATH, '//p[text()="Бренд"]', 'текст Бренд')
        brand_chbx = (By.XPATH, '//input[contains(@id, "Бренд") and @type="checkbox"]', 'чекбокс Бренд')
        brand_dropdown = (By.XPATH, '//div[contains(@id, "Бренд")]', 'дропдаун Бренд')

        discount_text = (By.XPATH, '//p[text()="Скидка"]', 'текст Скидка')
        discount_from = (By.XPATH, '//input[contains(@id, "min_Скидка")]', 'инпут min_Скидка')
        discount_to = (By.XPATH, '//input[contains(@id, "max_Скидка")]', 'инпут max_Скидка')
        price_text = (By.XPATH, '//p[text()="Цена"]', 'текст Цена')
        price_from = (By.XPATH, '//input[contains(@id, "min_Цена")]', 'инпут min_Цена')
        price_to = (By.XPATH, '//input[contains(@id, "max_Цена")]', 'инпут max_Цена')
        days_text = (By.XPATH, '//p[text()="Дней на сайте"]', 'текст Дней на сайте')
        days_from = (By.XPATH, '//input[contains(@id, "min_Дней на сайте")]', 'инпут min_Дней на сайте')
        days_to = (By.XPATH, '//input[contains(@id, "max_Дней на сайте")]', 'инпут max_Дней на сайте')
        sales_text = (By.XPATH, '//p[text()="Продажи за 2 недели"]', 'текст Продажи за 2 недели')
        sales_from = (By.XPATH, '//input[contains(@id, "min_Продажи за 2 недели")]', 'инпут min_Продажи за 2 недели')
        sales_to = (By.XPATH, '//input[contains(@id, "max_Продажи за 2 недели")]', 'инпут max_Продажи за 2 недели')
        sales_two_weeks_text = (By.XPATH, '//p[text()="Дней с продажами 2 недели"]', 'текст Дней с продажами 2 недели')
        sales_two_weeks_from = (By.XPATH, '//input[contains(@id, "min_Дней с продажами 2 недели")]', 'инпут min_Дней с продажами 2 недели')
        sales_two_weeks_to = (By.XPATH, '//input[contains(@id, "max_Дней с продажами 2 недели")]', 'инпут max_Дней с продажами 2 недели')
        sales_two_month_text = (By.XPATH, '//p[text()="Дней с продажами 2 месяца"]', 'текст Дней с продажами 2 месяца')
        sales_two_month_from = (By.XPATH, '//input[contains(@id, "min_Дней с продажами 2 месяца")]', 'инпут min_Дней с продажами 2 месяца')
        sales_two_month_to = (By.XPATH, '//input[contains(@id, "max_Дней с продажами 2 месяца")]', 'инпут max_Дней с продажами 2 месяца')

        outliers_chbx = (By.XPATH, '//input[@id="outlayer"]', 'чекбокс Исключить выбросы')

        other_filters_btn = (By.XPATH, '//button[@id="collapse-button"]', 'кнопка Показать остальные фильтры')
        xlsx_download_btn = (By.XPATH, '//button[@id="download_xls"]', 'кнопка Скачать в xlsx')
        csv_download_btn = (By.XPATH, '//button[@id="download_csv"]', 'кнопка Скачать в csv')
        toggle_columns_btn = (By.XPATH, '//button[@class="show-hide"]', 'кнопка Toggle Columns')

    class NoveltyTable(CommonTableElements):
        block = (By.XPATH, '//table[@class="cell-table"]', 'таблица с данными')
        hide_column = (By.XPATH, '//span[@class="column-header--hide"]', 'элемент фильтров таблицы')


class NoveltyPage(BasePage):
    """
    Страница "Новинки".
    """
    def __init__(self, driver):
        super().__init__(driver, '/novelty/')

    def check_header_elements(self):
        self.wait_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.block)
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.wb_logo_main),
                    'Не отображается логотип в хедере')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.analysis_dropdown),
                    'Не отображается дропдаун "Конкурентный анализ" в хедере')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.products_dropdown),
                    'Не отображается дропдаун "Мои товары" в хедере')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.phone_link),
                    'Не отображается телефон в хедере')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.exit_btn),
                    'Не отображается кнопка выхода в хедере')

    def check_payment_assert(self, is_assert_displayed: bool):
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyPageHeader.payment_assert_text),
                    equal_to(is_assert_displayed),
                    f'Отображение текста о необходимости оплаты в хедере - должно быть {is_assert_displayed}')

    def check_filters_elements(self):
        self.wait_locator_displayed(NoveltyPageLocators.Filters.block)
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_one_text),
                    'Не отображается текст Категория1')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_one_chbx),
                    'Не отображается чекбокс Категория1')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_one_dropdown),
                    'Не отображается дропдаун Категория1')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_two_text),
                    'Не отображается текст Категория2')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_two_chbx),
                    'Не отображается чекбокс Категория2')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_two_dropdown),
                    'Не отображается дропдаун Категория2')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_three_text),
                    'Не отображается текст Категория3')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_three_chbx),
                    'Не отображается чекбокс Категория3')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_three_dropdown),
                    'Не отображается дропдаун Категория3')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_four_text),
                    'Не отображается текст Категория4')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_four_chbx),
                    'Не отображается чекбокс Категория4')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_four_dropdown),
                    'Не отображается дропдаун Категория4')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_five_text),
                    'Не отображается текст Категория5')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_five_chbx),
                    'Не отображается чекбокс Категория5')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.category_five_dropdown),
                    'Не отображается дропдаун Категория5')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.brand_text),
                    'Не отображается текст Бренд')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.brand_chbx),
                    'Не отображается чекбокс Бренд')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.brand_dropdown),
                    'Не отображается дропдаун Бренд')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.discount_text),
                    'Не отображается текст Скидка')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.discount_from),
                    'Не отображается инпут Скидка от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.discount_to),
                    'Не отображается инпут Скидка до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.price_text),
                    'Не отображается текст Цена')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.price_from),
                    'Не отображается инпут Цена от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.price_to),
                    'Не отображается инпут Цена до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.days_text),
                    'Не отображается текст Дней на сайте')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.days_from),
                    'Не отображается инпут Дней на сайте от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.days_to),
                    'Не отображается инпут Дней на сайте до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_text),
                    'Не отображается текст Продажи за 2 недели')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_from),
                    'Не отображается инпут Продажи за 2 недели от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_to),
                    'Не отображается инпут Продажи за 2 недели до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_weeks_text),
                    'Не отображается текст Дней с продажами 2 недели')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_weeks_from),
                    'Не отображается инпут Дней с продажами 2 недели от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_weeks_to),
                    'Не отображается инпут Дней с продажами 2 недели до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_month_text),
                    'Не отображается текст Дней с продажами 2 месяца')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_month_from),
                    'Не отображается инпут Дней с продажами 2 месяца от')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.sales_two_month_to),
                    'Не отображается инпут Дней с продажами 2 месяца до')

        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.outliers_chbx),
                    'Не отображается чекбокс Исключить выбросы')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.other_filters_btn),
                    'Не отображается кнопка Показать другие фильтры')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.xlsx_download_btn),
                    'Не отображается кнопка Скачать в xlsx')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.csv_download_btn),
                    'Не отображается кнопка Скачать в csv')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.Filters.toggle_columns_btn),
                    'Не отображается кнопка Toggle Columns')

    def check_novelty_table(self):
        self.wait_locator_displayed(NoveltyPageLocators.NoveltyTable.block)
        titles_products_table = [t.text for t in self.find_elements(NoveltyPageLocators.NoveltyTable.header_item)]
        assert_that(titles_products_table,
                    equal_to([NoveltyTableHeaders.id,
                              NoveltyTableHeaders.image,
                              NoveltyTableHeaders.graph,
                              NoveltyTableHeaders.category,
                              NoveltyTableHeaders.brand,
                              NoveltyTableHeaders.provider,
                              NoveltyTableHeaders.price,
                              NoveltyTableHeaders.discount,
                              NoveltyTableHeaders.name,
                              NoveltyTableHeaders.sales_two_weeks,
                              NoveltyTableHeaders.revenue_two_weeks,
                              NoveltyTableHeaders.sales_month,
                              NoveltyTableHeaders.sales_two_month,
                              NoveltyTableHeaders.revenue_two_month,
                              NoveltyTableHeaders.date,
                              NoveltyTableHeaders.bought,
                              NoveltyTableHeaders.sales_to_lifetime,
                              ]), 'Отображаются не все заголовки таблицы')
        assert_that(len(self.find_elements(NoveltyPageLocators.NoveltyTable.hide_column)), equal_to(17),
                    'Отображаются не все кнопки скрыть в хедерах')
        assert_that(self.find_elements(NoveltyPageLocators.NoveltyTable.data_item), 'Нет данных в таблице')

    def check_novelty_table_pagination(self):
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.first_page_btn),
                    'Не отображается стрелка пролистывания на первую страницу')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.previous_page_btn),
                    'Не отображается стрелка пролистывания на предыдущую страницу')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.current_page),
                    'Не отображается номер текущей страницы')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.next_page_btn),
                    'Не отображается стрелка пролистывания на следующую страницу')
        assert_that(self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.last_page_btn),
                    'Не отображается стрелка пролистывания на последнюю страницу')

    def check_all_elements(self, is_assert_displayed: bool=False):
        self.check_header_elements()
        self.check_payment_assert(is_assert_displayed=is_assert_displayed)
        self.check_filters_elements()
        self.check_novelty_table()
        self.check_novelty_table_pagination()

    def assert_data_not_displayed(self):
        assert_that(not self.is_locator_displayed(NoveltyPageLocators.Filters.block),
                    'Отображается блок фильтров')
        assert_that(not self.is_locator_displayed(NoveltyPageLocators.NoveltyTable.block),
                    'Отображается таблица с новинками')
