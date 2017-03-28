from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    renderDic = {
        'jumbotron': "Projects",
        'pageTitle': 'Projects - Roymond.net'
      }
    return render(request, 'template.html', renderDic)
