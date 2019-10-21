from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tv/<str:tag>', views.tv, name='tv'),
]