from src.pages.page import BasePage


class HowToGetApiLocators:

    class HowToGetApiHeader:
        ...


class HowToGetApiPage(BasePage):
    """
    Страница "Как получить API-ключ?".
    """
    def __init__(self, driver):
        super().__init__(driver, '/howto/api-key')
