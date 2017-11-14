# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from secret import req

import requests

API_URL = 'https://api.github.com/'
USERS = 'users/'


#def index(request):
#	name = request.GET.get('name','blottn')
#	return HttpResponse(req(API_URL + USERS + name))

@csrf_protect
def index(request):
	c = {}
	return HttpResponse(render(request,'analysis/index.html', c))

@csrf_protect
def login(request):
	c = {}
	return HttpResponse(render(request,'analysis/login.html', c))

@csrf_protect
def callback(request):
	c = {}
	c['name'] = request.POST['uname']
	c['pass'] = request.POST['pw']
	return HttpResponse(render(request,'analysis/callback.html', c))
