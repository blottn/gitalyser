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
		
		access_token = get_token(session_code)
		
		u_data = get_user(access_token)
		if access_token != 'Not Found':
			request.session['tok'] = access_token

			c['avatar']=u_data['avatar_url']
		request.session['user'] = u_data['login']
		repos = get_repos(access_token)
		c['repos'] = []
		for repo in repos:
			c['repos'].append({'name':repo['name']})
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

def leach(request):
	token = request.session['tok']
	repo = request.GET['repo']
	user = request.session['user']

	context = {}
	context['repo_name'] = repo
	context['contributors'] = []
	contribs = get_contribs(token,user,repo)
	for contrib in contribs:
		context['contributors'].append({'name':contrib['login'],'leach':is_leach(token,contrib['login'])})
	return render(request,'analysis/leach.html',context)
