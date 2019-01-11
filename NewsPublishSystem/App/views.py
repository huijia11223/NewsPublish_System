from django.shortcuts import render, redirect, HttpResponse
from .forms.register import RegisterForm
from .forms.login import LoginForm
from .forms.editUser import EditUser
from .forms.loginPublisher import LoginPublisher
from django.contrib.auth import logout
from .models import User, NewPublisher
import time
import random


# Create your views here.


def index(request):
    uid = request.session.get("uid")
    user = request.session.get("username")
    return render(request, "index.html", {'username': user, 'uid': uid})


def index2(request, uid):
    data = User.objects.filter(uid=uid).values().first()
    uid = data['uid']
    username = data['username']
    return render(request, 'index.html', {'uid': uid, "username": username})


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['username']
            passwd = f.cleaned_data['password']
            try:
                user = User.objects.get(username=name)
                if user.password != passwd:
                    message = "密码错误"
                    return render(request, 'login.html', {"obj": f, "message": message})
            except User.DoesNotExist:
                message = "用户不存在"

                return render(request, 'login.html', {'obj': f, 'message': message})

            request.session['username'] = user.username
            request.session['uid'] = user.uid
            uid = request.session.get('uid')
            username = request.session.get("username")

            return render(request, 'index.html', locals())

        obj = LoginForm(request.POST)
        return render(request, 'login.html', {'obj': obj})
    else:
        obj = LoginForm()
        return render(request, "login.html", {'obj': obj})


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get("email")
        country = request.POST.get("country")
        idNumber = request.POST.get("idNumber")
        token = time.time()+random.randrange(1, 100000)
        usertoken = str(token)
        uid = random.randrange(1, 1000)
        uid = str(uid)

        user = User.createUser(uid, name, password, phone,
                               email, country, idNumber, usertoken)
        user.save()
        request.session['uid'] = uid
        request.session['username'] = name
        request.session['usertoken'] = usertoken
        return redirect('/index/')

    obj = RegisterForm()
    return render(request, 'register.html', {'obj': obj})


def quit(request):
    logout(request)
    return redirect('/index/')


def mine(request, uid):
    obj = User.objects.filter(uid=uid).values().first()
    return render(request, 'mine.html', locals())

# 初始化资料首页


def initMaterial(request, uid):
    row = User.objects.filter(uid=uid).values(
        'uid', 'username', 'phone', 'email', 'country', 'idNumber').first()
    udata = EditUser(initial=row)
    return render(request, 'mine.html', {'uid': uid, 'udata': udata})


def ModifyData(request, uid):
    if request.method == 'POST':
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        country = request.POST.get("country")
        User.objects.filter(uid=uid).update(
            username=username, phone=phone, email=email, country=country)
        return redirect('/mine/%d' % int(uid))


def military(request):
    return render(request, 'military.html')


def science(request):
    return render(request, 'science.html')


def base(request):
    return render(request, 'base.html')


def newPublisherLogin(request):
    if request.method == 'POST':
        f = LoginPublisher(request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            passwd = f.cleaned_data['passwd']
            try:
                newPublisher = NewPublisher.objects.get(username=username)
                if newPublisher.password != passwd:
                    return HttpResponse("password error")
            except NewPublisher.DoesNotExist:
                return HttpResponse("account is not exist")
            return render(request, 'NewPublisher/indexPublisher.html')
    else:
        newpublisher = LoginPublisher()
        return render(request, "NewPublisher/login.html", {'obj': newpublisher})

def publisherExit(request):
    newpublisher = LoginPublisher()
    return render(request, "NewPublisher/login.html", {'obj': newpublisher})
