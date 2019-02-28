# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world! This is the Index screen")

def form_view(request):
    return HttpResponse("This is the questionnaire")
