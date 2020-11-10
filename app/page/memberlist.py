from app.page.add_member import Add_Member
from app.page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Memberlist(BasePage):


    def goto_add_member(self):
        #点击添加成员
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return Add_Member(self._driver)