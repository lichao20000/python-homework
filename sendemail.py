#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

recvFile = open('ReceiverList.csv') # 打开文件
recvReader = csv.reader(recvFile) # 读取收件箱
recvData = list(recvReader) # 接收邮件列表

# 第三方 SMTP 服务
mail_host = 'smtp.chinaunicom.cn'  # 设置服务器
mail_user = 'liujm1541@chinaunicom.cn' # 用户名
mail_pass = '****' # 口令授权码

sender = 'liujm1541@chinaunicom.cn'

message = MIMEText('刘金梅的Python作业', 'plain', 'utf-8')
message['From'] = Header("python全栈教程", 'utf-8')
message['To'] = Header("刘金梅", 'utf-8')

subject = '刘金梅的Python作业'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, recvData, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print( "Error: 无法发送邮件")
