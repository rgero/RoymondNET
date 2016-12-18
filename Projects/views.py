from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/index.html',
            {'active': "projects",
             'jumbotron':"Projects"
            }
        )
def language(request,renderDic):
    renderDic['active'] = 'projects'
    return render(request, request.path[1::] + "/index.html", renderDic)

def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def python(request):
    return language(request, {'jumbotron':"Python Projects"})

def python_guitar_notes(request):
    return render(request, 'projects/python/guitar-notes.html', {'active':'projects','jumbotron':"Guitar Notes"})

def java(request):
    return language(request,{'jumbotron':"Java Projects"})

def csharp(request):
    return language(request,{'jumbotron':"C# Projects"})

def csharp_selina(request):
    return render(request, 'projects/c-sharp/selina-no.html', {'active':'projects','jumbotron':"Selina No!"})

def csharp_painbow(request):
    return render(request, 'projects/c-sharp/painbow-road.html', {'active':'projects','jumbotron':"Painbow Road"})

def java_background(request):
    return render(request, 'projects/java/background.html', {'active':'projects','jumbotron':"The Background Generator"})

def java_image_processor(request):
    return render(request, 'projects/java/imageprocessor.html', {'active':'projects','jumbotron':"The Image Processor"})

def perl(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"PERL Projects"})

def android(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"Android Projects"})

def iOS(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"iOS Projects"})
