#  coding utf-8
# @time      :2019/5/1516:42
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :MoreFunctionMenu.py
from common.basepage import BasePage
from PageLocator.menu_locator import Menu as lo


class MoreFunctionMenu(BasePage):

    def click_menu(self,locator):
        self.wait_element_Visible(locator=locator)
        self.click_element(model_name="",locator=locator)
