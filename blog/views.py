from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView

from .models import Article


class IndexView(ListView):
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    queryset = Article.objects.all().order_by('-pub_time')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'
