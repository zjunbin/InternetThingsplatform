#  coding utf-8
# @time      :2019/6/25 13:44
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_0_alarm.py
import pytest
from PageObject.index_page import IndexPage
from PageObject.alarm_page.alarm_first import AlarmPage
from Testdatas import alarm_datas as data


@pytest.mark.usefixtures("alarm_conf")
class TestAlarmFrist:
    @pytest.mark.alarm_moke
    def test_0(self, alarm_conf):
        AlarmPage(driver=alarm_conf).alarm_first(value='13051667963')
        assert (IndexPage(driver=alarm_conf).alarm_User_Authentication_Exists())

    # @pytest.mark.parametrize("item",  data.data_error)
    # def test_data_error(self, item, alarm_conf):
    #     AlarmPage(driver=alarm_conf).alarm_first(item['number'])
    #     text = AlarmPage(alarm_conf).get_message()
    #     assert  text == item['excepted']
