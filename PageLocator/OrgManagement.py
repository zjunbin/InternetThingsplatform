#  coding utf-8
# @time      :2019/6/12 10:42
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :OrgManagement.py

from selenium.webdriver.common.by import By



class OrgManage:
    # 更多功能菜单
    mor = (By.XPATH, "//img[@id='morefun']")
    # 组织结构管理菜单
    bicycle_menu = (By.XPATH, "//div[@id='divMenu_Icon']//a[@rel='411']")
    # 派出所编号
    txtPcNumber = (By.XPATH,"//input[@id='txtPcNumber']")
    # 派出所名称：
    txtPcName = (By.XPATH,"//input[@id='txtPcName']")
    # 所属区域：
    drpAreas = (By.XPATH,"//td[text()='所属区域：']//following-sibling::td/select")
    # 部门类型：
    drpPLType = (By.XPATH,"//*[@id='drpPLType']")
    # 取消按钮
    btnCancel = (By.XPATH,"//input[@id='btnCancel']")
    # 确定按钮
    btnSave = (By.XPATH,"//input[@id='btnSave' and @class='newbutton']")
    # 功能iframe
    ifram411 = "ifram411"
    # 首页iframe
    iframStaiton='iframStaiton'
    # 新建弹出框iframe
    iframeDiv='iframeDiv'
    # 输入页面iframe
    iframeAdd='iframeAdd'
    # 新建按钮
    btnAdd=(By.XPATH,"//input[@id='btnAdd']")
    # 添加成功
    success_message = (By.XPATH,"//div[text()='添加成功!']")
