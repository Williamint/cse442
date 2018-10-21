from django.shortcuts import render, render_to_response
from library import databasecheck
# Create your views here.

from django.views.generic.base import TemplateView

from django.http import HttpResponseRedirect
from library.checkinput import Check
from library.usermodel import User


class HomePageView(TemplateView):
    template_name = "homepage.html"


def index(request):
        #databasecheck.SubmitSignUp(2, 'William', 'Aa11235813', 'Empty', 'WeiBin', 'Hu', 'weibinhu@buffalo', '', '08201996')
        if request.GET.get('log'):
            if Check.checkhomepage(Check, request.GET['uname'], request.GET['password']):
                User.setInfo(User, request.GET['uname'], request.GET['password'])
                return HttpResponseRedirect('/userpage/')
            else:
                error = Check.geterror(Check)
                return render(request, 'homepage.html', {'errormsg': [error]})
        elif request.GET.get('sig'):
            return HttpResponseRedirect('/signup/')
        else:
            return render_to_response('homepage.html')
