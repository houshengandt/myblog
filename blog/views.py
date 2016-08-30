from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import Article


class IndexView(ListView):
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    queryset = Article.objects.all().order_by('-pub_time')