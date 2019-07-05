#  coding utf-8
# @time      :2019/6/25 10:25
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :alarm_three.py
import time

from common.basepage import BasePage
from PageLocator.Alarm_locator import Alarm as loc

class AlarmThreePage(BasePage):

    def alarm_stree(self, reporterName, reporterMobel, lostTime, endCaseReason, remarks, lostPlace):
        self.wait_element_Visible(locator=loc.reporterName,model_name='填写接警信息')
        self.input_text(model_name='填写接警信息',locator=loc.reporterName,value=reporterName)
        self.input_text(model_name='填写接警信息', locator=loc.reporterMobel, value=reporterMobel)
        self.operating_time(locator=loc.lostTime,value=lostTime)
        self.selector(locator=loc.endCaseReason,model_name='',value=endCaseReason,type='text')
        self.input_text(model_name='填写接警信息', locator=loc.remarks, value=remarks)
        self.input_text(model_name='填写接警信息', locator=loc.lostPlace, value=lostPlace)
        self.random_element(locator=loc.lngLat)
        self.click_element(model_name='填写接警信息',locator=loc.btnNext3)

    def get_message(self):
        self.wait_element_Visible(locator=loc.alarm_err_message,model_name='接警信息填写')
        text = self.get_element_text(model_name='接警信息填写',locator=loc.alarm_err_message)
        return text