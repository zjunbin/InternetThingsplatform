#  coding utf-8
# @time      :2019/7/5 13:41
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_2_PopTracking.py
import pytest
from PageObject.PopulationTracking import PopTracking
from Testdatas.PopTracking_data import PopTrackingData as  pd


@pytest.mark.usefixtures("global_login")
@pytest.mark.usefixtures("global_page")

class Test_PopTracking:
    @pytest.mark.poptracking
    # @pytest.mark.parametrize("item", pd.error_data)
    def test_0(self, global_login):
        # PopTracking(driver=global_login).Application(idCard=item['idCard'],startTime=item['startTime'],endtime=item['endtime'],applyCause=item['applyCause'])
        # assert PopTracking(driver=global_login).get_message() == item['excepted']
        PopTracking(driver=global_login).Application(idCard='140430199404286810', startTime='2019-12-1',
                                                     endtime='2019-12-21', applyCause='测试')

