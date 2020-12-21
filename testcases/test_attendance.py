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
from PublicObject import publicdata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test(BasePage,MyClass):

    def __init__(self, case):
        self.setUp()
        self.initial(case)
        self.logHandle.info('Open the browser and maximize the window')
        self.logHandle.info('...init...')

    def test_case(self):
        self.open()
        self.logHandle.info('begin test')
        Attendance(self.driver).place()
        self.teardown()
        self.logHandle.info('Exit the browser')

if __name__ == "__main__":
    sys.argv = ['1', 'test_attendance']
    test = Test(sys.argv[1],)
    try:
        test.test_case()
    except Exception as e:
        val = traceback.format_exc()
        test.logHandle.error(val)
        test.errorquit('test failed !!')





