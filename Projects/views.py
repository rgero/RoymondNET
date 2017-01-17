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
    return language(request, {'pageTitle':"Python Projects - Roymond.NET", 'jumbotron':"Python Projects", 'active':'projects'})

def python_guitar_notes(request):
    return render(request, 'projects/python/guitar-notes.html', {'active':'projects','jumbotron':"Guitar Notes", "pageTitle":"Guitar Notes - Roymond.net"})

def java(request):
    return language(request,{'pageTitle':"Java Projects - Roymond.NET", 'jumbotron':"Java Projects", 'active':'projects'})

def csharp(request):
    return language(request,{'pageTitle':"C# Projects - Roymond.NET", 'jumbotron':"C# Projects"})

def csharp_selina(request):
    return render(request, 'projects/c-sharp/selina-no.html', {'active':'projects','jumbotron':"Selina No!", "pageTitle":"Selina No! - Roymond.net"})

def csharp_painbow(request):
    return render(request, 'projects/c-sharp/painbow-road.html', {'active':'projects','jumbotron':"Painbow Road", "pageTitle":"Painbow Road - Roymond.net"})

def java_background(request):
    return render(request, 'projects/java/background.html', {'active':'projects','jumbotron':"The Background Generator", "pageTitle":"The Background Generator - Roymond.net"})

def java_image_processor(request):
    return render(request, 'projects/java/imageprocessor.html', {'active':'projects','jumbotron':"The Image Processor", "pageTitle":"The Image Processor- Roymond.net"})

def java_guitar_trainer(request):
    return render(request, 'projects/java/guitar-trainer.html', {'active':'projects','jumbotron':"The Guitar Trainer", "pageTitle":"The Guitar Trainer - Roymond.net"})

def perl(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"PERL Projects", "pageTitle":"PERL Projects - Roymond.net"})

def android(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"Android Projects", "pageTitle":"Android Projects - Roymond.net"})

def iOS(request):
    return comingsoon(request, {'active': 'projects', 'Header':'Coming Soon!','jumbotron':"iOS Projects", "pageTitle":"iOS Projects- Roymond.net"})
