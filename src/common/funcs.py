import re

from selenium.webdriver.remote.webdriver import WebDriver

from src.common import network
from src.common.consts import month
from src.common.decorators import wait_until


def is_in_view(locator_position, window_position, window_size):
    _, locator_position_y = locator_position
    window_position_y = int(window_position['y'])
    return window_position_y <= int(locator_position_y) <= window_position_y + window_size['height']


def wait_in_view(locator_position, window_position, window_size):
    @wait_until(exception_message='локатор не появился в области видимости', wait_time=10)
    def check_view(locator_position, window_position, window_size):
        return is_in_view(locator_position, window_position, window_size)
    check_view(locator_position, window_position, window_size)


def get_callable_phone(browser: WebDriver):
   network_items = network.get_network_log(browser, is_web_doc=False)
   for item in network_items:
       if 'tel:' in item.url:
           return item.url


def get_callable_email(browser: WebDriver):
   network_items = network.get_network_log(browser, is_web_doc=False)
   for item in network_items:
       if 'mailto:' in item.url:
           return item.url


def get_str_data(date):
    current_month = date.split('.')[1]
    date_str = date.replace(f'.{current_month}', f' {month[int(current_month)].lower()}')
    return delete_zero_in_dates(date_str)


def delete_zero_in_dates(date):
    return re.sub("^0", "", date)
