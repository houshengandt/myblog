from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archive/$', views.ArticleArchiveView.as_view(), name='archive'),
    url(r'^archive/(?P<year>[0-9]{4})/$', views.ArticleYearArchiveView.as_view(), name='year_archive'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.ArticleMonthArchiveView.as_view(), name='month_archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^tag/(?P<tag>.*)/$', views.TagView.as_view(), name='tag'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^admin/$', views.WarningView.as_view(), name='warning'),
    url(r'^workshop/$', views.WorkShopView.as_view(), name='workshop'),
]
