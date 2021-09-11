from selenium.webdriver.common.by import By

class Locator:
    def __init__(self,locator_type, selector) -> None:
        self.locator_type = locator_type
        self.selector = selector

"""Home page element locators"""
class HomePageLocators:
    title = Locator(By.XPATH,"//*[@id=\"title\"]")
    load_delay = Locator(By.XPATH, "//*[@id=\"overview\"]/div/div[1]/div[4]/h3/a")
    click = Locator(By.XPATH, "//*[@id=\"overview\"]/div/div[2]/div[3]/h3/a")
    text_input = Locator(By.XPATH,"//*[@id=\"overview\"]/div/div[2]/div[3]/h3/a")
    verify_text = Locator(By.XPATH,"//*[@id=\"overview\"]/div/div[3]/div[3]/h3/a")
    progress_bar = Locator(By.XPATH, "//*[@id=\"overview\"]/div/div[3]/div[4]/h3/a")

"""Load Delay page element locators"""
class LoadDelayPageLocators:
    LoadDelaysTitle = Locator(By.CSS_SELECTOR, "body > section > div > h3")
    LoadDelaysButton = Locator(By.CSS_SELECTOR, "body > section > div > button")

"""Click page element locators"""
class ClickPageLocators:
    ClickPageTitle = Locator(By.XPATH,"/html/body/section/div/h3")
    ClickPageButton = Locator(By.ID,"badButton")

"""Text Input page element locators"""
class TextInputLocators:
    TextInputTitle = Locator(By.XPATH,"/html/body/section/div/h3")
    TextInputField = Locator(By.ID,"newButtonName")
    TextInputButton = Locator(By.ID,"updatingButton")

"""Verify Text page element locators"""
class VerifyTextLocators:
    VerifyTextTitle = Locator(By.XPATH,"/html/body/section/div/h3")

"""Progress Bar page element locators"""
class ProgressBarLocators:
    ProgressBarTitle = Locator(By.XPATH,"/html/body/section/div/h3")
    ProgressBarStartButton = Locator(By.ID,"startButton")
    ProgressBarStopButton = Locator(By.ID,"stopButton")
    ProgressBarProgressBar = Locator(By.ID,"progressBar")
    ProgressBarProgressBar = Locator(By.ID,"result")