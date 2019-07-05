# #  coding utf-8
# # @time      :2019/5/1614:45
# # @Author    :zjunbin
# # @Email     :648060307@qq.com
# # @File      :test.py
# import time
# from selenium import webdriver
# from common.basepage import BasePage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
#
# driver = webdriver.Chrome(service_log_path=r"D:\ChromeLog\log.log")
# driver.maximize_window()
# driver.get("https://www.baidu.com/")
# WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//input[@id='kw']")))
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys('北京')
# lc = (By.XPATH,"//div[@class='bdsug']//li")
# BasePage(driver).random_element(locator=lc)
#
# # WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//div[@class='bdsug']//li")))
# # ele = driver.find_elements(By.XPATH,"//div[@class='bdsug']//li")
# # print(ele)
#
#
# time.sleep(5)
# driver.quit()
# # import random,string
# # num=string.ascii_letters+string.digits
# # print ( "".join(random.sample(num,10)) )

# import pymssql
# server = '192.168.0.175'
# user = 'sa'
# pwd = 'Jdkj2015'
# db = 'IntelligentGuardApp'
# conn = pymssql.connect(server,user, pwd ,db)
# cur = conn.cursor()
#
# if not cur:
#     print('success')
# else:
#     print('error')

# import pymssql
# conn = pymssql.connect(host = '192.168.0.175',user = 'sa',password = 'Jdkj2015',database = 'IntelligentGuardApp')
# cur = conn.cursor()
# cur.execute('select * from table1')
# 如果是插入，删除，更新语句切记要写提交命令con.commit（）print（cur.fetchall（））cur.close（）conn.close（）


while True:
    try:
        a = int(input('请输入一个整数'))
        # b="{0:b}".format(int(a))
        b="{}".format(int(a))
        print(b)
        try:
            print(b.count("1") )
        except Exception as e :
            print('没有1')
        break
    except Exception as e :
        print('输入有误')
        continue