from .models import *
from django.shortcuts import render

def data_context(request):
    context = {}
    context['recent'] = Posts.objects.all().order_by('-id')[:3]
    context['categories']=Category.objects.all().order_by('-id')
    context['tags']=Tag.objects.all().order_by('-id')
    return  context