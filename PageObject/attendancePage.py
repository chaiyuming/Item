# encoding: utf-8

import time
import os

from PublicObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Attendance(BasePage):
    # def __init__(self, driver,case):
    #     super().__init__(self,driver, case)
    #     self.case = case
    #     # self.initial(case)

    title_top = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/strong')
    manage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div[4]/span')
    # 年假额度
    holidaymanage=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/div')
    quota_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/ul/li[1]')
    name_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[2]/section/div[1]/div[1]/div/div[2]/input')
    query_loc = (By.XPATH, '//*[@id="leaveQuery"]/div[1]/div[1]/div/div[3]/button[1]/span')
    check_name_value=(By.XPATH,'//*[@id="leaveQuery"]/div[2]/div[3]/table/tbody/tr/td[3]/div')
    result_name_title=(By.XPATH,'//*[@id="leaveQuery"]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div')
    result_title=(By.XPATH,'//*[@id="leaveQuery"]/div[1]/div[2]/div')
    # 员工请假
    vacation_loc=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]')
    vacation_check_enter=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/ul/li[2]')
    vacation_check_title=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/div/span[2]/span')
    vacation_department_loc=(By.XPATH,'//*[@id="leaveQuery"]/div[1]/div/form/div[1]/div/div[1]/input')


    def place(self,name):
        '''
        年假额度查询name字段
        :return:
        '''
        WebDriverWait(self.driver, 20, 1).until(EC.element_can_be_clickable(self.manage_loc))
        time.sleep(1)
        WebDriverWait(self.driver, 20, 1).until(EC.element_can_be_clickable(self.holidaymanage))
        time.sleep(1)
        if self.wait_time_to_find_element(*self.quota_loc,4):
            self.find_element(*self.quota_loc).click()
        else:
            try:
                time.sleep(2)
                self.log.info('try again !!')
                WebDriverWait(self.driver, 20, 1).until(EC.element_can_be_clickable(self.holidaymanage))
                WebDriverWait(self.driver, 20, 1).until(EC.element_can_be_clickable(self.quota_loc))
                time.sleep(1)
                self.find_element(*self.quota_loc).click()
            except:
                self.log.error('it is invisibility !!')
        if name == 'fukaiyun':
            name = '傅开云'
        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(self.name_loc))
        self.log.info('the element is visibility')
        self.find_element(*self.name_loc).send_keys(name)
        self.log.info('input name success')

        time.sleep(1)
        self.find_element(*self.query_loc).click()
        title= self.find_element(*self.result_title)
        result= self.wait_time_to_find_element(*self.result_name_title,3)
        if title and result:
            self.log.info('checkout success')
            allcheckout=self.find_elements(*self.check_name_value)
        else:
            allcheckout=False
        result=0
        if allcheckout:
            for checkout in allcheckout:
                self.log.info('111111111')
                self.log.info(checkout.text)
                if checkout.text == name:
                    result=1
                    self.log.info('result is %s' % result)
                else:
                    result=0
                    self.log.error('result is %s' % result)
                    break
        else:
            result=2
        if result == 1:
            self.log.info('checkout successfully !!')
            self.SetRunResult(True)
        elif result ==2:
            self.log.info('result is null')
            self.SetRunResult(True)
        else:
            self.log.info('checkout failed !!')
            self.SetRunResult()

    def vacation(self,department,name,category,starttime,endtime):
        '''
         假期查询
         :return:
         '''
        pass







