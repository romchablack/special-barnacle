from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_element import BaseElement
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.locator import Locator


class SignInPage(BasePage):
    url = "https://github.com/login"

    @property
    def login_field(self):
        locator = Locator(By.ID, 'login_field')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = Locator(By.ID, 'password')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sign_in_btn(self):
        locator = Locator(By.NAME, 'commit')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def login_failed_alert(self):
        locator = Locator(By.CSS_SELECTOR, "div.js-flash-alert")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def forgot_password_link(self):
        locator = Locator(By.LINK_TEXT, "Forgot password?")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def create_account_link(self):
        locator = Locator(By.LINK_TEXT, "Create an account")
        return BaseElement(driver=self.driver, locator=locator)
