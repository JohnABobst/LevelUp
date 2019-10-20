from django.urls import path 

urlpatterns = [
    path('', views.groups),
    path('<str:group_name>/',views.group_detail),
    path('<str:group_name>/members', views.group_members),
    
]
