from selenium import webdriver
from PublicObject import PublicConfig,logUtil,BasePage
import time
import win32api
import win32con
from PublicObject import publicdata

class MyClass:

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(publicdata.DriverPath(), chrome_options=option)
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()

    def teardown(self):
        win32api.keybd_event(win32con.VK_F11, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        self.driver.quit()