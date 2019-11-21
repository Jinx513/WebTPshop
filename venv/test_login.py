
# 2.定义测试类
import unittest

from page.goods_datail_page import DatailProxy
from page.goods_search_page import SearchProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtils


class TestLogin(unittest.TestCase):

    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        cls.login_page = LoginProxy()
        cls.index_page = IndexProxy()
        cls.search_page = SearchProxy()
        cls.datail_page = DatailProxy()
    @classmethod
    def tearDownClass(cls):
        pass
        # DriverUtils.quit_driver()

    def setUp(self):
        self.driver.get('http://localhost/')
        self.driver.find_element_by_class_name('red').click()

    def test_login(self):
        #登入成功
        self.login_page.test_login_cg("13700000001","123456","8888")
        #搜索小米
        self.index_page.test_index("小米")
        #进入详情页
        self.search_page.test_search()
        self.datail_page.test_datail()