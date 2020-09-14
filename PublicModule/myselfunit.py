import unittest
from selenium import webdriver
from PublicModule import opt
import time
import win32api
import win32con


class MyClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(r'd:\chromedriver.exe', chrome_options=option)

        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        win32api.keybd_event(win32con.VK_F11, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        self.driver.close()