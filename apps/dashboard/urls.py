from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.dashboard),
    path("groups/", include('apps.groups.urls')),
    path('goals/', include('apps.goals.urls')),
    path('squad/', include('apps.squad.urls'))
]