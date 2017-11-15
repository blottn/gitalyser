# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from secret import req, getSecret, getId

import requests

API_URL = 'https://api.github.com/'
USERS = 'users/'


#def index(request):
#	name = request.GET.get('name','blottn')
#	return HttpResponse(req(API_URL + USERS + name))

@csrf_protect
def index(request):
	session_code = ''
	if 'code' in request.GET:
		session_code = request.GET['code']
	c = {}
	c['client_id']=getId()
	c['code']=session_code
	return render(request,'analysis/index.html', c)

def stats(request):
	return render(request,'analysis/stats.html')
