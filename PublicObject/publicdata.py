#!/usr/bin/python
# encoding: utf-8


from functools import wraps

from selenium import webdriver

def Tryagain(func)  :
    @wraps(func)
    def _wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except:
            print('try again ............')
            func(*args,**kwargs)
    return _wrapper


def DriverPath():
    # path = r'd:\chromedriver.exe'
    path = r'E:\Google\chromedriver87_win32\chromedriver.exe'
    return path


