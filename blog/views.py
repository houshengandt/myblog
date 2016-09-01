from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe
from markdown import markdown

from .models import Article, Tags
from myblog.settings import MARKDOWNX_MARKDOWN_EXTENSIONS


class IndexView(ListView):
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    queryset = Article.objects.all().order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = mark_safe(markdown(obj.body, extensions=MARKDOWNX_MARKDOWN_EXTENSIONS))
        return obj
