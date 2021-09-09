from selenium.webdriver.common.by import By

class Locator:
    def __init__(self,locator_type, selector) -> None:
        self.locator_type = locator_type
        self.selector = selector

"""Login page element locators"""
class LoginPageLocators:
    access = Locator(By.XPATH,"")