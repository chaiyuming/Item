import os, sys
import csv
import unittest
# from unittest import case
from PublicModule import HTMLTestRunner
from selenium import webdriver
import time
import json
import urllib
import multiprocessing


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param
    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        # 用来创建测试套件
        suite = unittest.TestSuite()
        for name in testnames:
            # addTest（）方法是将测试用例添加到测试套件中
            suite.addTest(testcase_klass(name, param=param))
        return suite

def runRecord(logname):
    os.system("python Recording.py %s" % logname)
def rmavi(logname):
    with open("log\\%s.log" % logname, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "PASS" in line:
                print('PASS in logs file!!')
                # os.remove('R:\\%s\\%s.avi' %(opt.http_server,logname))
                os.remove('E:\\Record_csv\\%s.avi' % (logname))
class test_model_1(ParametrizedTestCase):

    def test(self):
        print('param', self.param)
        path = self.param[1]
        argv = self.param[2]
        name = self.param[3]
        casenameList = name.strip().split(',')
        defaultcasename = casenameList[0]
        # file_dir = "E:\\Recod"
        # try:
        #     td = os.path.exists(file_dir)
        #     if not td:
        #         os.mkdir(file_dir)
        #     p1 = multiprocessing.Process(target=runRecord, args=(name,))
        #     p1.start()
        # except:
        #     print("error")
        # try:
        #     td2 = os.path.exists(file_dir)
        #     if td2:
        #         os.rmdir(file_dir)
        # except:
        #     print("rm error")

        ret = os.system('python %s %s' % (path, argv))
        for casename in casenameList:
            os.system("copy log\\%s.log Z:\\log\\%s.log" % (defaultcasename, casename))
        if ret:
            # os.system('taskkill /im chromedriver.exe /F')
            # os.system('taskkill /im chrome.exe /F')
            assert ()
        else:
            print("pass")
        # try:
        #     rmavi(name)
        # except:
        #     print("del error")


def run(case_list):
    # os.system('rd /s /q log')
    # os.system('md log')
    suite = unittest.TestSuite()
    for case in case_list:
        suite.addTest(ParametrizedTestCase.parametrize(test_model_1, param=case))
    # unittest框架的TextTextRunner()类，通过该类下面的run（）方法来进行suite所组装的测试用例，入参为suite测试套件。
    unittest.TextTestRunner(verbosity=2).run(suite)

    # # 生成报告方式
    # now = time.strftime('%Y%m%d %H%M%S')
    # with open('./TestReport/htmlreport/' + now + '.html', 'wb') as fp:
    #     # HTMLTestRunner.HTMLTestRunner(stream=fp, title='XX Test Report', description='Test Execution Report', verbosity=2, retry=0).run(suite)
    #     HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='XX Test Report', description='Test Execution Report').run(suite)
    #     # HTMLTestRunner.HTMLTestRunner(stream=fp, title='XX Test Report', description='Test Execution Report').run(suite)


    # now = time.strftime("%Y%m%d_%H%M%S")
    # filename = './TestReport/htmlreport/' + now + 'result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='automation report', description='case execution status')
    # runner.run(suite)
    # fp.close()

def get_cases():
    case_path = "test_case.csv"
    # case_path = sys.argv[1]
    case_list = []
    with open(case_path) as f:
        f_reader = csv.reader(f)
        header = next(f_reader)
        # print(header)
        for row in f_reader:
            if row[0] == '1':
                case_list.append(row)
    print("cases num is %d" % len(case_list))
    return case_list


if __name__ == '__main__':
    rootdir = os.path.abspath(os.path.dirname(__file__))
    os.environ['PYTHONPATH'] = rootdir
    os.chdir(rootdir)
    print(os.environ['PYTHONPATH'])
    case_list = get_cases()
    # i = 0
    # while i < 10:
    #     run(case_list)
    #     time.sleep(5)
    #     i+=1
    run(case_list)


