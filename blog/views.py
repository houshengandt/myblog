from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView

from .models import Article, Tags


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
