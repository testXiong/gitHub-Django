

# 全局路由配置信息
from django.urls import path

from projects import admin
from projects.apps import index
from .apps import  IndexView,IndexRender,IndexJsonResponse

urlpatterns = {

    # 这里的admin 为Django自带的类 里边有一些封装的方法 修改登录密码等等
    #调用类请求，类请求一定要加 as_view()固定形式
    path('IndexView/',IndexView.as_view()),
    #调用方法请求
    path('index/',index),
    #调用一个请求网页
    path('IndexRender/',IndexRender.as_view()),

    #前后端分离项目，调用一个返回 json
    path('IndexJsonResponse/<int:pk>/',IndexJsonResponse.as_view()),
}
