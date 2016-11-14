from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/index.html',
            {'active': "projects",
            }
        )
def language(request):
    print request
    return render(request, request.path[1::] + "/index.html", {'active':'projects'})

def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def python(request):
    return language(request)

    
def java(request):
    return language(request)
    
def csharp(request):
    return language(request)

def java_background(request):
    return render(request, 'projects/java/background.html', {'active':'projects'})
    
def java_image_processor(request):
    return render(request, 'projects/java/imageprocessor.html', {'active':'projects'})
    
def perl(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Perl Projects Coming Soon!'})
    
def android(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Android Projects Coming Soon!'})
    
def iOS(request):
    return comingsoon(request, {'active': 'projects', 'Header':'iOS Projects Coming Soon!'})