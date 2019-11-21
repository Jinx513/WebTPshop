
from selenium.webdriver.common.by import By

from base.base_page import BasePage


# 对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.ID, 'username')
        # 密码输入框
        self.password = (By.ID, 'password')
        # 验证码输入框
        self.verfiy_code = (By.ID, 'verify_code')
        # 登陆按钮
        self.submit_btn = (By.NAME, 'sbtbutton')

    def  find_username(self):
        return self.find_elt(self.username)
    def find_password(self):
        return self.find_elt(self.password)
    def find_verfiy_code(self):
        return self.find_elt(self.verfiy_code)
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)

#操作层
class LoginHandler():
    def __init__(self):
        self.login = LoginPage()
    def input_username(self,username):
        self.login.find_username().send_keys(username)

    def input_password(self,password):
        self.login.find_password().send_keys(password)
    def input_verfiy(self,verfiy_code):
        self.login.find_verfiy_code().send_keys(verfiy_code)
    def coick_submit(self):
        self.login.find_submit_btn().click()

#业务层
class LoginProxy:
    def __init__(self):
        self.login_handler = LoginHandler()

    def test_login_cg(self,username,password,verfiy_code):
        self.login_handler.input_username(username)
        self.login_handler.input_password(password)
        self.login_handler.input_verfiy(verfiy_code)
        self.login_handler.coick_submit()