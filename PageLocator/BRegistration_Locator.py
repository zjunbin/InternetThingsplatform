#  coding utf-8
# @time      :2019/5/513:39
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :BRegistration_Locator.py
from selenium.webdriver.common.by import By



class BRegistration_Locator:
    # 更多功能菜单
    more = (By.XPATH, "//img[@id='morefun']")
    # 车辆登记菜单
    bicycle_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='251']")
    # 车辆登记iframe
    bicycle_num = '251'
    # 车辆登记页面iframe
    bicycle_win = 'bicycleregifr'
    # 新增按钮
    button = (By.XPATH,"//input[@id='btnAdd']")
    # 登记页面
    bicycle_page= (By.XPATH,"//td[text()='车主信息']")
    # 车主姓名
    txtOwnName = (By.XPATH, "//input[@name='txtOwnName']")
    # 车主身份证
    txtIDCardNumber = (By.XPATH, "//input[@name='txtIDCardNumber']")
    # 车主电话
    txtOwnTel = (By.XPATH, "//input[@name='txtOwnTel']")
    # 车架号
    txtVIN = (By.XPATH, "//input[@name='txtVIN']")
    # 品牌
    txtBrand = (By.XPATH, "//input[@name='txtBrand']")
    # 电机
    txtMotorNumber = (By.XPATH, "//input[@name='txtMotorNumber']")
    # 颜色
    txtColor = (By.XPATH, "//input[@name='txtColor']")
    # 提交按钮
    btnSave = (By.XPATH, "//input[@name='btnSave']")
    # 删除
    delete = (By.XPATH, "//input[@title='删除']")
    # 提示
    message = (By.XPATH, "//div[text()='提示']")
    # 确定
    determine = (By.XPATH, "// button[text() = '确定")
    #登记成功
    successful = (By.XPATH,"//div[text()='添加成功!']")
