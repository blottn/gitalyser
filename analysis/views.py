# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
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

	#if logged in:
	if not 'tok' in request.session:
		request.session['tok'] = ''
	
	if request.session['tok'] == '' and 'code' in request.GET:
		session_code = request.GET['code']
		access_token = get_token(session_code)
		if access_token != 'Not Found':
			request.session['tok'] = access_token

	if request.session['tok'] == '' :
		return render(request,'analysis/index.html',{'client_id':get_id()})
	
	c = {'signin':True}
	access_token = request.session['tok']
	u_data = get_user(access_token)
	if access_token != 'Not Found':
		request.session['tok'] = access_token
		c['avatar']=u_data['avatar_url']
	request.session['user'] = u_data['login']
	repos = get_repos(access_token)
	c['repos'] = []
	for repo in repos:
		c['repos'].append({'name':repo['name'],'owner':repo['owner']['login']})
	
	c['client_id']=get_id()

	return render(request,'analysis/index.html', c)

def stats(request):
	return render(request,'analysis/stats.html')


def signout(request):
	if not 'tok' in request.session:
		request.sesion['tok'] = ''

	request.session['tok'] = ''
	return redirect('index')

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
	if not 'tok' in request.session or request.session['tok']:
		redirect('index')

	token = request.session['tok']
	repo = request.GET['repo']
	user = request.session['user']
	owner = request.GET['owner']

	context = {}
	context['repo_name'] = repo
	context['contributors'] = []
	commits = get_commits(token,repo,owner)
	authors = {}
	for commit in commits:
		if commit['author'] != None:
			if commit['author']['login'] in authors:
				authors[commit['author']['login']] += 1
			else:
				authors[commit['author']['login']] = 0

	#now scale between 100 and 0 for each
	scale = 100
	max_v = 0
	for key in authors:
		if authors[key] > max_v:
			max_v = authors[key]
	
	for key in authors:
		authors[key] /= float(max_v)
		authors[key] *= scale
		
	for key in authors:
		context['contributors'].append({'name':key,'value':authors[key]})
	context['contributors'] = json.dumps(context['contributors'])
	return render(request,'analysis/leach.html',context)
