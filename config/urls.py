"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pybo import views

#app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('pybo/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>',
         views.answer_create, name='answer_create'),
    path('admin/', admin.site.urls),
]
