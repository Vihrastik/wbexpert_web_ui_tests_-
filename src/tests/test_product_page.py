from src.pages.product_page import ProductPage


class TestProductPage:

    def test_web_ui_49_check_product_page_locators(self, auth_by_paid_tariff, browser):
        product_page = ProductPage(browser)
        product_page.open()
        product_page.wait_preloader_to_hide()
        product_page.check_all_elements(is_assert_displayed=False)

    def test_web_ui_50_check_product_page_trial_message(self, auth_by_trial_tariff, browser):
        product_page = ProductPage(browser)
        product_page.open()
        product_page.wait_preloader_to_hide()
        product_page.check_all_elements(is_assert_displayed=True)
