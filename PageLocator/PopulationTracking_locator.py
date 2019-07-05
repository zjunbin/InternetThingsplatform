#  coding utf-8
# @time      :2019/7/5 9:34
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :PopulationTracking.py
from selenium.webdriver.common.by import By


class PopulationTracking:

    # 切换到重点人口追踪窗口
    ifram = "ifram122"

    # 新建按钮
    createApply = (By.XPATH,"//button[@id='createApply']")

    # 身份证输入框
    ownerIDCard = (By.XPATH,"//input[@id='ownerIDCard']")

    # 获取错误信息
    error = (By.XPATH,"//p[@id='error']")

    # 申请原因
    applyCause = (By.XPATH,"//textarea[@id='applyCause']")

    # 开始时间
    Mian_StartTime = (By.XPATH,"//div[@class='col-md-4']//input[@id='Mian_StartTime']")
    # 时分
    minAndSec1_StartTime = (By.XPATH,"//div[@class='col-md-4']//input[@id='minAndSec1_StartTime']")
    # 结束时间
    Mian_EndTime = (By.XPATH,"//div[@class='col-md-4']//input[@id='Mian_EndTime']")
    # 时分
    minAndSec1_EndTime = (By.XPATH,"//div[@class='col-md-4']//input[@id='minAndSec1_EndTime']")
    # 确定按钮
    inc_affirm = (By.XPATH,"//button[@id='inc_affirm']")

    # 取消按钮
    cancel = (By.XPATH,"//div[@id='create']//a")
    # 保存不提交按钮
    save = (By.XPATH,"//div[@id='create']//button[text()='保存不提交']")
    # 提交申请
    primary = (By.XPATH,"//div[@id='create']//button[text()='提交申请']")