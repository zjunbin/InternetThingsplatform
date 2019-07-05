#  coding utf-8
# @time      :2019/6/26 9:50
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_2_alarm.py
from PageObject.alarm_page.alarm_three import AlarmThreePage
from PageObject.alarm_page.alarm_first import AlarmPage
from PageObject.alarm_page.alarm_dem import AlarmDem
from PageObject.alarm_page.alarm_two import alarmTwo
import pytest

@pytest.mark.usefixtures("alarm_conf")
class TestAlarmFrist:
    @pytest.mark.alarm_moke3
    def test_0(self, alarm_conf):
        AlarmPage(driver=alarm_conf).alarm_first('13051667963')
        AlarmDem(driver=alarm_conf).alarm_dem('123456')
        alarmTwo(driver=alarm_conf).alarm_two()
        AlarmThreePage(alarm_conf).alarm_stree(reporterName='',reporterMobel='',lostTime='2019-5-23 12:25:23',endCaseReason='东城区',remarks='丢失',lostPlace='北京丰台区')
