from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_element import BaseElement
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.locator import Locator

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


import time


class SignUpPage(BasePage):
    url = "https://github.com/signup"
    id = "login"

    @property
    def email_field(self):
        locator = Locator(By.ID, "email")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_error(self):
        locator = Locator(By.CSS_SELECTOR, "p#email-err > p")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_continue_button(self):
        locator = Locator(By.XPATH, "//div[@id='email-container']/div[2]/button")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_field(self):
        locator = Locator(By.ID, "password")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_error(self):
        locator = Locator(By.XPATH, "//p[@id='password-err']/p[1]")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def password_continue_button(self):
        locator = Locator(By.XPATH, "//div[@id='password-container']/div[2]/button")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_field(self):
        locator = Locator(By.ID, "login")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_continue_button(self):
        locator = Locator(By.XPATH, "//div[@id='username-container']/div[2]/button")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def username_error(self):
        locator = Locator(By.XPATH, "//p[@id='login-err']/div/div")
        return BaseElement(driver=self.driver, locator=locator)

