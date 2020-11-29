from src.pages.analytics_page import AnalyticsPage


class TestAnalyticsPage:

    def test_web_ui_45_check_analyticts_page_locators(self, auth_by_paid_tariff, browser):
        analytics_page = AnalyticsPage(browser)
        analytics_page.open()
        analytics_page.check_all_elements(is_assert_displayed=False)

    def test_web_ui_46_check_analyticts_page_trial_message(self, auth_by_trial_tariff, browser):
        analytics_page = AnalyticsPage(browser)
        analytics_page.open()
        analytics_page.check_all_elements(is_assert_displayed=True)
