from django.http import (HttpResponse, HttpResponseRedirect, )
from django.shortcuts import (render, get_object_or_404, redirect,)
from django.urls import reverse

# from .models import ()
# This imports required models.

# Create your views here.

def index (request, error=None):
   # All views must have request parameter as 1st by default.
   # This serves multiple purposes.
   return render(
      request,
      '<app_name>/<html template>', # app/template/app/*
      {
         'key1':value1,
         'key2':value2,
      }, # passing variables to template in key:value format.
   )

def othertype (request):
   model1 = Model1(parameter1='somevalue') # creating instance.
   model2 = Model1(parameter1='somevalue') # creating instance.
   model1.save()
   model2.save() # saving details / instance in database.
   
   model3 = Model2(param1=model1, param2='someval')
   model3.save()
   # Adding model1 to many2manyfield in Model2.
   # This is a many to many relation, and hence, requires both models to be
   # saved before linking each other.
   model3.many2manyfield.add(model1)
   # Same is done to many to one relation fields as well.
   # These are defined in models.py.
   model3.many2onefield.add(model2)
   return redirect('<namespace>:<view>', 'passing parameter to respective view')

def otherview1 (request):
   try:
      modelslist = Model2.objects.all()
   except Model2.DoesNotExist:
      return redirect('<namespace>:<view>', 'parameter passing')
   return render(request, 'template', \
      {'key': value, 'key2':request.POST['key'] # Extracting post form data.
      })
