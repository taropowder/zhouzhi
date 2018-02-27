# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
def send_email(msg_to,url):
    smtp_ssl_port = 465
    smtp_server = "smtp.qq.com"
    msg_from = "549537094@qq.com"
    smtp_password = "poltxmcsfqgkbcig"
    subject = "周知绑定邮箱"
    content=u""""
<p>用户您好,您的用户正在绑定周知邮箱,如果是您的用户请点击此链接,如果不是您的账户请不要管,如果链接无法点击清复制链接到浏览器地址栏中打开</p>
<p><a href="http://123.206.74.236:8000/">绑定我的邮箱</a></p>
<p>http://123.206.74.236:8000/%s</p>
"""%url
    msg = MIMEText(content, "html", 'utf-8')
    msg['Subject'] = subject
    msg['From'] = "周知官方账户"
    msg['To'] = msg_to
    server = smtplib.SMTP_SSL(smtp_server, smtp_ssl_port)
    server.login(msg_from, smtp_password)
    try:
        server.sendmail(msg_from, msg_to, msg.as_string())
        status=1
        print("发送成功")
    except Exception as e:
        print(e)
        status=0
        print("发送失败")
    finally:
        server.quit()
    print("exit")
    return status
