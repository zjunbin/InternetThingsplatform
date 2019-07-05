#  coding utf-8
# @time      :2019/5/1515:11
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :Alarm_locator.py
from selenium.webdriver.common.by import By



class Alarm:
    # 更多功能菜单
    more = (By.XPATH, "//img[@id='morefun']")
    #  接警输入框元素
    idcard = (By.XPATH,"//input[@id='txtIDCard']")
    # 提交按钮元素
    btn = (By.XPATH,"//input[@id='btnNext1']")
    # 身份证、手机号异常元素
    lable_error = (By.XPATH,"//label[@id='lblResult']")
    #身份确认弹出框元素
    aui_title = (By.XPATH,"//div[text()='身份确认']")
    # 接警菜单
    menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='221']")
    # 接警页面iframe
    alarm_page = "ifram221"
    #获取错误信息
    lblResult = (By.XPATH,"//label[@id='lblResult']")



    #接警确认密码
    txtPwd = (By.XPATH,"//input[@id='txtPwd'and@class='textboxs']")
    # 接警取消按钮
    button_cancel = (By.XPATH, "//body[@id='bodys']//input[@value='取消']")
    # 接警确认按钮
    button_determine = (By.XPATH, "//body[@id='bodys']//input[@value='确定']")
    # 接警确认错误提示
    lblMsg = (By.XPATH,"//label[@id='lblMsg']")


    #接警第二步，提交按钮
    btnNext2 = (By.XPATH,"//input[@name='btnNext2']")
    #接警第二步，错误提示信息
    button_tow_message = (By.XPATH,"//div[text()='请选择要报案的车辆!']")


    #接警第三步，报案人姓名
    reporterName = (By.XPATH,"//input[@id='txtReporterName']")
    #接警第三步，报案人手机号
    reporterMobel = (By.XPATH,"//input[@id='txtReporterPhone']")
    #接警第三步，丢失时间
    lostTime = (By.XPATH,"//input[@id='txtLostTime']")
    #接警第三步，所属区域
    endCaseReason = (By.XPATH,"//select[@id='ddlArea']")
    #接警第三步，案件描述
    remarks = (By.XPATH,"//textarea[@id='txtDescription']")
    #接警第三步，丢失地点
    lostPlace = (By.XPATH,"//input[@id='txtAddress']")
    #接警第三步，丢失经纬度
    lngLat = (By.XPATH,"//div[@id='result1']/*")
    #接警第三步，下一步按钮
    btnNext3 = (By.XPATH,"//input[@id='btnNext3']")

    #接警第二步错误提示信息
    alarm_err_message = (By.XPATH,"//div[@class=' aui_state_focus']//div[@class='aui_content']")


    #接警第四步 完成按钮

    btnNext4 = (By.XPATH,"//input[@name='btnNext4']")

    finished = (By.XPATH,"//div[@id='finished']/span")


