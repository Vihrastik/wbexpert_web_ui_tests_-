from src.pages.docs.license_page import LicensePage
from src.pages.docs.privacy_policy_page import PrivacyPolicyPage
from src.pages.docs.terms_of_use_page import TermsOfUsePage


class TestTermsOfUsePage:

    def test_web_ui_14_check_terms_of_use_page(self, browser):
        terms_page = TermsOfUsePage(browser)
        terms_page.open()
        terms_page.check_all_elements()


class TestLicensePage:

    def test_web_ui_15_check_license_page(self, browser):
        license_page = LicensePage(browser)
        license_page.open()
        license_page.check_all_elements()


class TestPrivacyPolicyPage:

    def test_web_ui_16_check_confidentiality_page(self, browser):
        confidentiality_page = PrivacyPolicyPage(browser)
        confidentiality_page.open()
        confidentiality_page.check_all_elements()
