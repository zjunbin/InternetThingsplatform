#  coding utf-8
# @time      :2019/4/2614:31
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :basepage.py
import win32gui
import win32con
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.do_mylog import MyLog
from common import globpath
import datetime,time




class BasePage:

    def __init__(self,driver):
        self.driver = driver
        # self.mylog = MyLog()



    #等待元素可见
    def wait_element_Visible(self, locator, timeout = 30, poll_frequency= 0.5, model_name=None):
        # self.mylog.info('等待{}元素可见'.format(locator))
        try:
            #获取开始时间
            starttime = datetime.datetime.now()
            # 等待元素
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(locator))
            #获取结束的时间
            endtime = datetime.datetime.now()
            #获取等待时长
            # self.mylog.info('等待元素总时长{}'.format((endtime - starttime).seconds))
        except Exception as e:
            #写日志
            # self.mylog.error(e)
            self.save_iamge(model_name)
            raise



    def get_element(self,model_name ,locator):
        # self.mylog.info('查找模块{}下的元素：{}'.format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            return ele
        except:
            # self.mylog.error('查找模块{}下的元素：{}。失败'.format(model_name, locator))
            raise

    def click_element(self,model_name ,locator):
        # 查找元素
        ele = self.get_element(model_name ,locator)
        # 元素操作
        # self.mylog.info('点击操作：{}下的元素：{}'.format(model_name, locator))
        try:
            ele.click()
        except:
            raise


    def input_text(self,model_name ,locator ,value):
        # 查找元素
        ele = self.get_element(model_name,locator)
        # 元素操作
        # self.mylog.info('输入操作：{}下的元素{}'.format(model_name, locator))
        try:
            ele.send_keys(value)
        except:
            raise

    def get_element_attribute(self,model_name ,locator ,attr):
        # 查找元素
        ele = self.get_element(model_name, *locator)
        # 元素操
        # self.mylog.info('获取元素属性：{}下的元素{}的属性{}'.format(model_name, locator ,attr))
        try:
            return ele.get_attribute(attr)
        except:
            # self.mylog.error('获取元素属性失败：{}下的元素{}的属性{}'.format(model_name, locator ,attr))
            self.save_iamge(model_name)
            raise

    def get_element_text(self, model_name ,locator):
        ele = self.get_element(model_name ,locator)
        # self.mylog.info('获取元素文本值：模块{} 下 {}的文本值'.format(model_name,locator))
        try:
            return ele.text
        except:
            # self.mylog.info('获取元素文本值失败：模块{} 下 {}的文本值'.format(model_name, locator))
            raise

    def save_iamge(self,model_name):

        # 文件名称  当前时间
        filepath = globpath.screenshot_path + '{}_{}.png'.format(model_name,time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(filepath)
            # self.mylog.info("截图成功，文件路径为:{}".format(filepath))
        except Exception as e:
            # self.mylog.error("截屏保存失败")
            raise e

    def switch_window(self,str='',index=None):
        if str == 'new':
        # 等待新窗口出现
            time.sleep(2)
            win = self.driver.window_handles
            self.driver.switch_to.window(win[-1])
        # 切换到窗口
            pass
        else:
            # 获取所有的窗口
            # 切换到index下标所有的窗口
            win = self.driver.window_handles
            if index != None and 0 <= int(index)< len(win):
                self.driver.switch_to.window(win[int(index)])


    def switch_alert(self,action = 'accept'):
        # 等待alter出现
        WebDriverWait(self.driver,10).until(ec.alert_is_present())
        # 关闭alter弹框  accept dismiss
        alert = self.driver.switch_to.alert
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()



    def switch_iframe(self,iframe):
        try:
            WebDriverWait(self.driver,10).until(ec.frame_to_be_available_and_switch_to_it(locator=iframe))
            time.sleep(0.5)
        except:
            raise

    # 文件上传
    def upload(filePath, browser_type="chrome"):
        if browser_type == "chrome":
            title = "打开"
        elif browser_type == 'Firefox':
            title = "文件上传"
        else:
            title = "选择要加载的文件"
        dialog = win32gui.FindWindow("#32770", title)
        # 找窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)
        # 操作
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 写入文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    # 等待页面存在某个元素
    def wait_until_page_comtains_element(self,model_name,locator):
        self.get_element(model_name=model_name,locator=locator)