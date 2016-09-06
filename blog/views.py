from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.utils.safestring import mark_safe
from django.db.models import Count
from django.db.models.expressions import DateTime
from markdown import markdown
import pytz

from .models import Article, Tags
from myblog.settings import MARKDOWNX_MARKDOWN_EXTENSIONS


class IndexView(ListView):
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    queryset = Article.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['dates'] = Article.objects.datetimes('pub_time', 'month', order='DESC')
        # context['num'] = Article.objects.all().annotate(month=DateTime("pub_time", "month", pytz.timezone("Etc/UTC"))).\
        #     values("month").\
        #     annotate(created_count=Count('id'))
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = mark_safe(markdown(obj.body, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS))
        return obj

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['latest'] = Article.objects.all().order_by('-pk')[:10]
        return context


class ArticleArchiveView(ArchiveIndexView):
    model = Article
    date_field = 'pub_time'

    def get_context_data(self, **kwargs):
        context = super(ArticleArchiveView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['dates'] = Article.objects.datetimes('pub_time', 'month', order='DESC')
        return context


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_time'
    context_object_name = 'article_list'
    make_object_list = True

    def get_context_data(self, **kwargs):
        context = super(ArticleYearArchiveView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['dates'] = Article.objects.datetimes('pub_time', 'month', order='DESC')
        return context


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_time'
    month_format = '%m'
    context_object_name = 'article_list'
    make_object_list = True

    def get_context_data(self, **kwargs):
        context = super(ArticleMonthArchiveView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        context['dates'] = Article.objects.datetimes('pub_time', 'month', order='DESC')
        return context


class AboutView(TemplateView):
    template_name = 'about.html'