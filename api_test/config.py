#读取配置文件config.ini 和数据库配置
import os
import configparser as CP

#获取项目的根目录
base_path=str(os.path.abspath(os.path.dirname(__file__)))
print(base_path)
base_path=base_path.replace('\\','/')
cfg_path=base_path+'/config.ini'
cf=CP.ConfigParser()
cf.read(cfg_path,encoding='utf-8')

#获取数据库相关参数值
host=cf.get('MYSQL','host')
port=cf.get('MYSQL','port')
user=cf.get('MYSQL','user')
password=cf.get('MYSQL','password')
db_name=cf.get('MYSQL','db_name')
charset=cf.get('MYSQL','charset')