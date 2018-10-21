from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
# Create your views here.

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from library.usermodel import User


class UserPageView(TemplateView):
    template_name = "userprofile.html"


def index(request):
        if request.GET.get('save'):
            User.saveInfo(User, request.GET['uname'], request.GET['firstn'], request.GET['lastn'], request.GET['email'],
                          request.GET['bith'], request.GET['education'])
            return HttpResponseRedirect('/userpage/')
        elif request.GET.get('cancel'):
            # User.saveInfo(User, request.GET['uname'])
            return HttpResponseRedirect('/userpage/')
        else:
            return render(request, 'userprofile.html', {'usname': User.getusername(User),
                                                        'firstna': User.getfirstname(User),
                                                        'lastna': User.getlastname(User),
                                                        'emailv': User.getemail(User),
                                                        'eduv': User.geteducation(User),
                                                        'birth': User.getdobirth(User)})

