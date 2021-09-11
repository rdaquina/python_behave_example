from pages.locators import HomePageLocators, LoadDelayPageLocators, ClickPageLocators, TextInputLocators, ProgressBarLocators
from pages.base_page import BasePage
from behave import *

@given('I am at the UI Test Automation Playground')
def i_am_at_ui_test_automation_playground_page(context):
    BasePage.locate_element(context, HomePageLocators.title)

@when('I navigate to Load Delay test page')
def i_navigate_to_load_delay_test_page(context):
    load_delay_page_navigator = BasePage.locate_element(context, HomePageLocators.load_delay)
    load_delay_page_navigator.click()
    BasePage.locate_element(context, LoadDelayPageLocators.LoadDelaysTitle)

@given('I navigate to Click test page')
def i_navigate_to_click_test_page(context):
    click_page_navigator = BasePage.locate_element(context, HomePageLocators.click)
    click_page_navigator.click()
    BasePage.locate_element(context, ClickPageLocators.ClickPageTitle)

@given('I navigate to Text Input test page')
def i_navigate_to_text_input_test_page(context):
    text_input_page_navigator = BasePage.locate_element(context, HomePageLocators.text_input)
    text_input_page_navigator.click()
    BasePage.locate_element(context, TextInputLocators.TextInputTitle)

@given('I navigate to Progress Bar test page')
def i_navigate_to_progress_bar_test_page(context):
    progress_bar_page_navigator = BasePage.locate_element(context, HomePageLocators.progress_bar)
    progress_bar_page_navigator.click()
    BasePage.locate_element(context, ProgressBarLocators.ProgressBarTitle)

