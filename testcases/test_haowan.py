import random
import time
import sys
import traceback

from PublicModule.myselfunit import MyClass
from PublicModule.BasePage import BasePage
from selenium import webdriver


class Joy(MyClass,BasePage):
    def __init__(self,caseid,a, b):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(r'd:\chromedriver.exe', chrome_options=option)
        BasePage.init(caseid)
        self.a = a
        self.b = b

    def test_joy(self):
        self.logHandle.info('b is %s,a is %s'%(self.b,self.a))
        self.logHandle.info('a is %s'%self.a)
        self.logHandle.info('b is %s'%self.b)


if __name__ == '__main__':
    # sys.argv = ['1','1','2']
    test = Joy(sys.argv[1],sys.argv[2],sys.argv[3])
    try:
        test.test_joy()
        test.setResut(True)
    except Exception as e:
        val = traceback.format_exc()
        print(val)
        test.setResut()

