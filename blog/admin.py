from django.contrib import admin

from .models import Article, Comment, Tags


admin.site.register(Article)
admin.site.register(Tags)
