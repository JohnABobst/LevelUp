from django.urls import path 

urlpatterns = [
    path('', views.squad)
    path('squad/<str:username>/', views.profile),
]