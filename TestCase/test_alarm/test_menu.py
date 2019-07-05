#  coding utf-8
# @time      :2019/6/25 16:14
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_menu.py
import pytest
from selenium import webdriver
from Testdatas import common_data as cd
from  PageObject.login_page import LoginPage
from Testdatas import login_datas as ld
from PageObject.MoreFunctionMenu import MoreFunctionMenu
from PageLocator.menu_locator import Menu
from common.basepage import BasePage


class testMenu():

    def as1(self):
        driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
        driver.maximize_window()
        driver.get(cd.login_url)
        from PageObject.login_page import LoginPage
        LoginPage(driver).Login(ld.success_data['username'], ld.success_data['pwd'], ld.success_data['code'])
        return driver

    def test_01(self):
        driver =self.as1()
        MoreFunctionMenu(driver=driver).click_menu(locator=Menu.Alarm_menu)

if __name__ == '__main__':
    testMenu().test_01()