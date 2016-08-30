from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article_detail')
]