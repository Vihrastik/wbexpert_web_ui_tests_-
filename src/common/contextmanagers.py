import time
from contextlib import contextmanager

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.common import network
from src.common.decorators import wait_until


@contextmanager
def wait_for_new_window(browser: WebDriver, wait_time: int = 10):
    tabs = browser.window_handles
    yield
    WebDriverWait(browser, wait_time).until(expected_conditions.new_window_is_opened(tabs))
    tabs = browser.window_handles
    browser.switch_to.window(tabs[len(tabs)-1])


@contextmanager
def wait_for_page_to_reload(browser: WebDriver, wait_time: int = 30):
    browser.execute_script('document.__selenium_placeholder_id = "SELENIUM_PLACEHOLDER_ID"')
    yield

    @wait_until(exception_message=f'не перезагрузилась страница {browser.current_url}',
                wait_time=wait_time)
    def wait_to_reload() -> bool:
        sel_id = browser.execute_script('return document.__selenium_placeholder_id')
        return sel_id != 'SELENIUM_PLACEHOLDER_ID'
    wait_to_reload()


@contextmanager
def wait_all_requests_stop(browser: WebDriver, wait_time: int = 30):
    yield

    @wait_until(exception_message='не прекратились запросы к странице', wait_time=wait_time)
    def is_stopped() -> bool:
        requests_before = network.get_network_log(browser)
        time.sleep(0.25)
        requests_after = network.get_network_log(browser)
        return requests_before == requests_after

    is_stopped()
