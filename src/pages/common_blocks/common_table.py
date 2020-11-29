from selenium.webdriver.common.by import By


class CommonTableElements:
    block = (By.XPATH, '//div[@id="table_div"]', 'блок таблицы')
    header_item = (By.XPATH, '//span[@class="column-header-name"]', 'элемент шапки таблицы')
    filter_item = (By.XPATH, '//input[@placeholder="filter data..."]', 'элемент фильтра таблицы')
    data_item = (By.XPATH, '//td[@data-dash-row]', 'элемент данных таблицы')

    first_page_btn = (By.XPATH, '//button[@class="first-page"]', 'кнопка первая страница')
    previous_page_btn = (By.XPATH, '//button[@class="first-page"]', 'кнопка предыдущая страница')
    current_page = (By.XPATH, '//input[@class="current-page"]', 'текущая страница')
    last_page = (By.XPATH, '//div[@class="last-page"]', 'последняя страница')
    next_page_btn = (By.XPATH, '//button[@class="next-page"]', 'кнопка следущая страница')
    last_page_btn = (By.XPATH, '//button[@class="last-page"]', 'кнопка последняя страница')
