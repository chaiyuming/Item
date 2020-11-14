# encoding: utf-8
import time
import traceback
import os
import re
import ctypes
import sys
import win32api
import win32con


from PublicModule.myselfunit import MyClass
from PublicModule import profile
from PublicModule.BasePage import BasePage
from PageObject.attendancePage import Attendance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test(BasePage):

    def __init__(self,caseid):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infonars')
        self.driver = webdriver.Chrome(r'd:\chromedriver.exe', options=option)
        BasePage.initial(caseid)
        self.logHandle.info('...init...')
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

        self.logHandle.info('Open the browser and maximize the window')

    def test_case(self):
        self.open()
        self.logHandle.info('begin test')
        Attendance(self.driver).place()
        # # 点击F11退出全屏
        time.sleep(1)
        self.driver.quit()
        self.logHandle.info('Exit the browser')


if __name__ == "__main__":

    test = Test(sys.argv[1],)
    try:
        test.test_case()
    except Exception as e:
        val = traceback.format_exc()
        print(val)
        test.errorExit('test failed !!')





