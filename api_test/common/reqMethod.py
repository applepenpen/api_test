import requests
import config


class RequestMethod:
    '''定义请求类型'''

    def __init__(self):
        self.base_url=config.base_path
        self.data = {}
        self.files={}

    def get(self,url,params):
        '''定义get 请求'''
        test_url=self.base_url+url
        try:
            return requests.get(ul=test_url,params=params,timeout=60)
        except TimeoutError:
            return print('%s get request timeout'% test_url)

    def post(self,url,params):
        '''定义post方法'''
        test_url=self.base_url+url
        try:
            return requests.post(url=test_url,data=params,timeout=60)
        except TimeoutError:
            return print('%s post request timeout' % test_url)

    def post_with_file(self,url,parames,fp):
        '''post请求:上传文件'''
        test_url = self.base_url + url
        file={'file':open(fp,'rb')}
        try:
            return requests.post(url=test_url,data=parames,files=file,timeout=60)
        except TimeoutError:
            return print('%s post request timeout' % test_url)

    def post_with_json(self,url,parames):
        '''post请求:参数为json类型'''
        test_url = self.base_url + url
        try:
            return requests.post(url=test_url,json=parames,timeout=60)
        except TimeoutError:
            return print('%s post request timeout' % test_url)
