from django.contrib import admin
from .models import Board
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_display_links =['title']
    list_filter = ['created_at']
    
admin.site.register(Board, BoardAdmin)