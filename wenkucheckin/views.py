from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView
import os
import pickle
from myblog.settings import BASE_DIR
from .models import BaiduUser

from .baidulogin import LoginBaiduWenku


class IndexView(ListView):
    model = BaiduUser
    template_name = 'wenkucheckin/index.html'


session_dir = os.path.join(BASE_DIR, 'wenkucheckin', 'static', 'sessions')

def add_baidu_account(request):
    username = request.POST['baiduaccount']
    password = request.POST['password']

    if not os.path.exists(session_dir):
        os.mkdir(session_dir)
    user_dir = os.path.join(session_dir, username)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    info = BaiduUser(username=username, password=password)

    login_session = LoginBaiduWenku(username=username, password=password)
    login_session.download_verifycode(path=os.path.join(user_dir, 'verifycode.png'))
    info.save()
    with open(os.path.join(user_dir, username+".pk"), 'wb') as f:
        pickle.dump(login_session, f)
    return render(request, template_name='wenkucheckin/verify.html', context={'img': 'sessions/' + username + '/verifycode.png',
                                                                              'username': username})


def verify_login(request):
    username = request.POST['username']
    verify_code = request.POST['verifycode']
    with open(os.path.join(session_dir, username, username + '.pk'), 'rb') as f:
        login_session = pickle.load(f)
    login_session.get_verifycode(verify_code)
    login_session.login()
    with open(os.path.join(session_dir, username, username + '.pk'), 'wb') as f:
        pickle.dump(login_session, f)
    return redirect("index")
