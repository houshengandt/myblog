from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='wenkuindex'),
    url(r'^add-baidu-account/', views.add_baidu_account, name='add_account'),
    url(r'^delete-baidu-account/(?P<pk>.*)/', views.delete_baidu_account, name='delete_account'),
    url(r'^verify-login/', views.verify_login, name='verify_login'),
]