import HTMLTestRunner
from unittest import TestLoader, TestSuite
from test_D9launcher.test_D9launcher import TestD9launcher
from test_D9music.test_D9music import TestD9music
from test_360backcar.test_360backcar import Test360backcar
from test_weather.test_weather import Testweather

def allTest():
#    suite1 = TestLoader().loadTestsFromTestCase(TestD9launcher)   #定义个测试集D9桌面
    suite2 = TestLoader().loadTestsFromTestCase(TestD9music)      #定义个测试集D9音乐
    suite3 = TestLoader().loadTestsFromTestCase(Test360backcar)
    suite4 = TestLoader().loadTestsFromTestCase(Testweather)
    alltests = TestSuite([suite3]+[suite2]+[suite4])                       #定义全部用例集
    return alltests

if  __name__ == "__main__":
    # 定义个报告存放的路径，支持相对路径
    file_path = "D:\\gaodq\\电脑备份\\四维\脚本存档\\d9\\testcase\\report\\reportresult.html"
    file_result = open(file_path, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestReportCN(stream=file_result, tester='最棒QA',
                                    description='用例执行情况', title='D9冒烟自动化测试报告')
    # 运行测试用例
    runner.run(allTest())
    file_result.close()