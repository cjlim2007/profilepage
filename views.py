from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

def home(request):
    return render(request, "home.html")

def info(request):
    return render(request, "info.html")

def profile(request):
    return render(request, "profile.html")