import pytest
from pageObjects.HomePage import HomePage
from test_data.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, get_data):
        log = self.get_logger()

        homepage = HomePage(self.driver)
        log.info("first name is "+get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["lastname"])
        homepage.get_password().send_keys("123456")

        homepage.get_checkbox().click()

        self.select_option_by_text(homepage.get_gender_form(), get_data["gender"])

        homepage.get_submit_button().click()

        alert_text = homepage.get_message().text
        assert "Success" in alert_text

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
