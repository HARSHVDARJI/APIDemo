from django.shortcuts import render, HttpResponse

# Create your views here.
import json
from django.core import serializers

from .models import UserDetails

def DisplayUserDetails(request):
    if request.GET:
        try:
            userDetails = UserDetails.objects.filter(fname = request.GET['fname'])
        except Exception:
            return HttpResponse(json.dumps("{'Error' : 'No data Found'}"), content_type='application/json')

    else:
        userDetails = UserDetails.objects.all()
    return HttpResponse(serializers.serialize("json",userDetails),content_type='application/json')