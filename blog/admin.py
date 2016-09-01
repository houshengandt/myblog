from django.contrib import admin

from .models import Article, Comment, Tags
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Tags)
