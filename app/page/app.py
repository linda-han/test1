from app.page.main import Main
from appium import webdriver


class App:

    def start(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True,
            "skipDeviceInitialization": True,
            "skipServerInstallation": True

        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self._driver.implicitly_wait(20)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)