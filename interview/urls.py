from django.urls import path
from . import views

urlpatterns = [
    path('', views.interview_dashboard, name='interview_dashboard'),
    path('add/', views.add_candidate, name='add_candidate'),
]