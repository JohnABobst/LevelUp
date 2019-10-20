from django.shortcuts import render
from . import views
# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def settings(request):
    pass