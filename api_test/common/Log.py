import logging
from datetime import datetime
import threading
import api_test.readConfig
import os
class Log:
    def __init__(self):
        global logPath,resultPath,proDir
        proDir=api_test.readConfig.base_path

        #测试报告的总路径
        resultPath=os.path.join(proDir+'testResult')
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        #测试报告按照时间创建子路径
        logPath=os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))

        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #定义logger

        self.logger=logging.getLogger()
        #定义log等级
        self.logger.setLevel(logging.INFO)

        #定义handler
        handler=logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)

        # add handler
        self.logger.addHandler(handler)

class MyLog:
    log=None
    mutex=threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.Log=Log()
            MyLog.mutex.release()
        return MyLog.log
