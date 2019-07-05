#  coding utf-8
# @time      :2019/6/25 10:46
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :alarm_two.py
from common.basepage import BasePage
from PageLocator.Alarm_locator import Alarm as loc


class alarmTwo(BasePage):

    def alarm_two(self):
        self.wait_element_Visible(model_name='接警选择车辆',locator=loc.btnNext2)
        self.click_element(model_name='接警选择车辆',locator=loc.btnNext2)