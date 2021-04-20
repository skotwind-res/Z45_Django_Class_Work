from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

from .models import Bb

def index(request):
  bbs = Bb.objects.all()
  return render(request, 'bboard/index.html', {'bbs': bbs})

def cur_time(request):
    return HttpResponse(f"Current time: {datetime.now().hour}:{datetime.now().minute}")




