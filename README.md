**Web Ui tests**

The framework used is pytest (https://habr.com/ru/post/448782/), with the following commands to run the tests:
- To run all tests in the repository:
`pytest`
- To run tests for a specific page (e.g., /analytics/):
`pytest src/tests/test_analytics_page.py::TestAnalyticsPage`
- To run a single test: 
`pytest src/tests/test_analytics_page.py::TestAnalyticsPage::test_web_ui_45_check_analyticts_page_locators`
- To run on the beta environment:
`pytest --beta`

The test run command for the runner is located in the .gitlab-ci.yml file.

By default, Chrome is opened on a remote machine via RemoteWebDriver. The settings are in the file settings.py:
- For remote execution, RemoteWebDriver is used in PARAMS['driver'].
- For local execution, the appropriate driver from selenium.webdriver needs to be selected and specified in PARAMS['driver'].
- DesiredCapabilities are the parameters that need to be used for configuring the browser session. Locally, these should match the selected selenium.webdriver.
- For local execution, the path to the driver executable should be specified in PARAMS['driver_data'] (the folder settings already contains Chrome for Windows and Linux).

Tests are run remotely on Selenoid (description: https://aerokube.com/selenoid/) You can join the session, go full screen, and intervene in the execution process.
