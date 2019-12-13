from django.shortcuts import render
from .models import * 


def goals(request):
    context = {
        'goals': Goal.objects.filter(user= request.user, accomplished=False)
    }
    return render(request, 'goals/goals.html', context)

def goal_setup(request):
    pass 

def accomplishments(request):
    context = {
        'accomplishments': Goal.objects.filter(user=request.user, accomplished=True)
    }
    return render(request, 'goals/accomplishments.html', context)


    