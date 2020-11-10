import pytest
import yaml
from python.Cal import Cal
from decimal import Decimal
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

class TestCal():
    # @pytest.fixture()
    # def start(self):
    #     self.cal = Cal()
    #
    #
    # @pytest.mark.parametrize(["a", "b", "expe"], yaml.safe_load(open("datas/testdata.yml")))
    # def calc_add(self, start, a, b, expe):
    #     # self.cal = Cal()
    #     if isinstance(a, float) or isinstance(b,float):
    #         assert expe == float(self.cal.add(Decimal(str(a)), Decimal(str(b))))
    #     else:
    #         assert expe == self.cal.add(a, b)
    #     # print(a, b, expe)
    #
    # @pytest.mark.parametrize(["a", "b", "expe"], yaml.safe_load(open("datas/div.yml")))
    # def calc_div(self, start, a, b, expe):
    #     # self.cal = Cal()
    #     assert expe == self.cal.div(a, b)
    #
    # def test_one(self):
    #     print("test_one")
    #

    def test_getstep(self):
       options = Options()
       options.debugger_address = "127.0.0.1:9222"
       self.driver = webdriver.chrome(options)
       self.driver.get("https://www.baidu.com")
        # with open("datas/steps.yml") as f:
        #     return yaml.safe_load(f)


    def test_case(self):
        steps1 = self.getstep()
        for step in steps1:
            if 'add' == step:
                self.cal.add(a, b)





