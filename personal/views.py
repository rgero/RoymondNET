from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

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
