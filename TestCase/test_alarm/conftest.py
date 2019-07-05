#  coding utf-8
# @time      :2019/6/25 13:46
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :conftest.py.py
import pytest
from selenium import webdriver
from Testdatas import common_data as cd
from  PageObject.login_page import LoginPage
from Testdatas import login_datas as ld
from PageObject.MoreFunctionMenu import MoreFunctionMenu
from PageLocator.menu_locator import Menu



@pytest.fixture
def alarm_conf():
    global driver
    # 前置条件
    driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
    driver.maximize_window()
    driver.get(cd.login_url)
    LoginPage(driver).Login(ld.success_data['username'], ld.success_data['pwd'], ld.success_data['code'])
    MoreFunctionMenu(driver=driver).click_menu(locator=Menu.Alarm_menu)
    yield driver  # 分隔符
    # 后置条件
    driver.quit()