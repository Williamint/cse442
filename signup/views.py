from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse
#from django.conf.urls import include
from django.template import loader
from django.http import HttpResponseRedirect
from library.checkinput import Check
from library import databasecheck
from library.usermodel import User

class HomePageView(TemplateView):
    template_name = "signup.html"


def index(request):
        if request.GET.get('sav'):
            if Check.checksignuppage(Check, request.GET['uname'], request.GET['pword'], request.GET['email'], request.GET['dob']):
                databasecheck.SubmitSignUp(request.GET['uname'], request.GET['pword'], 'Empty User Story', request.GET['firstn'], request.GET['lastn'], request.GET['email'], '', request.GET['dob'])
                return HttpResponseRedirect('http://localhost:8000/')
            else:
                return render(request, 'signup.html', {'errormsg': [Check.geterror(Check)]})
        elif request.GET.get('cancel'):
            return HttpResponseRedirect('http://localhost:8000/')
        else:
            return render_to_response('signup.html')

