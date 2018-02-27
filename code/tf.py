# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
NUM_LENGTH = 6

def SendEmail(Message,Except='error'):
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

def WriteQuestionDB(answer,question_id,qq):
    try:
        import sqlite3
        con = sqlite3.connect('db.sqlite3')
        db = con.cursor()
        db.execute("INSERT INTO Table_Name (answer, question_id, answer_owner) VALUES (? ,? ,?)",(answer,question_id,qq))
        con.commit()
        con.close()
    except BaseException:
        pass
    
def WritePerfcetDB(answer,question_id):
    try:
        import sqlite3
        con = sqlite3.connect('db.sqlite3')
        db = con.cursor()
        db.execute("INSERT INTO Table_Name (answer, question_id) VALUES (? ,?)",(answer,question_id))
        con.commit()
        con.close()
    except BaseException:
        pass

def SelectAnswerDB(question_id):
    import sqlite3
    con = sqlite3.connect(database="db.sqlite3")
    db = con.cursor()
    answers = []
    answers_str = None
    for answer in db.execute('SELECT answer_text FROM zhou_answer WHERE quesion_answer_id = ?;',question_id):
        answers.append(answer[0])
        answers_str += answer + ' '
    con.close()
    return answers, answers_str

def Summary(question_id, answer, qq):
    WriteQuestionDB(answer,question_id,qq)
    try:
        # 获取全部答案
        answers,answers_str = SelectAnswerDB(question_id)
    except BaseException:
        pass

    Tf_Idf = jieba.analyse.extract_tags(answers_str)
    sgin = ',.!%?:;\'\"=+-_，。！？：；‘”@～、'
    later = []
    perfcet = []
    for answer_ in answers:
        later_ = None
        for i in jieba.cut(answer_):
            if i in Tf_Idf or i in sgin:
                later_ += i
        if later_ in later:
            if later_ in perfcet:
                continue
            else:
                perfcet.append(later_)
        later.append(later_)
        
    for perfcet_answer in perfcet:
        WritePerfcetDB(perfcet_answer,question_id)
    
    return len(perfcet)

def dataManage(MyName, content,answer_owner_qq):
    from collections import Counter
    content.replace('@'+MyName,'')
    word_count = Counter(jieba.cut(content))

    # 获取问题ID
    serial_id = None
    for element in word_count:
        try:
            int(element)
            if len(element) != NUM_LENGTH:
                if serial_id is None:
                    serial_id = element
                else:
                    SendEmail('con\'t find serial_id')
                    return -1,None
            else:
                continue
        except:
            continue
    # 未找到ID处理
    if serial_id == None:
        return -1,'没有识别到问题ID呀，若已输入ID请与管理员联系'
    
    content.replace(serial_id,'')
    return Summary(serial_id,content,answer_owner_qq),None