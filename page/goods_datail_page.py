# 对象库层
import time
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils import DriverUtils



class DatailPage(BasePage):
    def __init__(self):
        super().__init__()
        # 加入购物车
        self.gouwu = (By.ID, "join_cart")
        self.iframe = (By.ID,"layui-layer-iframe1")
        self.jiesuan = (By.CLASS_NAME,"ui-button-122")

    def find_gouwu(self):
        return self.find_elt(self.gouwu)
    def find_iframe(self):
        return self.find_elt(self.iframe)
    def find_jiesuan(self):
        return self.find_elt(self.jiesuan)


class DatailHandler:
    def __init__(self):
        self.datail_page = DatailPage()
    def click_gouwu(self):
        self.datail_page.find_gouwu().click()
    def click_iframe(self):
        DriverUtils.get_driver().switch_to.frame(self.datail_page.find_iframe())
    def click_jiesuan(self):
        self.datail_page.find_jiesuan().click()

class DatailProxy:
    def __init__(self):
        self.datail_handler = DatailHandler()
    def test_datail(self):
        self.datail_handler.click_gouwu()
        time.sleep(5)
        self.datail_handler.click_iframe()
        self.datail_handler.click_jiesuan()