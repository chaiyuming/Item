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
for i in ra1 import time
 2 
 3 def consumer(name):
 4     print("%s 准备吃包子啦！" %name)
 5     while 1:
 6         baozi = yield
 7         print("包子[%s]来了，被[%s]吃了" %(baozi,name))
 8         
 9 def producer(name):
10     c = consumer('A')
11     c2 = consumer('B')
12     c.__next__()
13     c2.__next__()
14     print("%s开始准备做包子啦!" %name)
15     for i in range(3):
16         time.sleep(1)        #执行时为了更清楚的看到过程
17         print("做了2个包子")
18         c.send(i)
19         c2.send(i)
20               
22 producer('root')

?123456789101112A 准备吃包子啦！B 准备吃包子啦！root开始准备做包子啦!做了2个包子包子[0]来了，被[A]吃了包子[0]来了，被[B]吃了做了2个包子包子[1]来了，被[A]吃了包子[1]来了，被[B]吃了做了2个包子包子[2]来了，被[A]吃了包子[2]来了，被[B]吃了nge(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                n +=1
                print (i,j,k)
print(n)
'''

'''
import time
def consumer(name):
    print("%s 准备吃包子啦！" %name)
    while 1:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))
def producer(name):
    c = consumer('A')
    print('0000',c)
    c2 = consumer('B')
    c.__next__()
    # print('11111',c.__next__())
    # c2.__next__()
    print("%s开始准备做包子啦!" %name)
    for i in range(3):
        time.sleep(1)        #执行时为了更清楚的看到过程
        print("做了2个包子")
        c.send(i)
        # c2.send(i)
producer('root')

'''
'''
def bar(a,b,c,d):
    print(a,b,c,d)

bar(*[1,2,3,4])

def bar(a, b, c):
    print(a,b,c)

bar(**{'a': 1, 'b': 2, 'c': 3}) #1，2，3

'''


'''
class gradapa():
    def __init__(self, money):
        self.money = money

    def p(self):
        print("this is gradapa")


class father(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is father,我重写了父类的方法")


class mother(gradapa):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job

    def p(self):
        print("this is mother,我重写了父类的方法")
        return 'success'
# 定义一个函数，函数调用类中的p()方法

def fc(obj):
    return obj.p()

gradapa1 = gradapa(3000)
father1 = father(2000, "工人")
mother1 = mother(1000, "老师")

fc(gradapa1)  # 这里的多态性体现是向同一个函数，传递不同参数后，可以实现不同功能.
fc(father1)
print(fc(mother1))
# fc(mother1)
'''

l=['a','b','c']

m=','.join(l)
print(','.join(l))
print(type(m))