#读取配置文件config.ini 和数据库配置
import os
import configparser as CP

#获取项目的根目录
base_path=str(os.path.abspath(os.path.dirname(__file__)))
# base_path=base_path.replace('\\','/')
# print(base_path)
cfg_path=os.path.join(base_path,'config.ini')
# print(cfg_path)
excel_path=os.path.join(base_path,'testFile','test cases.xlsx')
# print(excel_path)
class ReadConfig:
    def __init__(self):
        self.cf = CP.ConfigParser()
        self.cf.read(cfg_path, encoding='utf-8')

    def get_mail(self,name):
        value=self.cf.get('EMAIL',name)
        return value

    def get_http(self,name):
        value=self.cf.get('HTTP',name)
        return value

    def get_db(self,name):
        value=self.cf.get('DATABASE',name)
        return value


if __name__=='__main__':
    readconfig=ReadConfig()
    print(readconfig.get_mail('mail_host'))

