# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from secret import *

from gitclient import *

import requests
import json
import os
API_URL = 'https://api.github.com/'
USER = 'user/'

access_token = '';

def index(request):
	c = {}
	c['code']=''
	if 'code' in request.GET:
		session_code= request.GET['code']
		c['code'] = session_code
		access_token = get_token(session_code)	#add redirect if no access_token acquired
		if access_token != 'Not Found':
			u_data = get_user(access_token)
			repos = get_repos(access_token)
			results = get_commits(access_token,u_data['login'])
			c['avatar']=u_data['avatar_url']
			c['repos']=repos
			c['results']="hello from the other side"
	c['client_id']=get_id()
	return render(request,'analysis/index.html', c)

def stats(request):
	return render(request,'analysis/stats.html')


