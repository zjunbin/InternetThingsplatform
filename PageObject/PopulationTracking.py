#  coding utf-8
# @time      :2019/7/5 10:48
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :PopulationTracking.py
import time

from PageLocator.menu_locator import Menu
from common.basepage import BasePage
from PageLocator.PopulationTracking_locator import PopulationTracking as loc



class PopTracking(BasePage):

    def Application(self, idCard, startTime, endtime, applyCause):
        self.wait_element_Visible(locator=Menu.mor)
        self.click_element(model_name="更多功能菜单", locator=Menu.mor)
        self.wait_element_Visible(locator=Menu.Population_tracking_menu, model_name='选择功能')
        self.click_element(model_name='选择功能', locator=Menu.Population_tracking_menu)
        self.switch_iframe(iframe=loc.ifram)
        self.wait_element_Visible(model_name='重点人口追踪',locator=loc.createApply)
        self.click_element(model_name='',locator=loc.createApply)
        self.input_text(model_name='',locator=loc.ownerIDCard,value=idCard)
        self.Keys_ENTER(locator=loc.ownerIDCard)
        self.operating_time(locator=loc.Mian_StartTime,value=startTime)
        # self.input_text(model_name='',locator=loc.minAndSec1_StartTime,value=mstarttime)
        self.operating_time(locator=loc.Mian_EndTime,value=endtime)
        # self.input_text(model_name='',locator=loc.minAndSec1_EndTime,value=mendtime)
        self.input_text(model_name='',locator=loc.applyCause,value=applyCause)
        self.click_element(model_name='',locator=loc.inc_affirm)
        time.sleep(10)

    def get_message(self):
        self.wait_element_Visible(locator=loc.error)
        ele = self.get_element_text(locator=loc.error)
        return ele