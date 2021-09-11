from pages.locators import ClickPageLocators
from pages.base_page import BasePage
from behave import *
from pages.base_page import BasePage

@when('I click the Click Test Page button')
def i_click_the_click_test_page_button(context):
    click_page_button = BasePage.locate_element(context, ClickPageLocators.ClickPageButton)
    click_page_button.click()

@then('The button change class to Success')
def the_button_change_class_to_sucess(context):
    BasePage.locate_element(context, ClickPageLocators.ClickPageButtonSuccess)