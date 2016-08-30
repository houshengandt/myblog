from django.shortcuts import render, HttpResponse


def index(requset):
    return render(requset, 'blog/index.html')