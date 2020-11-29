from enum import Enum
from selenium.webdriver import (
    Chrome,
    Firefox,
    Edge,
    Opera,
    Safari,
    Remote,
)
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BASE_URL_MASTER = 'http://wbexpert.ru/'
BETA_BASE_URL = ''
TELEBOT_TOKEN = ''
CHANNELS_TELEBOT = []


class DriverTypes:
    def __init__(self, path, version):
        self.path = path
        self.version = version


class DriverTypesData(Enum):
    chrome = DriverTypes('chromedriver', '74')
    remote = DriverTypes('url:4444/wd/hub', '')


PARAMS = {
    'driver': Remote,
    'desired_capabilities': DesiredCapabilities.CHROME,
    'driver_data': DriverTypesData.remote,
}
