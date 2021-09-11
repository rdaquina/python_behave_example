from pages.locators import ProgressBarLocators
from pages.base_page import BasePage
from behave import *
import re

@when('I click the Start Progress Bar button')
def i_click_the_Start_Progress_Bar_button(context):
    progress_bar_start_button = BasePage.locate_element(context, ProgressBarLocators.ProgressBarStartButton)
    progress_bar_start_button.click()

@when('The Progress Bar is at {progressbar}')
def The_Progress_Bar_is_at(context, progressbar):
    progress_bar = BasePage.locate_element(context, ProgressBarLocators.ProgressBarProgressBar)
    while progress_bar.text != progressbar:
        continue
    
@then('I click on the Stop Progress Bar button')
def I_click_on_the_Stop_Progress_Bar_button(context):
    progress_bar_stop_button = BasePage.locate_element(context, ProgressBarLocators.ProgressBarStopButton)
    progress_bar_stop_button.click()

@then('Result should be {result}')
def result_should_be(context, result):
    progress_bar_result = BasePage.locate_element(context, ProgressBarLocators.ProgressBarResult)
    regex_expression = re.compile(r'\d+')
    result_value = regex_expression.findall(progress_bar_result.text)
    if (result_value[0] != result):
        raise AssertionError("Result value is " + result_value[0] + " but expected value is " + result)