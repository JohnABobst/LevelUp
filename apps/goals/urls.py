from django.urls import path
from . import views
urlpatterns = [ 
    path('goals/', views.goals),
    path('goal_setup/', views.goal_setup),   
    path('accomplishments/', views.accomplishments),
    

]