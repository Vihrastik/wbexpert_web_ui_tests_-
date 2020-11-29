import time

from selenium.common.exceptions import WebDriverException

from src.common.consts import WbException


def wait_until(exception_message: str, wait_time: int = 30, frequency: int = 5):
    def decorator(function_to_decorate):
        def wrapper(*args, **kwargs):
            end_time = time.time() + wait_time
            err_str = ''
            while time.time() < end_time:
                try:
                    result = function_to_decorate(*args, **kwargs)
                    if result:
                        return result
                except WebDriverException as e:
                    if e.msg:
                        err_str = f'Возможная ошибка: {e.msg}'
                time.sleep(frequency)
            raise WbException(f'За {wait_time} секунд {exception_message}.\n{err_str}')
        return wrapper
    return decorator
