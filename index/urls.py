"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from . import views
urlpatterns = [
 #   path('download.html', views.download),
    # 首页的URL
re_path('(?P<year>[0-9]{4}.html)',views.myyear,name='myyear')
 #   path('login.html', views.login),
    # 通用视图
    # path('index/', views.ProductList.as_view()),
 #   path('index/<id>.html', views.ProductList.as_view(),{'name':'phone'})
]
