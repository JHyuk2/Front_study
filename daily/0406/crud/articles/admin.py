from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 메뉴에서 보임
    list_display = ('pk', 'title', 'content')

admin.site.register(Article)