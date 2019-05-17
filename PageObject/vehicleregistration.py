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
        # WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("251"))
        self.switch_iframe(iframe=lo.bicycle_win)
        # WebDriverWait(self.driver,20).until(ec.frame_to_be_available_and_switch_to_it("bicycleregifr"))
        self.click_element(model_name='',locator=lo.button)
        # self.driver.find_element_by_xpath("//input[@id='btnAdd']").click()
        self.wait_element_Visible(locator=lo.bicycle_page,model_name='')
        # WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//td[text()='车主信息']")))
        self.input_text(model_name='姓名',locator=lo.txtOwnName,value=txtOwnName)
        # self.driver.find_element_by_xpath("//input[@name='txtOwnName']").send_keys(txtOwnName)
        self.input_text(model_name='身份证', locator=lo.txtIDCardNumber,value=txtIDCardNumber)
        # self.driver.find_element_by_xpath("//input[@name='txtIDCardNumber']").send_keys(txtIDCardNumber)
        self.input_text(model_name='手机号', locator=lo.txtOwnTel,value=txtOwnTel)
        # self.driver.find_element_by_xpath("//input[@name='txtOwnTel']").send_keys(txtOwnTel)
        self.input_text(model_name='车架号', locator=lo.txtVIN,value=txtVIN)
        # self.driver.find_element_by_xpath("//input[@name='txtVIN']").send_keys(txtVIN)
        self.input_text(model_name='品牌', locator=lo.txtBrand,value=txtBrand)
        # self.driver.find_element_by_xpath("//input[@name='txtBrand']").send_keys(txtBrand)
        self.input_text(model_name='电机号', locator=lo.txtMotorNumber,value=txtMotorNumber)
        # self.driver.find_element_by_xpath("//input[@name='txtMotorNumber']").send_keys(txtMotorNumber)
        self.input_text(model_name='颜色', locator=lo.txtColor,value=txtColor)
        # self.driver.find_element_by_xpath("//input[@name='txtColor']").send_keys(txtColor)
        self.click_element(model_name='提交信息', locator=lo.btnSave)
        # self.driver.find_element_by_xpath("//input[@name='btnSave']").click()

    #删除信息
    def Del_data(self):
        # WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("251"))
        self.switch_iframe(iframe=lo.bicycle_num)
        # WebDriverWait(self.driver, 20).until(ec.frame_to_be_available_and_switch_to_it("bicycleregifr"))
        self.switch_iframe(iframe=lo.bicycle_win)
        # WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//input[@title='删除']")))
        self.wait_element_Visible(locator=lo.delete,model_name='删除')
        # self.driver.find_element_by_xpath("//input[@title='删除']").click()
        self.click_element(model_name='删除', locator=lo.delete)
        # WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[text()='提示']")))
        self.wait_element_Visible(locator=lo.message,model_name='提示')
        # self.driver.find_element_by_xpath("// button[text() = '确定']").click()
        self.click_element(locator=lo.determine,model_name='确定')
        # // button[text() = '取消']
        # // div[text() = '提示'] / following - sibling::a


    #登记成功元素获取
    def SuccessfulRegistration(self):
        self.wait_element_Visible(locator=lo.successful,model_name='添加成功')
        # WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//div[text()='添加成功!']")))
        # tex = self.driver.find_element_by_xpath("//div[text()='添加成功!']").text
        tex = self.get_element_text(model_name='添加成功',locator=lo.successful)
        return tex

    #为空数据元素获取
    def ErrorRegistration(self):
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//div[@id='massage']")))
        return self.driver.find_element_by_xpath("//div[@id='massage']").text

    #验证删除数据
    def Number_elements(self):
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//td[text()='当前没有车辆信息']")))

        ele = self.driver.find_element_by_xpath("//td[text()='当前没有车辆信息']").text
        return ele