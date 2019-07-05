#  coding utf-8
# @time      :2019/4/2316:14
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :index_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class IndexPage:
    def __init__(self,driver):
        self.driver = driver
    def isExist_quitEle(self):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//div[@id='container']")))
            return  True
        except:
            return False

    # 车辆管理页面存在
    def vehicleManagement_Exists(self):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//div[@class='dialogHeader_c']/h1")))
            return True
        except:
            return False


    def vehicleDetails(self):
        try:
            self.driver.switch_to_iframe("iframBicycleManage")
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,"//td[@class='th']")))
            return True
        except:
            return False


    # 接警页面存在
    def alarm_Exists(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, "//h1[text()='接警']")))
            return True
        except:
            return False

    # 接警警员密码验证页面
    def alarm_User_Authentication_Exists(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, "//div[text()='身份确认']")))
            return True
        except:
            return False

    # 接警警员密码验证页面
    def alarm_twopage_Exists(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, "//div[@class='stepText']")))
            return True
        except:
            return False