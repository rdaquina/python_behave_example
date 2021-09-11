from pages.locators import TextInputLocators
from pages.base_page import BasePage
from behave import *
import selenium.webdriver as driver

@when('I input {text} on text input field')
def I_input_text_on_text_input_field(context, text):
    input_text_field = BasePage.locate_element(context, TextInputLocators.TextInputField)
    input_text_field.send_keys(text)

@when('I press the Button that should change it\'s name based on input value')
def I_press_the_Button_tha_should_change_its_name_based_on_input_value(context):
    text_input_button = BasePage.locate_element(context, TextInputLocators.TextInputButton)
    text_input_button.click()

@then('The Button should have {text} in it')
def The_Button_should_have_text_in_it(context, text):
    text_input_button = BasePage.locate_element(context, TextInputLocators.TextInputButton)
    if (str(text_input_button.text) != str(text)):
        raise AssertionError('Expected button string was different than expected')