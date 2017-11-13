# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from secret import req

import requests

def index(request):
	return HttpResponse(req())

def callback(request):
	return HttpResponse('Successfully authenticated!')
