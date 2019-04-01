import json
import requests
from api_test.testFile.readexcel import ExcelUtil

def send_request(s,testdata):
    method=testdata['method']
    url=testdata['url']

    try:
        parmas=eval(testdata['params'])

    except:
        parmas=None

    try:
        headers = eval(testdata['headers'])

    except:
        headers = None


    data=testdata['tpye']

    test_nub=testdata['id']
    print('正在执行测试用例%s'%test_nub)
    print('请求的URL%s,请求的方式%s'%(url,method))
    print('请求的header%s,请求的params%s'%(headers,parmas))

    try:
        bodydata = eval(testdata['body'])

    except:
        bodydata = None


    #根据type 判断data类型

    if type=='json':
        body=bodydata.dumps()
    else:
        body=bodydata


