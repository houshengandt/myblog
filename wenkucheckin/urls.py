from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add-baidu-account/', views.add_baidu_account, name='add_account'),
    url(r'^verify-login/', views.verify_login, name='verify_login'),
]