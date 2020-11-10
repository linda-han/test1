from app.page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Add_Member(BasePage):



    def goto_manual_addmember(self):


        from app.page.manual_addmember import Manual_Addmember

        # 点击手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return Manual_Addmember(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text