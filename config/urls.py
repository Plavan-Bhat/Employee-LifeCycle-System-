"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('interview/', include('interview.urls')),
    path('onboarding/', include('onboarding.urls')),
    path('assets-it/', include('assets_it.urls')),
    path('assets-admin/', include('assets_admin.urls')),
    path('exit/', include('exit_process.urls')),
    path('users/', include('users.urls')),
    path('notifications/', include('notifications.urls')),
    path('audit/', include('audit_logs.urls')),
]
