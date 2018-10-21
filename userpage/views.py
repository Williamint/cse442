from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponse
#from django.conf.urls import include
from django.template import loader
from django.http import HttpResponseRedirect
from library.usermodel import User


class UserPageView(TemplateView):
    template_name = "userpage.html"


def index(request):
        if request.GET.get('sigt'):
            User.clearInfo(User)
            return HttpResponseRedirect("http://localhost:8000/")
        elif request.GET.get('edit'):
            return HttpResponseRedirect('/userprofile/')
        elif request.GET.get('friend'):
            return HttpResponseRedirect('/friend_list/')
        else:
            return render(request, 'userpage.html', {'nickname': User.getusername(User)})


