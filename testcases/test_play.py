import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
browser = webdriver.Chrome(r'd:\chromedriver.exe', chrome_options=option)
browser.implicitly_wait(0)
browser.maximize_window()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
print('11111111')
time.sleep(5)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source.text)

try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
