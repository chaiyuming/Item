# encoding: utf-8

import time
import os

from PublicModule.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Attendance(BasePage):

    title_top = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/strong')
    manage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div[4]/span')
    # 考勤方案
    place_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[1]/ul/li[2]')
    state_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[2]/section/div[1]/div[2]/div[1]/div/form/div[1]/div/div/div/input')
    inforbidden_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    query_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div[3]/section/div/div[2]/section/form/div[2]/div/button[1]')
    check_state_value=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/section/div/div[2]/section/div[4]/div[3]/table/tbody/tr/td[10]/div')

    error_windows=(By.CLASS_NAME,'el-message-warning')
    # 员工请假
    vacation_loc=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]')
    vacation_check_enter=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/aside/ul/li[2]/ul/li[2]')
    vacation_check_title=(By.XPATH,'//*[@id="app"]/section/div[1]/div[3]/section/div/div[1]/div/span[2]/span')
    vacation_department_loc=(By.XPATH,'//*[@id="leaveQuery"]/div[1]/div/form/div[1]/div/div[1]/input')



    def place(self):
        '''
        考勤地点查询状态字段
        :return:
        '''
        WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.manage_loc))
        WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.place_loc))
        WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.state_loc))
        try:
            WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(self.inforbidden_loc))
            self.logHandle.info('the element is visibility')
            self.find_element(*self.inforbidden_loc).click()
            self.logHandle.info('click success')
        except:
            self.logHandle.debug('try again')
            WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.title_top))
            self.logHandle.info('start click state button')
            WebDriverWait(self.driver, 10, 1).until(EC.element_can_be_clickable(self.state_loc))
            WebDriverWait(self.driver, 20, 1).until(EC.visibility_of_element_located(self.inforbidden_loc))
            self.find_element(*self.inforbidden_loc).click()
        time.sleep(1)
        self.find_element(*self.query_loc).click()
        if WebDriverWait(self.driver,20,1).until(EC.visibility_of_element_located(self.error_windows)):
            self.logHandle.info('it is not change company orangnazation')
        allcheckout=self.find_elements(*self.check_state_value)
        result=0
        for checkout in allcheckout:
            if checkout.text =='启用':
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
            self.setResut(True)
        else:
            self.logHandle.info('checkout failed !!')
            self.setResut()

    def vacation(self,department,name,category,starttime,endtime):
        '''
         假期查询
         :return:
         '''
        pass







