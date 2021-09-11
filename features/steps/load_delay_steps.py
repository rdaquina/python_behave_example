from pages.locators import LoadDelayPageLocators
from pages.base_page import BasePage
from behave import *

@then('I click the Load Delay button')
def i_click_the_click_test_page_button(context):
    load_delay_button = BasePage.locate_element(context, LoadDelayPageLocators.LoadDelaysButton)
    load_delay_button.click()