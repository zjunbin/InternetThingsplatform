#  coding utf-8
# @time      :2019/5/614:59
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :conftest.py.py
import pytest
from selenium import webdriver
from Testdatas import common_data as cd
from  PageObject.login_page import LoginPage
from Testdatas import login_datas as ld

driver = None

# @pytest.fixture(scope='class')
# def prepara_env():
#     global driver
#     # 前置条件
#     #  测试类级别
#     driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
#     driver.maximize_window()
#     driver.get(cd.login_url)
#     yield #分隔符
#     # 后置条件
#     driver.quit()


@pytest.fixture
def prepara_env():
    global driver
    # 前置条件
    driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
    driver.maximize_window()
    driver.get(cd.login_url)
    yield driver  # 分隔符
    # 后置条件
    driver.quit()


@pytest.fixture(scope='class')
def global_login():
    global driver
    # 前置条件
    driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
    driver.maximize_window()
    driver.get(cd.login_url)
    LoginPage(driver).Login(ld.success_data['username'], ld.success_data['pwd'], ld.success_data['code'])
    yield driver  # 分隔符
    # 后置条件
    driver.quit()


@pytest.fixture
def global_page():

    yield
    driver.refresh()