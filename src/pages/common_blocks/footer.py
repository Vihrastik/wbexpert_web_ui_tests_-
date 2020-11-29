from selenium.webdriver.common.by import By


class Footer:
    """
    Футер сайта
    """
    wb_logo_text = (By.XPATH, '//*[contains(text(), "© 2020 Wildberries Expert")]', 'логотип Wildberries')
    terms_of_use = (By.XPATH, '//a[text()="Пользовательское соглашение"]', 'ссылка Пользовательское соглашение')
    license_agreement = (By.XPATH, '//a[text()="Лицензионное соглашение"]', 'ссылка Лицензионное соглашение')
    privacy_policy = (By.XPATH, '//a[text()="Политика конфиденциальности"]', 'ссылка Политика конфиденциальности')
