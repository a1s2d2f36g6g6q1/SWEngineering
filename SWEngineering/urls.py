"""
URL configuration for SWEngineering project.

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
from django.urls import path
from .views import beginner, index, predict, stock
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("index.html", index, name="index"),
    path("beginner.html", beginner, name="beginner"), # 입문자용 정보 페이지
    path("stock.html", stock, name="stock"), # 주식 차트 페이지
    path("predict.html", predict, name="predict"), # 주식 예측 페이지
]
