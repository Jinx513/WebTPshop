import json
import time

from selenium import webdriver


# 1.定义工具类
class DriverUtils:
    # 私有变量，用来存储浏览器驱动对象
    __driver = None

    __openkey = False

    # 2.1定义获取浏览器驱动对象的方法
    # a、实现基本获取浏览器驱动的方法
    # b、为了方便其它地方调用，不想每次都实例化，则将方法定义为类级别的方法
    # c、为了保障整个测试用例执行过程中所操作的浏览器对象的唯一性，添加判断条件

    # 容易出错的地方
    # 1.在if中的代码不要写成cls.driver
    # 2.if中的代码和return的对齐方式
    # 3.忘记写return
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.implicitly_wait(10)
            cls.__driver.maximize_window()
        return cls.__driver

    # 2.2定义关闭浏览器驱动对象的方法
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None and cls.__openkey is False:
            time.sleep(3)
            cls.__driver.quit()
            cls.__driver = None

    @classmethod
    def change_openkey(cls, key):
        cls.__openkey = key


# 封装获取弹出框信息方法
def get_tip_msg():
    msg = DriverUtils.get_driver().find_element_by_css_selector('.layui-layer-content').text
    print("结果信息为：", msg)
    return msg


# 动态获取json数据并组装成parameterized的数据格式
def build_case_data(file_path):
    login_case_key = []
    login_case_data = []
    # login_data = []
    with open(file_path, encoding="utf-8") as f:
        # 加载json的数据
        case_data = json.load(f)
        # 遍历json数据对象的键值
        for test_data in case_data.values():
            # 遍历第一组value的键值
            for test_key in test_data:
                # 降所有的键值存储到login_case_key的空列表内，供后续使用
                login_case_key.append((test_key))
            print(login_case_key)
            # 只需要获取到其中一个用户的数据格式即可
            break
        # print(login_case_key)

        for test_data_1 in case_data.values():
            # 用来存储每次用例所需的数据，临时列表
            login_data = []
            # 根据键数量来循环获取test_data_1所遍历出来的值
            for i in range(len(login_case_key)):
                # login_case_key 表示第一获取回来的每一组数据的键值
                login_data.append(test_data_1.get(str(login_case_key[i])))
                print(login_data)
                # print(login_data)
            # 将第一次遍历的数据列表以一个元素添加到login_case_data空列表中，不会被清除
            login_case_data.append(login_data)
        print(login_case_data)
        # login_case_data 表示最终组装数据
    return login_case_data


def Get_data(fliename):
    test_list = []
    with open(fliename, encoding='utf-8') as f:
        login_data = json.load(f)
        for i in login_data.values():
            data_list = [x for x in i.values()]
            test_list.append(data_list)
    return test_list
