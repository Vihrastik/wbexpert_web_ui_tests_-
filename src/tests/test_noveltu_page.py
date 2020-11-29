from src.pages.novelty_page import NoveltyPage


class TestNoveltyPage:

    def test_web_ui_51_check_novelty_page_locators(self, auth_by_paid_tariff, browser):
        novelty_page = NoveltyPage(browser)
        novelty_page.open()
        novelty_page.wait_preloader_to_hide()
        novelty_page.check_all_elements(is_assert_displayed=False)

    def test_web_ui_52_check_novelty_page_trial_message(self, auth_by_trial_tariff, browser):
        novelty_page = NoveltyPage(browser)
        novelty_page.open()
        novelty_page.wait_preloader_to_hide()
        novelty_page.check_header_elements()
        novelty_page.check_payment_assert(is_assert_displayed=True)
        novelty_page.assert_data_not_displayed()
