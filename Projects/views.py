from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/index.html',
            {'active': "projects",
            }
        )

def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def python(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Python Projects Coming Soon!'})

def csharp(request):
    return comingsoon(request, {'active': 'projects', 'Header':'C# Projects Coming Soon!'})
    
def java(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Java Projects Coming Soon!'})
    
def perl(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Perl Projects Coming Soon!'})
    
def android(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Android Projects Coming Soon!'})
    
def iOS(request):
    return comingsoon(request, {'active': 'projects', 'Header':'iOS Projects Coming Soon!'})