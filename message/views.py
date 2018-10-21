from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect


def index(request):
    if request.GET.get('end'):
        return HttpResponseRedirect('/userpage/')

    return render_to_response('message.html')
