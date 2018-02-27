# -*- coding: utf-8-*-


# 发送错误邮件
def SendEmail(Message,Except):
    from email import encoders
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    import smtplib

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'cloudofzm@sina.com'
    password = 'qwerty123'
    to_addr = 'cloudofzm@163.com'
    smtp_server = 'smtp.sina.com'

    msg = MIMEText(Except+' \n'+Message, 'plain', 'utf-8')
    msg['From'] = _format_addr('cloudofzm <%s>' % from_addr)
    msg['To'] = _format_addr('manager <%s>' % to_addr)
    msg['Subject'] = Header(Except, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# 日志记录
def WriteLogging(message, content):
    pass

# 提问 数据库写入
def WriteQuestionDB(question, question_owner):
    try:
        import sqlite3
        con = sqlite3.connect(database = "db.sqlite3")
        db = con.cursor()
        db.execute("INSERT INTO Table_Name (question_owner, question) VALUES (? ,?)",(question_owner, question)) # 修改数据库，库名、表名、标签
        con.commit()
        con.close()
    except BaseException:
        SendEmail('WriteQuestionDB',BaseException)
        # 日志记录

# 问题发送
def SendMessage(content, member=None):
    # from * import * # 消息过滤
    try:
        from qqbot import _bot as bot
        bot.Login(['-q','549537094']) # change
    except BaseException:
        SendEmail('SendMessage',BaseException)
        # 日志记录
        return 0

    try:
        from time import sleep
        if member:
            for group in member:
                message = bot.SendTo(group,content)
                if '失败' in message:
                    pass # 日志记录
                sleep(0.5)
        else:
            for group in bot.List('group'):
                message = bot.SendTo(group,content)
                if '失败' in message:
                    pass # 日志记录
                sleep(0.5)
            # 日志记录
    except Exception as e:
        pass
        # 日志记录
