$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'ubuntu'): admin1
이메일 주소:
Password:
Password (again):
Superuser created successfully.



```python
from django.contrib import admin
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    # 메뉴에서 보일 attribute
    list_display = ('pk', 'title', 'content')
   
admin.site.register(Article, ArticleAdmin)
```

