from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def index(request):
    return HttpResponse(f"Здесь будет выведен список объявлений.")

def cur_time(request):
    return HttpResponse(f"Current time: {datetime.now().hour}:{datetime.now().minute}")

