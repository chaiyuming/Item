import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
'''
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

'''


dict1= {"a": 1, "b": 1}
a=str(dict1)
# print(str(dict1))
# print(type(str(dict1)))
# print(dict1)
# print(type(dict1))
# print(len(dict1))
# print(set(dict1))
# print(a[1:5])

# print(dict1.clear())
# print(dict1.fromkeys(('a','b','c'),10))
# print(dict1) #fromkeys只负责创建字典，不负责保存
# print(dict1.items())
# print(list(dict1.items()))
# print(dict1.keys())
# print(dict1.values())

'''
n=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                n +=1
                print (i,j,k)
print(n)
'''


