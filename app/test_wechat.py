
from appium import webdriver


class Test_Chat:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            #com.tencent.mm /.ui.LauncherUI
            "appPackage": "com.tencent.mm",
            "appActivity": ".ui.LauncherUI",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass

    # self.driver.quit()

    def test_wechat(self):

        el2 = self.driver.find_element_by_id("com.tencent.mm:id/f8y")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.mm:id/bhn")
        el3.send_keys("明月")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView")
        el4.click()
        el5 = self.driver.find_element_by_id("com.tencent.mm:id/al_")
        el5.click()
        el5.send_keys("你好呀")
        el6 = self.driver.find_element_by_id("com.tencent.mm:id/anv")
        el6.click()

