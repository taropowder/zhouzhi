# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from zhou.models import Question,Answer,User_info,Original_Anwser
from zhou.date import send_qq,explode_word
import time
import hashlib
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 导入模块
from zhou.smt import  send_email
import smtplib
import re
# Create your views here.


def put_name(fun):
    def wap(request):
        try:
            context['name']=request.session['name']
        except:
            pass
        fun(request)
    return wa

def home(request):
    context = {}
    try:
        context['name']=request.session['name']
    except:
        pass
    return render(request,'index.html',context)

def register(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = ""
        user = User.objects.create_user(name,email, password)
        user.save()
        id=user.id
        User_info.objects.update_or_create(user_connect_id=id, user_integral=0)
        context['name'] = name
        return render(request, 'login.html', context)
    return render(request, 'register.html', context)
def userlogin(request):
    context = {}
    context['statu'] = '0'
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_password = request.POST.get('password')
        user = authenticate(username=get_name, password=get_password)
        if user is not None:
            if user.is_active:
                # print('用户验证并登录成功')
                request.session['name'] = get_name
                context['name']=get_name
                login(request, user)  # 这才是登录，才会写入session
                return render(request, 'index.html', context)
            else:
                context['statu'] = '1'
                context['error'] = "您的用户已经被限制,请联系工作人员"
                print('密码正确，但是用户无法登录')
        else:
            context['statu'] = '1'
            context['error'] = "用户名或者密码错误"
            # context['error'] = '用户不存在'

    return render(request, 'login.html', context)
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')
def before_search(request):
    context = {}
    if request.method == 'POST':
        old_search_content = request.POST.get('search')
        search_content=explode_word(old_search_content)
        may_words=[]
        for foos in search_content:
            may_word=Question.objects.filter(content__contains=foos)
            for foo in may_word:
                tmps = foo.content
                tmps_id = foo.id
                if tmps not in may_words:
                    may_words.append([tmps,tmps_id])
        # print(search_content)
        context['content'] = old_search_content
        context['old_questions']=may_words

    return render(request, 'before_search.html', context)
@login_required
def search(request):
    context = {}
    if request.method == 'POST':
        search_content = request.POST.get('search')
        user_name = request.session['name']
        question = Question()
        question.content=search_content
        question.qustion_user=User.objects.get(username=user_name)
        Users=User.objects.get(username=user_name)
        Users_id=Users.id
        userinfo = Users.info
        user_integral = userinfo.all().values_list('user_integral')
        user_integral=(user_integral[0][0]+10,)
        User_info.objects.filter(user_connect_id=Users_id).update(user_integral=user_integral[0])
        question.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        question.save()
        send_qq(question.id,question.content)
        context['name'] = request.session['name']
        context['content'] = search_content
    return render(request, 'persion_after_search.html', context)
@login_required
def persion(request):
    context = {}
    context['name'] = request.session['name']
    user = User.objects.get(username=context['name'])
    questions = user.question_set.order_by("time")
    questions.reverse
    question_list=[]
    question_anwser_list={}
    i=0
    tmp={}
    for question in questions:
        i=i+1
        question_time=question.time
        question_id=question.id
        an = question.answer
        ans = an.order_by("answer_rank")
        texts = ans.all().values_list('answer_text')
        answer_list = []
        for text in texts:
            text = "".join(tuple(text))
            answer_list.append(text)
        question_anwser_list['id']=question_id
        question_anwser_list['time']=question_time
        question_anwser_list['quesition']=question
        question_anwser_list['answers']=texts
        tmp[i]=question_anwser_list.copy()
        question_list.append(tmp[i])
    question_list.reverse()
    context['questions']=question_list
    # print(context['questions'])


    # 结束
    return render(request, 'persion_question.html', context)
def listing(request):
    contact_list = Contacts.objects.all()  # 获取所有model对象
    paginator = Paginator(contact_list, 25)  # 第二个参数是每页显示的数量
    page = request.GET.get('page')  # 获取URL参数中的page number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:  # 若不是整数则跳到第一页
        contacts = paginator.page(1)
    except EmptyPage:  # 若超过了则最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request,'list.html', {"contacts": contacts})
@login_required
def perion_anwser(request):
    context = {}
    context['name'] = request.session['name']
    user = User.objects.get(username=context['name'])
    userinfo = user.info
    # user_qq = userinfo.all().values_list('user_qq')
    user_answers = Original_Anwser.objects.filter(original_answer_user_id=user.id)
    answer_list = []
    for user_answer in user_answers:
        answer_text = user_answer.original_answer_text
        answer_list.append(answer_text)
    print(answer_list)
    context['anwsers'] = answer_list
    return render(request, 'persion_anwser.html', context)
def answer(request,questions_id):
    context = {}
    context['name'] = request.session['name']
    # questions_id=request.GET.get('question_id')
    if questions_id=='None' :
        context['answers']="没有数据"

    # print(questions_id)
    question=Question.objects.get(id=questions_id)
    context['question'] =question.content
    an = question.answer
    ans = an.order_by("answer_rank")
    texts = ans.all().values_list('answer_text')
    answer_list = []
    for text in texts:
        text="".join(tuple(text))
        answer_list.append(text)
    print(answer_list)
    context['answers'] = answer_list

    return render(request, 'answer.html', context)
@login_required
def change_password(request):
    context = {}
    context['status']=0
    if request.method == 'POST':
        get_name = request.session['name']
        get_password = request.POST.get('old_password')
        user = authenticate(username=get_name, password=get_password)
        if user is not None:
            u = User.objects.get(username=get_name)
            password=request.POST.get('password')
            if password:
                u.set_password(password)
                u.save()
                context['status'] = 1
                context['result'] = "修改成功"
                logout(request)
                return render(request, 'changepass.html', context)
            else:
                context['status'] = 1
                context['result'] = "密码不能为空"

        else:
            context['status'] = 1
            context['result'] = "密码错误"
    return render(request, 'changepass.html', context)
# def reset_password(request):
@login_required
def persion_integral(request):
    context = {}
    context['name'] = request.session['name']
    user = User.objects.get(username=context['name'])
    user_id=user.id
    userinfo = user.info
    user_integral = userinfo.all().values_list('user_integral')
    context['integral'] = user_integral
    questions = Question.objects.filter(qustion_user_id=user_id)
    questions_time=[]
    for question in questions:
        questions_time.append(question.time)
    context['questions']=questions_time
    anwsers = Original_Anwser.objects.filter(original_answer_user_id=user.id)
    anwsers_time = []
    for anwser in anwsers:
        anwsers_time.append(anwser.original_time)
    context['answers']=anwsers_time
    return render(request, 'persion_integral.html', context)
def hot(request):
    context = {}
    questions=Question.objects.order_by()
    questions_list=[]
    for question in questions:
        questions_list.append([question.id,question,question.time])
    questions_list.reverse()
    paginator=Paginator(questions_list,10)
    page= request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context['questions']=contacts
    context['count']=paginator.page_range
    print(contacts.count)
    return render(request, 'hot.html', context)
def re_bundling_qq(request):
    context = {}
    user_name = request.GET.get('name')
    user_qq = request.GET.get('user_qq')
    token=request.GET.get('token')
    user = User.objects.get(username=user_name)
    name_pass=user_name+user.password
    check_name=hashlib.md5()
    check_name.update(name_pass)
    check_pass=check_name.hexdigest()
    print(check_pass)
    if(check_pass==token):
        user_id = user.id
        User_info.objects.filter(user_connect_id=user_id).update(user_qq=user_qq)
    return render(request, 'send_sucess.html', context)
@login_required
def send_bundling_qq(request):
    context = {}
    context['status']=2
    user_name = request.session['name']
    user = User.objects.get(username=user_name)
    context['mail']=user.email
    context['mail']=re.sub(r'@.*$','',context['mail'])
    if request.method == 'POST':
        user_qq = request.POST.get('user_qq')
        # if user_qq==None:
        user_qq_email=user_qq+"@qq.com"
        # user_name = request.session['name']
        # user = User.objects.get(username=user_name)
        name_pass = user_name + user.password
        check_name = hashlib.md5()
        check_name.update(name_pass)
        token = check_name.hexdigest()
        url="rebundling/?token=%s&name=%s&user_qq=%s"%(token,user_name,user_qq)
        context['status']=send_email(user_qq_email,url)
        if context['status']:
            context['result']="激活邮件已经发送到您的邮箱请注意查收"
        else:
            context['result']='发送失败'
        return render(request, 'bundling.html', context)
    return render(request, 'bundling.html', context)
@login_required
def persion_center(request):
    context = {}
    context['name'] = request.session['name']
    user = User.objects.get(username=context['name'])
    context['email'] = user.email
    userinfo = user.info
    # user.id=
    # user_qq=userinfo.all().values_list('user_qq')
    context['qq'] = user.id
    return render(request, 'persion_center.html', context)
