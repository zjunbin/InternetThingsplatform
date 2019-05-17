#  coding utf-8
# @time      :2019/5/59:52
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :VManagement_Locator.py
from selenium.webdriver.common.by import By

class VManagement_Locator:
    # 更多功能菜单
    mor =(By.XPATH, "//img[@id='morefun']")
    # 车辆管理菜单
    bicycle_menu = (By.XPATH,"//div[@id='divMenu_Icon']//a[@rel='211']")
    # 车辆详情
    bicycle_Details =(By.XPATH, "//td//input[@type='button' and @data-value='5' and @title='详情']")