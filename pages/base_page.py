from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self) -> None:
        super().__init__()

    def remove_space(data):
        return data.replace(' ','')


    def datapool_read(self, source, data, key):
        """Get a list of arguments named as 'data' on the 'source' and search the 'key' in that list"""
        data_args = source.get(self.remove_space(data))
        
        if data_args is not None:
            if data_args[0].get(key) is not None:
                return data_args[0].get(key)
            else:
                raise Exception("No matching results for data = " + str(data) + " for key = " + str(key))
        else:
            raise Exception("Data is None")

    def locate_element(context, locator):
        try:
            return WebDriverWait(context.browser, 20).until(EC.presence_of_element_located((locator.locator_type, locator.selector)))
        except TimeoutException:
            raise Exception("The element could not be found")

    def get_element(context, locator):
        return context.browser.find_element(locator.locator_type, locator.selector)