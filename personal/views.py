from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    return render(request, 'personal/index.html',
         {'active': None}
    
    )
    
def about(request):
    return render(request, 'personal/about.html', 
            {'active': "about",
            }
        )

def comingsoon(request):
    return render(request, 'personal/comingsoon.html', 
            {'active': "None",
            }
        )