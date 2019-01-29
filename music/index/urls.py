from django.urls import path
from . import views

# 设置首页的URL地址信息
urlpatterns = [
    path('', views.indexView, name='index'),
]

