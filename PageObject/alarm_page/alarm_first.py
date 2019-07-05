#  coding utf-8
# @time      :2019/6/24 17:09
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :alarm_first.py
from common.basepage import BasePage
from PageLocator.Alarm_locator import Alarm as loc
from Testdatas import common_data

class AlarmPage(BasePage):

    def alarm_first(self, value):
        self.switch_iframe(iframe=loc.alarm_page)
        self.wait_element_Visible(locator=loc.idcard,model_name='接警第一步')
        self.input_text(model_name='接警第一步输入信息',locator=loc.idcard,value=value)
        self.click_element(model_name='接警第一步信息提交提交',locator=loc.btn)

    def get_message(self):
        self.switch_iframe(iframe=loc.alarm_page)
        self.wait_element_Visible(locator=loc.lblResult,model_name='')
        ele = self.get_element_text(locator=loc.lblResult,model_name='')
        return ele
