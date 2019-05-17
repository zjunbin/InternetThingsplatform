#  coding utf-8
# @time      :2019/5/1515:11
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :Alarm_locator.py
from selenium.webdriver.common.by import By



class Alarm:


    #  输入框元素
    idcard = (By.XPATH,"//input[@id='txtIDCard']")
    # 提交按钮元素
    btn = (By.XPATH,"//input[@id='btnNext1']")
    # 身份证、手机号异常元素
    lable_error = (By.XPATH,"//label[@id='lblResult']")
    #身份确认弹出框元素
    aui_title = (By.XPATH,"//div[text()='身份确认']")
    # 接警菜单
    menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='221']")
    # 接警页面iframe
    alarm_page = 221

