from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Members(request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render())