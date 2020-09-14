#!/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import win32api
import win32con
import json

from PublicModule import logUtil,opt



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    usernameLoc = (By.XPATH, '//*[@id="app"]/div/div[4]/form/div[1]/div/div/input')
    titleimg_loc = (By.XPATH, '//*[@id="app"]/div/div[4]/div/img')
    passwordLoc = (By.XPATH, '//*[@id="app"]/div/div[4]/form/div[2]/div/div/input')
    login_loc = (By.XPATH, '//*[@id="app"]/div/div[4]/form/div[3]/div/button')
    process_loc= (By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div[1]/span')
    attendance_loc=(By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[4]/span')
    frame_loc=(By.XPATH, '//*[@id="app"]/div/div[2]')

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def initial(self, caseid):
        print('BasePage init begin ...')
        self.rootdir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.resultFile = os.path.join(self.rootdir, 'result.txt')
        self.caseid = caseid
        self.setlogger(caseid)


    @classmethod
    def setlogger(self, caseid):
        print('set_logger begin ...')
        if hasattr(self, "logHandle"):
            self.logHandle.close_logger()
        self.logHandle = logUtil.LogUtil(log_file_name=caseid, log_dir=os.path.join(self.rootdir, 'log'))
        self.logHandle.info("log file name is {}".format(caseid))

    # @classmethod
    def setResut(self, caseResult=False):
        if caseResult:
            result = 'pass'
        else:
            self.screenshot_img()
            result = 'fail'
        resultStr = '[%s]: %s' % (self.caseid, result)
        if hasattr(self, "logHandle"):
            self.logHandle.info('test %s' % result.upper())
            self.logHandle.info(resultStr)
        else:
            print('test %s' % result.upper())
            print(resultStr)
        f = open(self.resultFile, 'a')
        f.write(resultStr + '\n')
        f.close()
    # @classmethod
    def errorExit(self,msg):
        self.logHandle.error(msg)
        self.setResut()
        self.logHandle.info('beginning closed the windows')
        # # 点击F11退出全屏
        win32api.keybd_event(win32con.VK_F11, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        self.driver.quit()
        self.logHandle.error('closed the windows complete')
        exit(-1)

    def find_element(self, *ele, t=1):
        count = 0
        element = self.find_element_no_print(*ele)
        while not element:
            count += 1
            if count > t:
                # 没找到元素
                return None
            element = self.find_element_no_print(*ele)
        # 找到了元素
        return element

    def find_elements(self, *loc, delay_t=50):
        try:
            WebDriverWait(self.driver, delay_t).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            return None

    def find_element_no_print(self, *loc):
        try:
            if len(loc) >= 3:
                delay_t = loc[-1]
                loc = loc[:-1]
            else:
                delay_t = 5
            WebDriverWait(self.driver, delay_t).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            return None

    def login(self):
        WebDriverWait(self.driver, 60, 1).until(EC.visibility_of_element_located(self.usernameLoc))
        self.find_element(*self.usernameLoc).send_keys(opt.LoginInfo['username'])
        WebDriverWait(self.driver,10,1).until(EC.element_can_be_clickable(self.titleimg_loc))
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located(self.passwordLoc))
        self.find_element(*self.passwordLoc).send_keys(opt.LoginInfo['passwd'])
        time.sleep(1)
        self.logHandle.info('begin click login btn .....')
        self.find_element(*self.login_loc).click()
        self.logHandle.info('click login btn end .....')

    def open(self):
        count = 0
        while count < 2:
            try:
                self.driver.get(opt.LoginInfo['url'])  #\n表示回车键
                self.logHandle.info('input url success!')
                self.login()
                WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.process_loc))
                self.logHandle.info('login is successfully!!')
                # targetElem = self.wait_time_to_find_element(*self.agreement_submit_loc, 1)
                # self.driver.execute_script("arguments[0].scrollIntoView();", targetElem)
                break
            except :
                count += 1
                self.logHandle.info('the count is %s'%count)
                self.screenshot_img()
                # 处理 js 弹窗事件
                # win32api.keybd_event(13,0,0,0) # enter键
                # time.sleep(0.2)
                # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP,0) #释放按键
                self.driver.refresh()
        else:
            self.errorExit('open failed !!')

    # @classmethod
    def screenshot_img(self):
        '''
        截图，方便失败的时候定位问题
        :return:
        '''
        # imagepath直接写死。
        imagepath=opt.data_root
        # 当脚本允许错误的时候，截图并保存到响应的路径下面。
        self.driver.save_screenshot(os.path.join(imagepath,time.strftime('%Y%m%d_%H%M%S')+'_open.png'))

    def switchframe(self, loc):
        return self.driver.switch_to_frame(loc)

    def switch_default_frame(self):
        return self.driver.switch_to_default_content()

    def switch_parent_frame(self):
        self.driver.switch_to.parent_frame()


