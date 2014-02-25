from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from google.appengine.api import users
from google.appengine.api import images
import os
import sys
import models


'''def user_home(request):
    user_function = users.get_current_user() 
    filedir = sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))) 
    contributed_list = []
    started_list = []
    paid=0
    a=models.UserData()
    if user_function:
        username = user_function.nickname()  
        email = user_function.email()
        href = users.create_logout_url('/home')

        for i in a.query(a._properties['username'] == username):
            contributed_list.append(i.contributed_to)
        for j in a.query(a._properties['username'] == username):
            started_list.append(i.started)
        for k in a.query(a._properties['username'] == username):
            paid=k.paid
	
        if (not models.UserData.query(models.UserData.username == user_function.nickname(),models.UserData.email == user_function.email()).get()):
            query = models.UserData(username=user_function.nickname(), email=user_function.email())
            query.put()
        else:
            pass
    else:
        username = user_function.nickname()
        email = user_function.email()
        href = users.create_login_url('/home')
    return render(request, 'profile.html', { 'href': href, 'email': email, 'username': username, 'filedir': filedir, 'contributed_list': contributed_list, 'started_list':started_list, 'paid': paid})

def project(request):
    user_function = users.get_current_user() 
    b=models.UserData()
    if b.query(b._properties['username'] == username):
        date = b.query(b._properties['username'] == username).date
    for k in a.query(a._properties['username'] == username):
        payment=int(payment)+int(k.paid)
    if b.query(b._properties['username'] == username):
        title = b.query(b._properties['username'] == username).title
    return render(request, 'project.html', {'date': date, 'payment': payment, 'title': title})'''

def home(request):
    
    return render(request, 'home.html')

def user_home(request ):
    user_function = users.get_current_user() 
    a=models.UserData()
    if user_function:
        username = user_function.nickname()  
        email = user_function.email()
        href = users.create_logout_url('/home')

    else:
        username = user_function.nickname()
        email = user_function.email()
        href = users.create_login_url('/home')
    return render(request, 'profile.html', {'email': email, 'username': username,
    'href':href})

def upload(request):
    avatar = images.resize(self.request.get('img'),32,32)
    q = models.UserData()
    user_image = avatar
    user_function = users.get_current_user() 
    username = user_function.nickname()
    for i in q.query(q._properties['user_name'] == username):
        i.user_image = Avatar
        i.put()
    

def profile(request):
    user_function = users.get_current_user() 
    a=models.UserData()
    if user_function:
        username = user_function.nickname() 
        if username not in a.query(a._properties['username']):
            pass
        email = user_function.email()
        href = users.create_logout_url('/home')

    else:
        username = user_function.nickname()
        email = user_function.email()
        href = users.create_login_url('/home')
    return render(request, 'profile.html', {'email': email, 'username': username,
    'href':href})


        '''for i in a.query(a._properties['username'] == username):
            contributed_list.append(i.contributed_to)
        for j in a.query(a._properties['username'] == username):
            started_list.append(i.started)
        for k in a.query(a._properties['username'] == username):
            paid=k.paid
	
        if (not models.UserData.query(models.UserData.username == user_function.nickname(),models.UserData.email == user_function.email()).get()):
            query = models.UserData(username=user_function.nickname(), email=user_function.email())
            query.put()
        else:
            pass'''











