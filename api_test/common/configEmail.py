from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
import time
import api_test.readConfig as readConfig
from api_test.common.Log import MyLog
from email.mime.multipart import MIMEMultipart

localReadConfig=readConfig.ReadConfig()

class SendMail:
    def __init__(self):
        global host,user,password,sender,receicer,title,content
        host=localReadConfig.get_mail('mail_host')
        user = localReadConfig.get_mail("mail_user")
        password = localReadConfig.get_mail("mail_pass")
        sender = localReadConfig.get_mail("sender")
        title = localReadConfig.get_mail("subject")
        content = localReadConfig.get_mail("content")
        self.value = localReadConfig.get_mail("receiver")
        self.receiver=[]

        for n in str(self.value).split('/'):
            self.receiver.append(n)

        date=str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.subject=title+date+content

        self.log=MyLog.get_log()
        self.logger=self.log.get_logger()
        self.msg=MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject']=self.subject
        self.msg['from']=sender
        self.msg['to'] =';'.join(self.receiver)

    def config_content(self):
        content_plain=MIMEText(content,'plain','utf-8')
        self.msg.attach(content_plain)

    def config_file(self):
        if self.check_file():


    def check_file(self):
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False
    def send_mail(self):
        self.config_header()
        self.config_content()
        self.config_file()

        try:
            smtp=smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user,password)
            smtp.sendmail(sender,self.receiver,self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))
