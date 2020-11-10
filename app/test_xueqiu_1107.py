
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Search:
    def setup_class(self):
        print("setup_class")
        cap={}
        cap["platformName"] = "android"
        cap["deviceName"] =  "127.0.0.1:7555"
        cap["appPackage"] = "com.xueqiu.android"
        cap["appActivity"] = ".view.WelcomeActivityAlias"
        cap["noReset"] = " True"
        cap["skipDeviceInitialization"] = "True"
        cap["skipServerInstallation"] = "True"
        cap["unicodeKeyBoard"] = "True"
        cap["resetKeyBoard"] = "True"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")
        self.driver.find_element(By.ID,"com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize("searchkey, searchresult", [("alibaba","阿里巴巴"),("jd","京东")])
    def test_search(self, searchkey, searchresult):
        el7 = self.driver.find_element(By.ID,"com.xueqiu.android:id/tv_search")
        el7.click()
        el8 = self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text")
        el8.send_keys(searchkey)
        #el9= self.driver.find_element(By.ID,searchresult)
        #el9.click()
        #el10 = self.driver.find_element(By.XPATH,f"//*[@text={searchresult} and @class='android.widget.TextView']//..//..//*[@text='加自选']")
        #el10.click()

