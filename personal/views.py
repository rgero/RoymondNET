from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime, math

# Create your views here.

def index(request):
    renderDic = {
        'active': None
      }
    return render(request, 'personal/index.html', renderDic)

def about(request):
    renderDic = {
        'active': "about",
        'jumbotron': "About Me",
        'pageTitle': 'About Me - Roymond.net'
      }
    return render(request, 'personal/about.html', renderDic)

def timeLeft(request):
    today = datetime.date.today()
    august = datetime.date(2018,8,1)
    diff = int(math.fabs((august - today).days))
    weeks = int(math.floor(math.fabs((august - today).days) / 7))
    print(weeks)
    renderDic = {
        'active': None,
        'jumbotron': str(diff) + " days",
        'pageTitle': 'Time Left - Roymond.net',
        'weeksLeft': str(weeks)
      }
    return render(request, 'personal/timeLeft.html', renderDic)
