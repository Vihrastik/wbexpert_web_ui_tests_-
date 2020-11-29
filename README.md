**Web Ui тесты wbexpert.ru**

Используется фреймворк pytest(https://habr.com/ru/post/448782/), команды для запуска тестов:
- запуск всех тестов в репозитории 
`pytest`
- запуск тестов для конкретной страницы (например, /analytics/)
`pytest src/tests/test_analytics_page.py::TestAnalyticsPage`
- запуск одного теста 
`pytest src/tests/test_analytics_page.py::TestAnalyticsPage::test_web_ui_45_check_analyticts_page_locators`
- запуск на бете
`pytest --beta`

Команда запуска тестов для ранера находится в файле .gitlab-ci.yml.

По умолчанию открывается Chrome на удаленной машине через RemoteWebDriver.
Настройки находятся в файле settings.py:
- для удаленного запуска используется RemoteWebDriver в PARAMS['driver']
- для локального запуска нужно выбрать нужный драйвер из selenium.webdriver и указать в PARAMS['driver']
- DesiredCapabilities - это параметры, которые нужно использовать для настройки сеанса браузера. Локально должны совпадать с выбранным selenium.webdriver.
- для локального запуска в PARAMS['driver_data'] нужно указать путь к исполняемому файлу драйвера (в папке settings уже лежит Chrome для винды и линукса).


Удаленно тесты запускаются на selenoid
(описание https://aerokube.com/selenoid/)
Можно зайти в сессию, открыть полный экран, вмешаться в процесс выполнения.

Для хранения текстового описания кейсов используется testlink