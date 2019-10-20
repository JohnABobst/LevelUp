from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from apps.users.models import *
import bcrypt
import json
# Create your views here.
def index(request):
    return render(request,'registration.html')

def login(request):
    form = request.POST 
    email = form['email']
    password = form['password']
    user = User.objects.filter(email=email)
    print(user)
    if user:
        logged_user = user[0]
        print(bcrypt.checkpw(password.encode(), logged_user.password.encode()))
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session['email'] = logged_user.email
            request.session['user'] = logged_user.first_name
            return redirect('/dashboard')
        else:
            messages.error(request, 'Incorrect password')
    else:
        messages.error(request, 'No user with that email exists, please register')        
    return redirect('/')


def register(request):
    form = request.POST
    errors = User.objects.basic_validator(form)
    if len(errors)> 0:
        for key in errors:
            messages.error(request, errors[key])
        return redirect('/')
    else:        
        first_name = form['first_name']
        last_name = form['last_name']
        password = form['password']
        birthday = form['birthday']
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        email = form['email']
        user = User.objects.create(
            first_name = first_name,
            last_name=last_name,
            password=hashed,
            email=email,
            birthday=birthday
        )
        user.save()        
        request.session['userid'] = user.id
        request.session['email'] = user.email
        request.session['user'] = user.first_name      
        return redirect('/dashboard')

def success(request):
    return render(request,'success.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def validate_email(request):
    email = request.POST['email']
    print(email)
    print(request)
    print(User.objects.filter(email=email))
    if User.objects.filter(email=email):
        return JsonResponse(
            {'result': 'An account with that email already exists'})
    else:
        return JsonResponse({'result': 'Email is valid'})

    

        
