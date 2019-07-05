#  coding utf-8
# @time      :2019/6/24 17:19
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :alarm_dem.py
import pytest as pytest

from common.basepage import BasePage
from PageLocator.Alarm_locator import Alarm as loc



class AlarmDem(BasePage):

    def alarm_dem(self, password):
        self.wait_element_Visible(locator=loc.txtPwd,model_name='接警确认')
        self.input_text(model_name='接警确认',locator=loc.txtPwd,value=password)
        self.click_element(model_name='接警确认',locator=loc.button_determine)

    def get_err_message(self):
        self.wait_element_Visible(locator=loc.lblMsg,model_name='接警错误提示')
        text = self.get_element_text(model_name='接警错误提示',locator=loc.lblMsg)
        return text
