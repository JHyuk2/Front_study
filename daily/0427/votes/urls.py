from django.urls import path
from . import views

app_name = 'votes'

urlpatters = [
    path('', views.index, name='index'),
]