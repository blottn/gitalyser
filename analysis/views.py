# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from secret import req

import requests

API_URL = 'https://api.github.com/'
USERS = 'users/'


#def index(request):
#	name = request.GET.get('name','blottn')
#	return HttpResponse(req(API_URL + USERS + name))

def index(request):
	return HttpResponse(render(request,'analysis/index.html'))

def callback(request):
	return HttpResponse('Successfully authenticated! don\'t think this page is needed')
