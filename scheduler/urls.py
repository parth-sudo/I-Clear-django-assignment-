
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('schedule/', views.schedule, name = 'schedule'),
    path('ip/<int:pk>/', views.ping_detail, name = 'detail'),
]
