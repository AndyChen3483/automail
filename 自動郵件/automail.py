import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def mail():
    smtp = smtplib.SMTP("smtp.simplemart.com.tw")
    f1 = open("主旨和內容.txt", "r", encoding="utf-8").read().splitlines()
    f2 = open("附件.txt", "r", encoding="utf-8").read().splitlines()
    sender = "ssis@simplemart.com.tw"
    message = MIMEMultipart()
    message["From"] = sender
    message['Subject'] = Header(f1[1])
    message.attach(MIMEText(f1[4]))
    for i in range(len(f2)):
        mailline = f2[i].replace("\\", "/")
        attach = MIMEApplication(open(mailline, "rb").read())
        attach.add_header('Content-Disposition', 'attachment', filename = ('gbk', '', mailline.split("/")[-1]))
        message.attach(attach)


    f3 = open("寄件人.txt", "r").read().splitlines()
    for i in range(len(f3)):
        receiver = f3[i]
        message['To'] = receiver
        smtp.sendmail(sender, receiver, message.as_string())
        

