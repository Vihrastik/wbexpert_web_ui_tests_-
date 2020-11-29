import os

import pytest
import telebot
from selenium.webdriver import (
    Chrome,
    Remote,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from simple_settings import settings

from src.common.consts import (
    UserData,
)
from src.common.consts import WbException
from src.common.grafana import send_metric_to_grafana
from src.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--beta", action="store_true", help="env: choose beta environment for tests")


@pytest.hookimpl
def pytest_configure(config):
    os.environ.setdefault('SIMPLE_SETTINGS', 'settings.settings')
    os.environ.setdefault('BASE_URL', settings.BETA_BASE_URL if config.getoption('beta') else settings.BASE_URL_MASTER)


@pytest.fixture(scope='function')
def browser():
    caps = settings.PARAMS['desired_capabilities']
    caps['loggingPrefs'] = {'performance': 'ALL'}

    if settings.PARAMS['driver'] == Chrome:
        options = Options()
        options.add_experimental_option('w3c', False)
        driver = settings.PARAMS['driver'](executable_path=settings.PARAMS['driver_data'].value.path,
                                           desired_capabilities=caps, options=options)
    elif settings.PARAMS['driver'] == Remote:
        caps['selenoid:options'] = {"enableVNC": True, "enableVideo": False}
        if settings.PARAMS['desired_capabilities'] == DesiredCapabilities.CHROME:
            options = Options()
            options.add_experimental_option('w3c', False)
            driver = settings.PARAMS['driver'](command_executor=settings.PARAMS['driver_data'].value.path,
                                               desired_capabilities=caps, options=options)
        else:
            driver = settings.PARAMS['driver'](command_executor=settings.PARAMS['driver_data'].value.path,
                                               desired_capabilities=caps)
    else:
        driver = settings.PARAMS['driver'](executable_path=settings.PARAMS['driver_data'].value.path,
                                           desired_capabilities=caps)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def auth_by_trial_tariff(browser):
    auth_page = LoginPage(browser)
    auth_page.open()
    auth_page.log_in(browser=browser,
                     login=UserData.trial_tariff.value.login,
                     password=UserData.trial_tariff.value.password)


@pytest.fixture(scope='function')
def auth_by_paid_tariff(browser):
    auth_page = LoginPage(browser)
    auth_page.open()
    auth_page.log_in(browser=browser,
                     login=UserData.paid_tariff.value.login,
                     password=UserData.paid_tariff.value.password)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    result = yield
    report = result.get_result()
    if report.outcome == 'failed':
        if report.longrepr and report.longrepr.reprcrash:
            error_message = f'⚡*В прогоне упали тесты*⚡️:\n\n💣 {report.head_line} с ошибкой:\n' \
                            f'```{report.longrepr.reprcrash.message.strip()}```'.replace("_", "\\_")
        else:
            error_message = f'⚡*В прогоне упали тесты*⚡️:\n\n💣 {report.head_line}'
        try:
            bot = telebot.TeleBot(settings.TELEBOT_TOKEN)
            for channel in settings.CHANNELS_TELEBOT:
                bot.send_message(channel, error_message, disable_web_page_preview=True, parse_mode='Markdown')
        except telebot.apihelper.ApiTelegramException:
            raise WbException('Не удалось отправить сообщение в телеграмм')


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter):
    yield
    all_tests = 0
    if 'passed' in terminalreporter.stats:
        passed_tests = len(terminalreporter.stats['passed'])
        send_metric_to_grafana(name='passed_tests', value=int(passed_tests))
        print(passed_tests)
        all_tests += passed_tests
    if 'failed' in terminalreporter.stats:
        failed_tests = len(terminalreporter.stats['failed'])
        send_metric_to_grafana(name='failed_tests', value=int(failed_tests))
        print(failed_tests)
        all_tests += failed_tests
    print(all_tests)
    send_metric_to_grafana(name='tests_amount', value=int(all_tests))
