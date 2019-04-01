import unittest
import json
# from api_test.common.reqMethod import RequestMethod
import  requests
from api_test.testFile.readexcel import ExcelUtil

from api_test.readConfig import excel_path
class Login(unittest.TestCase):
    '''测试登录接口'''

    def setUp(self):
        self.sheet='login'
        self.datas=ExcelUtil(excel_path,sheetName='login').dict_data()
        # excel_path=

    def tearDown(self):
        print('111')

    def test_login_success(self):
        '''测试正常的登录'''
        casename='test_login_success'
        #获取请求的参数
        for requestData in self.datas:
            if requestData['id']==casename:
                # print(requestData)

                requestMethod=requestData['method']

                url=requestData['url']
                params=requestData['params']
                # print(url,params)
                # print(params)
                # print(type(params))
                res=requests.get(url,params=json.loads(params))
                print(res.status_code)
                self.assertEqual(res.status_code,requestData['statuscode'])
                self.assertEqual(res.json()['msg'],requestData['checkpoint'])

    def test_login_failed(self):
        '''测试失败的登录'''
        casename = 'test_login_failed'
        # 获取请求的参数
        for requestData in self.datas:
            if requestData['id'] == casename:
                requestMethod = requestData['method']
                url = requestData['url']
                params = requestData['params']
                res = requests.get(url, params=json.loads(params))
                print(res.status_code)
                self.assertEqual(res.status_code, requestData['statuscode'])
                self.assertEqual(res.json()['msg'], requestData['checkpoint'])


if __name__=='__main__':
    unittest.main()