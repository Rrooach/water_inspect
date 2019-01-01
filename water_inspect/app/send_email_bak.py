from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import smtplib
import sys
import os

SENDER_EMAIL = "OCEAN-Z@QQ.COM"
PWD = "lubmicbncseybaij"
HOST_SERVER = 'smtp.qq.com'


class SendMail:
    def __init__(self, content, subject, receivers):
        self.smtp = SMTP_SSL(HOST_SERVER, 465)
        self.msg = MIMEText(content, "html", "utf-8")
        self.msg["Subject"] = Header("456", 'utf-8')
        self.msg["From"] = "水质监测系统"
        self.receivers = receivers

    def build_content(self, receiver):
        self.msg["To"] = receiver


        # 采用html格式发送邮件
        # 等罗旭前端大佬来做

        # self.msg = MIMEText(mail_content, "html", 'utf-8')
        # self.msg["Subject"] = Header(mail_title, 'utf-8')
        # self.msg["From"] = self.conf_dict["sender_email"]
        # self.msg["To"] = receiver

    def send(self):

        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        try:
            self.smtp.set_debuglevel(0)
            self.smtp.ehlo(HOST_SERVER)
            self.smtp.login(SENDER_EMAIL, PWD)
            for receiver in self.receivers:
                print('+', receiver)
                self.build_content(receiver)
                self.smtp.sendmail(SENDER_EMAIL, receiver, self.msg.as_string())
            self.smtp.quit()
        except smtplib.SMTPServerDisconnected as e:
            print("发送成功！")
