import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestSearch():
    def setup_class(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True,
            "skipDeviceInitialization":True,
            "skipServerInstallation":True

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown_class(self):
        print("teardown")
        self.driver.quit()

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")




    def test_addmember(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']//..//*[@class='android.widget.EditText']").send_keys("霍格沃茨name1")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']//..//*[@text='男']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机　']//..//*[@class='android.widget.EditText']").send_keys("13476285854")

        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()



