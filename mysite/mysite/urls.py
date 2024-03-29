"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
# 맨아래 내용을 주석처리하고 include를 추가함
from django.urls import path, include
# from pybo import views(더이상필요하지 않으므로 주석처리함)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pybo/', views.index),
    path('pybo/', include('pybo.urls')),# pybo/로 시작하는 파일을 매핑정보를 읽어서 처리하라는 의미
]
