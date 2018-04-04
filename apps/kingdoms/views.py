from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


def index(request):
	return render(request, 'kingdoms/main.html')

def maps(request):
	return render(request, 'kingdoms/maps.html')

def characters(request):
	return render(request, 'kingdoms/characters.html')

