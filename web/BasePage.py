from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from web.AddMembers import AddMembers


class BasePage():
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)


    def goto_addmembers(self):
        self.driver.find_element_by_class_name("index_service_cnt_item_title").click()
        return AddMembers(self.driver)