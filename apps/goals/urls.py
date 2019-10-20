from django.urls import path

urlpatterns = [ 
    path('goals/', views.goals),
    path('goal_setup/', views.goal_setup),   
    path('acheivements/', views.acheivements),    
    

]