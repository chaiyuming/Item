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
from PublicObject.BasePage import BasePage
from PageObject.attendancePage import Attendance
from selenium import webdriver
from PublicObject import publicdata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test(BasePage,MyClass):

    def __init__(self, case,name):
        # self.case = case
        self.name=name
        self.setUp()
        BasePage.initial(case)
        self.log.info('Open the browser and maximize the window')
        self.log.info('...init...')

    def test_case(self):
        self.open()
        self.log.info('begin test')
        # Attendance(self.driver,self.case).place()
        Attendance(self.driver).place(self.name)
        self.teardown()
        self.log.info('Exit the browser')

if __name__ == "__main__":
    # sys.argv = ['1', 'test_attendance','傅开云']
    test = Test(sys.argv[1],sys.argv[2])
    try:
        test.test_case()
    except Exception as e:
        val = traceback.format_exc()
        test.log.error(val)
        test.errorquit('test failed !!')





