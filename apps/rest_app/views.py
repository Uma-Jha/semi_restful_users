# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
	return render(request, 'rest_app/index.html', {"users": User.objects.all()})

def new(request):
	return render(request, 'rest_app/new.html')

def show(request, number):
	return render(request, 'rest_app/show.html', {"user": User.objects.get(id=number)})

def edit(request, number):
	return render(request, 'rest_app/edit.html', {"user":User.objects.get(id=number)})

def destroy(request, number):
	User.objects.get(id=number).delete()
	return redirect('/users')

def update(request, number):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.iteritems():
			messages.error(request, value)
		return redirect('/users/edit/'+number)
	else:
		user = User.objects.get(id=number)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return render(request, 'rest_app/show.html', {"user": user})

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.iteritems():
			messages.error(request, value)
		return redirect('/users/new')
	else:
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		return redirect('/users')

