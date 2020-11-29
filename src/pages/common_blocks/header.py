from selenium.webdriver.common.by import By


class HeaderLocators:
    """
    Хедер сайта
    """
    block = (By.XPATH, '//div[@id="t-header"]', 'блок хедера')
    wb_logo_main = (By.XPATH, '//img[@alt="WB Expert"]', 'логотип "WB Expert"')
    wb_logo_link = (By.XPATH, '//a[@href="https://wbexpert.ru/"]', 'логотип "WB Expert" со ссылкой')

    tariffs_btn = (By.XPATH, '//a[text()="Тарифы"]', 'кнопка "Тарифы"')
    come_in_btn = (By.XPATH, '//a[text()="Войти"]', 'кнопка "Войти"')
    registration_btn = (By.XPATH, '//div[contains(@class, "right_buttons")]/a[contains(@href, "/signup")]', 'кнопка "Регистрация"')


class AuthorizedHeaderLocators:
    block = (By.XPATH, '//nav', 'блок хедера')
    wb_logo_main = (By.XPATH, '//img', 'логотип wbexpert')
    analysis_dropdown = (By.XPATH, '//li[./a[text()="Конкурентный анализ"]]', 'выпадающее меню Конкурентный анализ')
    analysis = (By.XPATH, '//a[text()="Аналитика"]', 'выпадающее меню Аналитика')
    brands = (By.XPATH, '//a[text()="Бренды"]', 'выпадающее меню Бренды')
    products = (By.XPATH, '//a[text()="Товары"]', 'выпадающее меню Товары')
    new = (By.XPATH, '//a[text()="Новинки"]', 'выпадающее меню Новинки')

    products_dropdown = (By.XPATH, '//li[./a[text()="Мои товары"]]', 'выпадающее меню Мои товары')
    table = (By.XPATH, '//a[text()="Сводная"]', 'выпадающее меню Сводная')
    selling = (By.XPATH, '//a[text()="Продажи"]', 'выпадающее меню Продажи')
    store = (By.XPATH, '//a[text()="Склад"]', 'выпадающее меню Склад')
    rating = (By.XPATH, '//a[text()="Рейтинг"]', 'выпадающее меню Рейтинг')
    api_key = (By.XPATH, '//a[text()="API ключи"]', 'выпадающее меню API ключи')

    phone = (By.XPATH, '//li[@class="nav-item"]//div', 'номер телефона')
    phone_link = (By.XPATH, '//a[@id="profile"]', 'ссылка с номером телефона')
    exit_btn = (By.XPATH, '//li[@class="nav-item"]//a[@href="/logout"]', 'кнопка выхода')

    payment_assert_text = (By.XPATH, '//h1[text()="Тариф не оплачен. Показаны старые данные. '
                                     'Для актуальных данных оплатите тариф на странице профиля."]',
                           'сообщение "Тариф не оплачен. Показаны старые данные. '
                           'Для актуальных данных оплатите тариф на странице профиля."')

    preloader = (By.XPATH, '//div[@class="spinner-border"]', 'прелоадер')
