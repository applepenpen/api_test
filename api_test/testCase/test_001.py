# import unittest
# from ddt import ddt,data,unpack
# import time
# import os
# from api_test.common.reqMethod import RequestMethod
# from api_test.testFile.readexcel import ExcelUtil
#
# project_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# excel_path=os.path.join(project_path,'testFile','test cases.xlsx')
# print(excel_path)
#
# testdatas=ExcelUtil(excel_path).dict_data()
#
# # print(testdatas)
#
# @ddt
# class Test_api(unittest.TestCase):
#     # @classmethod
#     # def setUpClass(cls):
#     #     cls.s=
#
#     @data(*testdatas)
#     @unpack
#     def test_api(self,value):
#         print(value)
#
#
# if __name__=='__main__':
#     unittest.main()