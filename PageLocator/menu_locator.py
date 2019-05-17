#  coding utf-8
# @time      :2019/5/1516:44
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :menu_locator.py
from selenium.webdriver.common.by import By

class Menu:

    # 接警菜单
    alarm_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='221']")
    # 车辆登记菜单
    registration_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']")
    # 车辆管理菜单
    management_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='211']")
    # 组织机构菜单
    organization_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='411']")
    # 警员管理菜单
    PoliceOfficer_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='412']")