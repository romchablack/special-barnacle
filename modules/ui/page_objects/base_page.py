from selenium import webdriver


class BasePage():
    url = None

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def go(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def check_title(self):
        return self.driver.title
