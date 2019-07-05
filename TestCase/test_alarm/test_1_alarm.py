#  coding utf-8
# @time      :2019/6/25 17:08
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_1_alarm.py
import pytest
from PageObject.index_page import IndexPage
from PageObject.alarm_page.alarm_first import AlarmPage
from PageObject.alarm_page.alarm_dem import AlarmDem
from Testdatas import alarm_datas as data


@pytest.mark.usefixtures("alarm_conf")
class TestAlarmFrist:
    @pytest.mark.alarm_moke2
    def test_0(self, alarm_conf):
        AlarmPage(driver=alarm_conf).alarm_first(value='13051667963')
        AlarmDem(alarm_conf).alarm_dem(password='123456')
        assert (IndexPage(alarm_conf).alarm_twopage_Exists())

    @pytest.mark.parametrize("item", data.alarm_dem_data)
    def get_error_message(self, alarm_conf, item):
        AlarmPage(driver=alarm_conf).alarm_first(value=item['password'])
        text = AlarmDem(driver=alarm_conf).get_err_message()
        assert text == item['excepted']
