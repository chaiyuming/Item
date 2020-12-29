# encoding: utf-8
import time
import traceback
import os
import re
import ctypes
import sys
import win32api
import win32con


from PublicObject.myselfunit import MyClass
from PublicObject import PublicConfig
from PublicObject.BasePage import BasePage
from PageObject.attendancePage import Attendance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test(BasePage):

    def __init__(self,caseid,department,name,category,starttime,endtime):
        self.department=department
        self.name=name
        self.category=category
        self.starttime=starttime
        self.endtime=endtime
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infonars')
        self.driver = webdriver.Chrome(r'd:\chromedriver.exe', options=option)
        BasePage.initial(caseid)
        self.log.info('...init...')
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

        self.log.info('Open the browser and maximize the window')

    def test_case(self):
        self.open()
        self.log.info('begin test')
        Attendance(self.driver).vacation(self.department,self.name,self.category,self.starttime,self.endtime)
        # # 点击F11退出全屏
        time.sleep(1)
        self.driver.quit()
        self.log.info('Exit the browser')


if __name__=="__main__":

    test = Test(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    try:
        test.test_case()
    except Exception as e:
        val = traceback.format_exc()
        print(val)
        test.errorquit('test failed !!')




