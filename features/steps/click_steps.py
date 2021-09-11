from pages.locators import HomePageLocators, LoginPageLocators
from pages.base_page import BasePage
from datasource.datapool import DATA_ACCESS, MESSAGES
from behave import *
from nose.tools import assert_equals
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

@given('I am at the UI Test Automation Playground')
def i_am_at_login_page(context):
    BasePage.locate_element(BasePage, context, HomePageLocators.title)

# @when('I fill the username with {credential}')
# def i_fill_the_username_with_credential(context, credential, user='username'):
#     user = BasePage.datapool_read(BasePage, DATA_ACCESS, credential, user)
#     username_field = BasePage.get_element(BasePage, context, LoginPageLocators.access)
#     username_field.clear()
#     username_field.send_keys(user)

# @when('I fill the password with {credential}')
# def i_fill_the_password_with_credential(context, credential, password='password'):
#     password = BasePage.datapool_read(BasePage, DATA_ACCESS, credential, password)
#     password_field = BasePage.get_element(BasePage, context, LoginPageLocators.password)
#     password_field.clear()
#     password_field.send_keys(password)