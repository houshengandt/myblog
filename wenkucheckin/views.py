from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView, ListView
from django.core.exceptions import ObjectDoesNotExist
import os
import shutil
import pickle
import logging
from myblog.settings import BASE_DIR
from .models import BaiduUser

from .baidulogin import LoginBaiduWenku

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(BASE_DIR, 'wenku.log'),
                    filemode='w')
logger = logging.getLogger('wenku')


class IndexView(ListView):
    model = BaiduUser
    template_name = 'wenkucheckin/index.html'


session_dir = os.path.join(BASE_DIR, 'static', 'sessions')


def add_baidu_account(request):
    username = request.POST['baiduaccount']
    password = request.POST['password']
    try:
        # 判断用户名是否被注册
        BaiduUser.objects.get(username=username)
    except ObjectDoesNotExist:
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
    else:
        return redirect('wenkuindex')


def verify_login(request):
    username = request.POST['username']
    verify_code = request.POST['verifycode']
    try:
        with open(os.path.join(session_dir, username, username + '.pk'), 'rb') as f:
            login_session = pickle.load(f)
        login_session.get_verifycode(verify_code)
        login_session.login()
        with open(os.path.join(session_dir, username, username + '.pk'), 'wb') as f:
            pickle.dump(login_session, f)
    except Exception as e:
        logger.error('login error')
        logger.error(e)
    finally:
        return redirect("wenkuindex")


def delete_baidu_account(request, pk):
    account = BaiduUser.objects.get(pk=pk)
    username = account.username
    account.delete()
    user_dir = os.path.join(session_dir, username)
    if os.path.exists(user_dir):
        shutil.rmtree(user_dir)
    return redirect("wenkuindex")


