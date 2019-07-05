#  coding utf-8
# @time      :2019/7/5 10:12
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test2.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//input[@id='kw']")))
driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("北京",Keys.ENTER)
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()