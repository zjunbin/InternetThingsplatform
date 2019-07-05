#  coding utf-8
# @time      :2019/5/1516:42
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :MoreFunctionMenu.py
from common.basepage import BasePage
from PageLocator.menu_locator import Menu


class MoreFunctionMenu(BasePage):

    def click_menu(self,locator):
        self.wait_element_Visible(locator=Menu.mor)
        self.click_element(model_name="更多功能菜单",locator=Menu.mor)
        self.wait_element_Visible(locator=locator,model_name='选择功能')
        self.click_element(model_name='选择功能',locator=locator)
