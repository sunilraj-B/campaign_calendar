"""
URL configuration for server project.

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
from client.views import create_event,success,base_view,update_backlog,backlog_events,download_excel
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base_view, name='base'),
    path('create/', create_event, name='create_event'),
    path('success/', success, name='success'),
    path('update_backlog/', update_backlog, name='update_backlog'),
    path('backlog_events/', backlog_events, name='backlog_events'),
    path('download_excel/', download_excel, name='download_excel'),

]
