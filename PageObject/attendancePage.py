# encoding: utf-8

import time
import os

from PublicObject.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Attendance(BasePage):

    title_top = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/strong')
    manage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div[4]/span')
    # 年假额度
    holidaymanage=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/div')
    quota_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/ul/li[1]')
    name_loc = (By.XPATH, '//*[@id="leaveQuery"]/div[1]/div/form/div[3]/div/div/input')
    query_loc = (By.XPATH, '//*[@id="leaveQuery"]/div[2]/div/form/div/div/button[1]')
    check_name_value=(By.XPATH,'//*[@id="leaveQuery"]/div[3]/div[3]/table/tbody/tr/td[3]/div')
    result_name_title=(By.XPATH,'//*[@id="leaveQuery"]/div[3]/div[2]/table/thead/tr/th[3]/div')
    # 员工请假
    vacation_loc=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]')
    vacation_check_enter=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/ul/li[2]')
    vacation_check_title=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/div/span[2]/span')
    vacation_department_loc=(By.XPATH,'//*[@id="leaveQuery"]/div[1]/div/form/div[1]/div/div[1]/input')



    def place(self):
        '''
        年假额度查询name字段
        :return:
        '''
        WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.manage_loc))
        WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.holidaymanage))
        if WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(self.quota_loc)):
            self.find_element(*self.quota_loc).click()
        else:
            self.logHandle.error('it is invisibility !!')

        WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(self.name_loc))
        self.logHandle.info('the element is visibility')
        # self.find_element(*self.name_loc).click()
        self.find_element(*self.name_loc).send_keys('傅开云')
        self.logHandle.info('input name success')

        time.sleep(1)
        self.find_element(*self.query_loc).click()
        if WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located(self.result_name_title)):
            self.logHandle.info('checkout success')
            allcheckout=self.find_elements(*self.check_name_value)
        else:
            self.logHandle.info('checkout failed !!')
            allcheckout=[]
        result=0
        for checkout in allcheckout:
            if checkout.text =='傅开云':
                result=1
                self.logHandle.info('result is %s'% result)
            # elif checkout.text =='':
            #     result=1
            #     self.logHandle.info('result is null')
            else:
                result=0
                self.logHandle.error('result is %s'% result)
                break
        if result == 1:
            self.logHandle.info('checkout successfully !!')
            self.SetRunResult(True)
        else:
            self.logHandle.info('checkout failed !!')
            self.SetRunResult()

    def vacation(self,department,name,category,starttime,endtime):
        '''
         假期查询
         :return:
         '''
        pass







