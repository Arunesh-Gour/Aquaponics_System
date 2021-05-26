from django.http import (Http404, HttpResponse, HttpResponseRedirect,)
from django.shortcuts import (render, get_object_or_404, redirect,)
from django.urls import reverse

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from . import DBReader
dbreader = DBReader.DBReader()
dbreader.start()

# from .models import ()

# Create your views here.

# def index (request):
#    return render(request, 'management/index.html',)

def index (request):
   return redirect ('management:home')

def home (request):
   return render(request, 'management/home.html')

@csrf_protect
def userlogin (request):
   username = request.POST['username']
   password = request.POST['password']
   user = authenticate(request, username=username, password=password)
   
   if user is not None:
      login(request, user)
      return redirect('management:dashboard')
   else:
      return redirect('management:home')

def userlogout (request):
   logout(request)
   return redirect('management:home')

@login_required(login_url='/home/')
def dashboard (request):
   return render(
      request,
      'management/dashboard.html',
      {
         'tankList' : tuple(DBReader.dataFiles.keys()),
      },
   )

@csrf_exempt
@login_required(login_url='/home/')
def fetchdata (request):
   try:
      if (request.POST['tankName'] in DBReader.dataFiles.keys()):
         return HttpResponse(
            DBReader.dataAttributes[request.POST['tankName']],
            content_type='application/json',
         )
      else:
         raise Http404("invalid tankName '{0}'".format(\
            request.POST['tankName'])\
         )
   except:
         raise Http404("tankName not supplied")
