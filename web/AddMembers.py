from web.BasePage import BasePage
class AddMembers():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def addmember(self):
        self.driver.