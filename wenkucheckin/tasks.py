from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
import pickle
import time
from myblog.settings import BASE_DIR
from .models import BaiduUser

session_dir = os.path.join(BASE_DIR, 'static', 'sessions')


@shared_task
def check_in():
    accounts = BaiduUser.objects.all()
    for account in accounts:

        with open(os.path.join(session_dir, account.username, account.username + '.pk'), 'rb') as f:
            login_session = pickle.load(f)
        login_session.check_in()
        account.ticket = login_session.check_tickets()
        account.check_in_times += 1
        account.save()
        time.sleep(600)
