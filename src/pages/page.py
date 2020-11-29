import os

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.common.decorators import wait_until
from src.pages.common_blocks.header import AuthorizedHeaderLocators


class BasePage:
    """
    Базовый класс для страниц. От него наследуются все остальные.
    """

    def __init__(self, driver, path=''):
        self.driver = driver
        self.base_url = os.environ.get('BASE_URL')
        self.path = path

    def find_element(self, locator: tuple, time: int = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator[:2]),
                                                      message=f'Не получается найти элемент {locator[2]} '
                                                              f'на странице {self.driver.current_url}')

    def find_elements(self, locator: tuple, time: int = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator[:2]),
                                                      message=f'Не получается найти элемент {locator[2]} '
                                                              f'на странице {self.driver.current_url}')

    def open(self):
        return self.driver.get(self.base_url+self.path)

    def is_locator_displayed(self, locator: tuple):
        try:
            return self.find_element(locator).is_displayed()
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException, TimeoutError):
            return False

    def wait_preloader_to_hide(self, wait_time: int = 60):
        @wait_until(exception_message=f'прелоадер не пропал со страницы {self.driver.current_url}',
                    wait_time=wait_time)
        def wait_preloader_locator_hide():
            return not self.is_locator_displayed(AuthorizedHeaderLocators.preloader)
        wait_preloader_locator_hide()

    def wait_locator_displayed(self, locator: tuple, wait_time: int = 90):
        @wait_until(exception_message=f'локатор {locator[2]} не отображается на странице {self.driver.current_url}',
                    wait_time=wait_time)
        def check_displayed():
            return self.is_locator_displayed(locator)
        check_displayed()
