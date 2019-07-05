#  coding utf-8
# @time      :2019/6/12 14:02
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test_1_orgmanaent.py
import pytest
from PageObject.OrganizationManagement import OrgManagemnet
from PageObject.login_page import LoginPage
from common.basepage import BasePage
from Testdatas import login_datas as ld


@pytest.mark.usefixtures("prepara_env")

class Test_OrgManaent:

    @pytest.mark.addnew
    def test_add_success(self,prepara_env):
        LoginPage(prepara_env).Login(ld.success_data['username'],ld.success_data['pwd'],ld.success_data['code'])
        OrgManagemnet(prepara_env).loginPage()
        OrgManagemnet(prepara_env).new_org(pcnumber= 'BJ1234', pcname='日月天地警务室', areas= '东城区', pltype='普通类型')
        text = OrgManagemnet(prepara_env).success_message()
        assert '添加成功!' == text
