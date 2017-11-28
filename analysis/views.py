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
from datetime import datetime

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
			commits = dictify(get_commits(access_token,u_data['login']))
			c['commits']=json.dumps(commits.keys())
			c['avatar']=u_data['avatar_url']
			c['repos']=repos
			c['results']="hello from the other side"
	c['client_id']=get_id()
	return render(request,'analysis/index.html', c)

def stats(request):
	return render(request,'analysis/stats.html')

fmt_string = '%Y-%m-%dT%H:%M:%SZ'


#helper for sorting commits
def dictify(commits):
	out = {}
	for commit in commits:
		time = datetime.strptime(commit['commit']['committer']['date'],fmt_string).strftime('%s')
		if time in out:
			out[time] += 1
		else:
			out[time] = 1
	return out
