from src.pages.page import BasePage


class PaymentPageLocators:

    class PaymentPageHeader:
        ...


class PaymentPage(BasePage):
    """
    Страница оплаты.
    """
    def __init__(self, driver):
        super().__init__(driver, '/payment')
