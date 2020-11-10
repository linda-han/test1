import pytest
from appium import webdriver
from selenium.webdriver.common.by import By


class TestSearch():
    def setup_class(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
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
        self.driver.find_element(By.ID, "com.xueqiu.android:id/action_close").click()


    @pytest.mark.parametrize("searchkey, searchresult,searchtype", [("alibaba", "阿里巴巴","BABA"), ("jd", "京东","JD")])
    def test_search(self, searchkey, searchresult, searchtype):
        #点击搜索框
        el7 = self.driver.find_element(By.ID,"com.xueqiu.android:id/tv_search")
        el7.click()

        #搜索框输入搜索内容
        el8 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
        el8.send_keys(searchkey)

        #点击搜索结果
        el9 = self.driver.find_element(By.XPATH,f"//*[@text='{searchresult}']")
        el9.click()

        #加自选
        el10=self.driver.find_element(By.XPATH,f"//*[@text='{searchtype}']//..//..//..//*[@text='加自选']")
        el10.click()

        el11= self.driver.find_element(By.ID, "com.xueqiu.android:id/followed_btn")
        assert "已添加"==el11.get_attribute("text")

