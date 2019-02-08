# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Welcome to the Iskra esmorzar Homepage!', content_type='text/plain')
