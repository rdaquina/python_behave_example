import os, sys
import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from context.config import settings

_file_path = os.path.dirname(__file__)

def browser_config(context, browser_name):
    if browser_name == "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Firefox(firefox_options=option)
        
        return driver
    
    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        option.add_argument("--test-type")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(chrome_options=option)

        return driver

    if browser_name == "headless-chrome":
        option = webdriver.ChromeOptions()
        option.headless = True
        option.add_argument("--no-sandbox")
        option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        option.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(chrome_options=option)

        return driver

    else:
        raise Exception("No browser foun in testsettings.json")

def before_scenario(context, scenario):
    browser_name = settings.browser
    context.browser = browser_config(context, browser_name)
    context.browser.implicitly_wait(5)
    context.browser.set_page_load_timeout(100)
    context.browser.get(settings.portal_url)

def after_scenario(context, scenario):
    context.browser.close()