# 对象库层
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self):
        super().__init__()
        # 加入购物车
        self.xiaomi = (By.CSS_SELECTOR, "a[onclick*='AjaxAddCart(104,']")

    def find_xiaomi(self):
        return self.find_elt(self.xiaomi)

class SearchHandler:
    def __init__(self):
        self.search_page = SearchPage()
    def click_Search(self):
        self.search_page.find_xiaomi().click()
class SearchProxy:
    def __init__(self):
        self.search_handler = SearchHandler()
    def test_search(self):
        self.search_handler.click_Search()