from HTMLTestRunner import HTMLTestRunner
import configparser as CP
import os,time
import unittest
from common.SQLServerConfig import DB
from common import SQLServerConfig
from config import base_path

discover=unittest.defaultTestLoader.discover(base_path+'/testCase',pattern='test*.py')

if __name__=='__main__':
    #往数据库中造数据
    runner=HTMLTestRunner.run(discover)



