#  coding utf-8
# @time      :2019/6/12 10:39
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :OrganizationManagement.py
import time

from common.basepage import BasePage
from PageLocator.OrgManagement import OrgManage as om


class OrgManagemnet(BasePage):

    def loginPage(self):
        self.wait_element_Visible(locator=om.mor,model_name="更多功能")
        self.click_element("更多功能",locator=om.mor)
        self.wait_element_Visible(locator=om.bicycle_menu,model_name="组织结构管理")
        self.click_element("组织结构管理",locator=om.bicycle_menu)

    def new_org(self,pcnumber,pcname,pltype,areas):
        self.switch_iframe(iframe=om.ifram411)
        self.switch_iframe(iframe=om.iframStaiton)
        self.click_element(model_name='新建按钮',locator=om.btnAdd)
        # self.switch_iframe(iframe=om.iframeDiv)
        self.switch_iframe(iframe=om.iframeAdd)
        self.wait_element_Visible(locator=om.txtPcNumber,model_name="派出所编号")
        self.input_text(model_name='派出所编号',locator=om.txtPcNumber,value=pcnumber)
        self.input_text(model_name='派出所名称',locator=om.txtPcName,value=pcname)
        self.selector(locator=om.drpPLType, model_name='组织机构类型',type='text', value=pltype)
        self.selector(locator=om.drpAreas, model_name='所属区域',type='text', value=areas)
        self.click_element(model_name='新增提交',locator=om.btnSave)

    def success_message(self):
        text= self.get_element_text(model_name='新增成功',locator=om.success_message)
        return text