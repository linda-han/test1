from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = [(MobileBy.XPATH, '//*[@text="确认"]'), (MobileBy.XPATH, '//*[@text="下次再说"]'),
                   (MobileBy.XPATH, '//*[@text="确定"]')]
    def __init__(self, driver:WebDriver):
        self._driver = driver


    def find(self, locator, value):

        try:
            element = self._driver.find_element(locator, value)
            return element



        except:
            for ele in self._black_list:
                element_list = self._driver.find_elements(*ele)

                if len(element_list)>0:
                    element_list[0].click()

                    return self.find(locator, value)


