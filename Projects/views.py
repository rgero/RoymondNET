from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

# Create your views here.

def readJSON(file):
    data = open(file, 'r')
    data = json.load(data)
    return data



def projects(request):
    renderDic = {
        'active': "projects",
        'jumbotron':"Projects",
        'pageTitle': 'Projects - Roymond.net',
    }
    return render(request, 'projects/index.html', renderDic)

def language(request,renderDic):
    return render(request, request.path[1::] + "/index.html", renderDic)

def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def python(request):
    renderDic = {
        'pageTitle':"Python Projects - Roymond.NET",
        'jumbotron':"Python Projects",
        'active':'projects'
    }
    return language(request, renderDic )

def python_guitar_notes(request):
    renderDic = {
        'pageTitle':"Guitar Notes - Roymond.NET",
        'jumbotron':"Guitar Notes",
        'active':'projects'
    }
    return render(request, 'projects/python/guitar-notes.html', renderDic)

def java(request):
    renderDic = {
        'pageTitle':"Java Projects - Roymond.NET",
        'jumbotron':"Java Projects",
        'active':'projects'
    }
    return language(request,renderDic)

def csharp(request):
    renderDic = {
        'pageTitle':"C# Projects - Roymond.NET",
        'jumbotron':"C# Projects",
        'active':'projects'
    }
    return language(request, renderDic)

def csharp_selina(request):
    renderDic = {
        'pageTitle':"Selina No! - Roymond.NET",
        'jumbotron':"Selina No!",
        'active':'projects'
    }
    return render(request, 'projects/c-sharp/selina-no.html', renderDic)

def csharp_painbow(request):
    renderDic = {
        'pageTitle':"Painbow Road - Roymond.NET",
        'jumbotron':"Painbow Road",
        'active':'projects'
    }
    return render(request, 'projects/c-sharp/painbow-road.html', renderDic)

def java_background(request):

    dataFile = 'Projects/static/projects/java/background/pageData.json'
    pageData = readJSON(dataFile)

    renderDic = {
        'pageTitle':"The Background Generator - Roymond.NET",
        'jumbotron':"The Background Generator",
        'active':'projects'
    }
    renderDic.update(pageData)
    return render(request, 'projects/projectTemp.html', renderDic)

def java_image_processor(request):
    renderDic = {
        'pageTitle':"The Bad Image Processor - Roymond.NET",
        'jumbotron':"The Bad Image Processor",
        'active':'projects'
    }
    return render(request, 'projects/java/imageprocessor.html', renderDic)

def java_guitar_trainer(request):
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'projects'
    }
    return render(request, 'projects/java/guitar-trainer.html', renderDic)

def java_chord_drawer(request):
    renderDic = {
        'pageTitle':"The Chord Drawer - Roymond.NET",
        'jumbotron':"The Chord Drawer",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def java_background_2017(request):
    renderDic = {
        'pageTitle':"The 2017 Background Generator - Roymond.NET",
        'jumbotron':"The 2017 Background Generator",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def perl(request):
    renderDic = {
        'pageTitle':"PERL Projects - Roymond.NET",
        'jumbotron':"PERL Projects",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def android(request):
    renderDic = {
        'pageTitle':"PERL Projects - Roymond.NET",
        'jumbotron':"PERL Projects",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def iOS(request):
    renderDic = {
        'pageTitle':"PERL Projects - Roymond.NET",
        'jumbotron':"PERL Projects",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)
