from django.shortcuts import render
from django.http import HttpResponse
def food(request):
    return HttpResponse('tasty and healthy food is available here')

# Create your views here.
