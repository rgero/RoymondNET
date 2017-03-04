from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

# Create your views here.

def readJSON(file):
    data = open(file, 'r')
    data = json.load(data)
    return data

def projects(request):
    dataFile = 'Projects/static/projects/index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def language(request,renderDic):
    return render(request, request.path[1::] + "/index.html", renderDic)

def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def python(request):
    dataFile = 'Projects/static/projects/python/index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def python_guitar_notes(request):
    renderDic = {
        'pageTitle':"Guitar Notes - Roymond.NET",
        'jumbotron':"Guitar Notes",
        'active':'projects'
    }
    return render(request, 'projects/python/guitar-notes.html', renderDic)

def java(request):
    dataFile = 'Projects/static/projects/java/index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def csharp(request):
    dataFile = 'Projects/static/projects/c-sharp/c-sharp-index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def csharp_selina(request):
    dataFile = 'Projects/static/projects/c-sharp/selina.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def csharp_painbow(request):
    renderDic = {
        'pageTitle':"Painbow Road - Roymond.NET",
        'jumbotron':"Painbow Road",
        'active':'projects'
    }
    return render(request, 'projects/c-sharp/painbow-road.html', renderDic)

def java_background_old(request):
    dataFile = 'Projects/static/projects/java/background_old/background.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def java_image_processor(request):
    dataFile = r'Projects/static/projects/java/imageprocessor/imageprocessor.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def java_guitar_trainer(request):
    dataFile = 'Projects/static/projects/java/guitartrainer/guitartrainer.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def java_chord_drawer(request):
    renderDic = {
        'pageTitle':"The Chord Drawer - Roymond.NET",
        'jumbotron':"The Chord Drawer",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def java_background(request):
    renderDic = {
        'pageTitle':"The Background Generator - Roymond.NET",
        'jumbotron':"The Background Generator",
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
        'pageTitle':"Android Projects - Roymond.NET",
        'jumbotron':"Android Projects",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def iOS(request):
    renderDic = {
        'pageTitle':"iOS Projects - Roymond.NET",
        'jumbotron':"iOS Projects",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def example_json(request):
    dataFile = 'Projects/static/exampleJSON.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)
