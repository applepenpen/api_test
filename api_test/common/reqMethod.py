import requests
import api_test.readConfig as readConfig
from api_test.common.Log import MyLog as Log

localReadConfig=readConfig.ReadConfig()


class RequestMethod:
    '''定义请求类型'''

    def __init__(self):
        global host,port,timeout
        host=localReadConfig.get_http('baseurl')
        port=localReadConfig.get_http('port')
        timeout=localReadConfig.get_http('timeout')
        self.log=Log.get_log()
        # self.logger=self.log.get_logger()
        self.headers={}
        self.params={}
        self.data = {}
        self.url=None
        self.files={}

    def set_url(self,url):
        self.url=host+url

    def set_header(self,header):
        self.headers= header

    def set_params(self,param):
        self.params=param

    def set_data(self,data):
        self.data=data

    def set_file(self,file):
        self.file=file

    def get(self):
        '''定义get 请求'''
        # test_url=host+url
        try:
            return requests.get(self.url,params=self.params,headers=self.headers,timeout=float(timeout))
        except TimeoutError:
            self.log.error('time out')
            return print('%s get request timeout'% self.url)

    def post(self):
        '''定义post方法'''
        # test_url=self.base_url+url
        try:
            return requests.post(self.url,data=self.params,headers=self.headers,timeout=float(timeout))
        except TimeoutError:
            self.log.error('time out')
            return print('%s post request timeout' % self.url)

    def post_with_file(self,fp):
        '''post请求:上传文件'''
        # test_url = self.base_url + url
        file={'file':open(fp,'rb')}
        try:
            return requests.post(self.url,headers=self.headers,files=file,timeout=float(timeout))
        except TimeoutError:
            self.log.error('time out')
            return print('%s post request timeout' % self.url)

    def post_with_json(self):
        '''post请求:参数为json类型'''
        # test_url = self.self.url + url
        try:
            return requests.post(self.url,json=self.params,timeout=float(timeout))
        except TimeoutError:
            self.log.error('time out')
            return print('%s post request timeout' % self.url)
