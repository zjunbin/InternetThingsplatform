#  coding utf-8
# @time      :2019/4/2515:10
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :vehicleregistration.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from common.basepage import BasePage
from PageLocator.BRegistration_Locator import BRegistration_Locator as lo

class vehicleregistration(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    #进入登记页面
    def registrationPage(self):
        self.wait_element_Visible(locator=lo.more,model_name="更多功能")
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//img[@id='morefun']")))
        self.click_element(model_name='更多功能',locator=lo.more)
        # self.driver.find_element(By.XPATH, "//img[@id='morefun']").click()
        self.wait_element_Visible(locator=lo.bicycle_menu,model_name='车辆登记菜单')
        # WebDriverWait(self.driver, 10).until(
        #     ec.visibility_of_element_located((By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']")))
        self.click_element(model_name='车辆登记菜单',locator=lo.bicycle_menu)
        # self.driver.find_element(By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']").click()

    #新增信息
    def NewVehicle(self,txtOwnName,txtIDCardNumber,txtOwnTel,txtVIN,txtBrand,txtMotorNumber,txtColor):
        self.switch_iframe(iframe=lo.bicycle_num)
        self.switch_iframe(iframe=lo.bicycle_win)
        self.click_element(model_name='',locator=lo.button)
        self.wait_element_Visible(locator=lo.bicycle_page,model_name='登记')
        self.input_text(model_name='姓名',locator=lo.txtOwnName,value=txtOwnName)
        self.input_text(model_name='身份证', locator=lo.txtIDCardNumber,value=txtIDCardNumber)
        self.input_text(model_name='手机号', locator=lo.txtOwnTel,value=txtOwnTel)
        self.input_text(model_name='车架号', locator=lo.txtVIN,value=txtVIN)
        self.input_text(model_name='品牌', locator=lo.txtBrand,value=txtBrand)
        self.input_text(model_name='电机号', locator=lo.txtMotorNumber,value=txtMotorNumber)
        self.input_text(model_name='颜色', locator=lo.txtColor,value=txtColor)
        self.click_element(model_name='提交信息', locator=lo.btnSave)

    #删除信息
    def Del_data(self):
        self.switch_iframe(iframe=lo.bicycle_num)
        self.switch_iframe(iframe=lo.bicycle_win)
        self.wait_element_Visible(locator=lo.delete,model_name='删除')
        self.click_element(model_name='删除', locator=lo.delete)
        self.wait_element_Visible(locator=lo.message,model_name='提示')
        self.click_element(locator=lo.determine,model_name='确定')


    #登记成功元素获取
    def SuccessfulRegistration(self):
        self.wait_element_Visible(locator=lo.successful,model_name='添加成功')
        tex = self.get_element_text(model_name='添加成功',locator=lo.successful)
        return tex

    #为空数据元素获取
    def ErrorRegistration(self):
        self.wait_element_Visible(locator=lo.null_message,model_name="车辆登记")
        text = self.get_element_text(locator=lo.null_message,model_name="车辆登记")
        return text

    #验证删除数据
    def Number_elements(self):
        self.wait_element_Visible(locator=lo.error_message,model_name="车辆登记")
        text = self.get_element_text(locator=lo.error_message,model_name="车辆登记")
        return text