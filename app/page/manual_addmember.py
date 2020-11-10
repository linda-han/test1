from app.page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Manual_Addmember(BasePage):



    def input_name(self):
        self.find(MobileBy.XPATH, "//*[@text='姓名　']//..//*[@class='android.widget.EditText']").send_keys(
            "霍格沃茨name1")
        return self

    def input_gender(self):
        self.find(MobileBy.XPATH, "//*[@text='性别']//..//*[@text='男']").click()
        self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self

    def input_phonenumber(self):
        self.find(MobileBy.XPATH, "//*[@text='手机　']//..//*[@class='android.widget.EditText']").send_keys(
            "13476285854")
        return self

    def save(self):

        from app.page.add_member import Add_Member
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return Add_Member(self._driver)
