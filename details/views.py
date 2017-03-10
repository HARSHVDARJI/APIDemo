from __future__ import print_function
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
import json
from django.core import serializers

from .models import UserDetails
from .forms import Userform

def home(request):
    return render(request,'demo.html')
def log(request):
    return render(request,'login.html')

def DisplayUserDetails(request):
    if request.GET:
        try:
            userDetails = UserDetails.objects.filter(fname = request.GET['fname'])
        except Exception:
            return HttpResponse(json.dumps("{'Error' : 'No data Found'}"), content_type='application/json')

    else:
        userDetails = UserDetails.objects.all()
    return HttpResponse(serializers.serialize("json",userDetails),content_type='application/json')

'''def formexample(request):
    if request.GET:
        form = Userform(request.GET)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = Userform()

    return render(request, "demo.html", {'form': form})'''

def example(request):
    if request.POST:
        data = Userform(request.POST)
        if data.is_valid():
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            query = UserDetails(fname = fname, lname = lname, email = email)
            query.save()
        else:
            return render(request, 'error.html')
    return render(request,'success.html')

def login(request):
    if request.POST:
        fname = request.POST.get('fname')
    queryset = UserDetails.objects.filter(fname= fname)
    return render(request, 'profile.html', {'details': queryset})