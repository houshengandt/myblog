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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = mark_safe(markdown(obj.body, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS))
        obj.viewed()
        return obj

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['latest'] = Article.objects.all().order_by('-pk')[:10]
        return context


class ArticleArchiveView(ArchiveIndexView):
    model = Article
    date_field = 'pub_time'


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_time'
    context_object_name = 'article_list'
    make_object_list = True


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = 'pub_time'
    month_format = '%m'
    context_object_name = 'article_list'
    make_object_list = True


class TagView(ListView):
    context_object_name = 'articles'
    template_name = 'blog/tag.html'

    def get_queryset(self):
        return Article.objects.filter(tags__tag_name=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['the_tag'] = Tags.objects.filter(tag_name=self.kwargs['tag'])
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class WarningView(TemplateView):
    template_name = 'warning.html'


class WorkShopView(TemplateView):
    template_name = 'workshop.html'