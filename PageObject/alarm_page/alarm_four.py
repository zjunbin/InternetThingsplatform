#  coding utf-8
# @time      :2019/6/25 10:47
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :alarm_four.py

from common.basepage import BasePage
from PageLocator.Alarm_locator import Alarm as loc


class AlarmFourPage(BasePage):

    def test_1(self):
        self.wait_element_Visible(locator=loc.btnNext4)
        self.click_element(model_name='接警第四步',locator=loc.btnNext4)

    def get_messgage(self):
        self.get_element_text(model_name='接警第四步',locator=loc.finished)