from selenium.webdriver.common.by import By

from base.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        #返回首页
        self.souye = (By.CSS_SELECTOR, "[class='home']")
        #搜索框
        self.sousuo_box = (By.ID,"q")
        #搜索按钮
        self.sousuo_annv = (By.CSS_SELECTOR,".ecsc-search-button")

    def  find_souye(self):
        return self.find_elt(self.souye)
    def find_sousuo_box(self):
        return self.find_elt(self.sousuo_box)
    def find_sousuo_annv(self):
        return self.find_elt(self.sousuo_annv)

class IndexHandler():
    def __init__(self):
        self.index_page = IndexPage()

    def click_souye(self):
        self.index_page.find_souye().click()
    def click_sousuo_box(self,shop):
        self.index_page.find_sousuo_box().send_keys(shop)
    def click_sousuo_annv(self):
        self.index_page.find_sousuo_annv().click()

class IndexProxy():
    def __init__(self):
        self.indexhandler = IndexHandler()

    def test_index(self,shop):
        self.indexhandler.click_souye()
        self.indexhandler.click_sousuo_box(shop)
        self.indexhandler.click_sousuo_annv()