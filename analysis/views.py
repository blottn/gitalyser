# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from secret import req, get_secret, get_id

from gitclient import *

import requests
import json
API_URL = 'https://api.github.com/'
USER = 'user/'

access_token = '';


#def index(request):
#	name = request.GET.get('name','blottn')
#	return HttpResponse(req(API_URL + USERS + name))

@csrf_protect
def index(request):
	c = {}
	c['code']=''
	if 'code' in request.GET:
		session_code= request.GET['code']
		c['code'] = session_code
		access_token = get_token(session_code)
		if access_token != 'Not Found':
			u_data = get_user(access_token)
			c['avatar']=u_data['avatar_url']
	c['client_id']=get_id()
	return render(request,'analysis/index.html', c)

def stats(request):
	return render(request,'analysis/stats.html')
