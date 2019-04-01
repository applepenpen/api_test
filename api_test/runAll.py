from HTMLTestRunner import HTMLTestRunner
import configparser as CP
import os,time
import unittest
# from common.SQLServerConfig import DB
# from common import SQLServerConfig
# from config import base_path

test_dir=os.path.dirname(os.path.abspath(__file__))
testcase_dir=os.path.join(test_dir,'testCase')
report_path=os.path.join(test_dir,'testResult')

report_name=time.strftime('%Y%m%d_%H%M%S')+'_report.html'
print(testcase_dir)

discover=unittest.defaultTestLoader.discover(testcase_dir,pattern='test*.py')

if __name__=='__main__':

    fp=open(os.path.join(report_path,report_name),'wb')

    runner=HTMLTestRunner(stream=fp,title='api test',description='132123343')
    runner.run(discover)
    fp.close()



