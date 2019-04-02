"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from ToDoApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('/create_schedule', views.create_schedule, name='create_schedule'),
    path('/delete_schedule', views.delete_schedule, name='delete_schedule'),
    path('/update_schedule', views.update_schedule, name='update_schedule'),
    path('/update_schedule_complete', views.update_schedule_complete, name='update_schedule_complete'),
    path('/submit_email', views.submit_email, name='submit_email'),
]
