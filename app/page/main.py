from app.page.basepage import BasePage
from app.page.memberlist import Memberlist
from appium.webdriver.common.mobileby import MobileBy


class Main(BasePage):

    def goto_memberlist(self):
        #点击通讯录
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return Memberlist(self._driver)