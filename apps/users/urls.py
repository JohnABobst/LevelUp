from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index ),    
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^validate_email$', views.validate_email),
    url(r'^logout', views.logout),
]
