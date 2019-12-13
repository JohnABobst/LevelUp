from django.urls import path 
from . import views
urlpatterns = [
    path('', views.squad),
    path('<str:username>/', views.profile),
]