from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

# Create your views here.

def readJSON(file):
    data = open(file, 'r')
    data = json.load(data)
    return data

def readFile(filePath):
    data = open(filePath, 'r')
    data = data.read()
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

# The Python Projects
def python(request):
    dataFile = 'Projects/static/projects/python/index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def python_test(request):
    dataFile = 'Projects/static/projects/python/Python_Index.md'
    content = readFile(dataFile)
    renderDic = {
      "pageTitle" : "Python Projects - Roymond.NET",
      "jumbotron" : "Python Projects",
      "active" : "projects",
      "pageContent": content
    }
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp2.html', renderDic)

def python_guitar_notes(request):
    dataFile = 'Projects/static/projects/python/guitar-notes/guitar-notes.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def roymond_net(request):
    renderDic = {
        'pageTitle':"The History of Roymond.NET - Roymond.NET",
        'jumbotron':"The History of this Site",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def python_ip_notifier(request):
    renderDic = {
        'pageTitle':"The IP Notifier - Roymond.NET",
        'jumbotron':"The IP Notifier",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def python_last_to_spotify(request):
    renderDic = {
        'pageTitle':"Last.FM to Spotify - Roymond.NET",
        'jumbotron':"Last.FM to Spotify",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)


#The list of C-Sharp projects
def csharp(request):
    dataFile = 'Projects/static/projects/c-sharp/c-sharp-index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def csharp_selina(request):
    dataFile = 'Projects/static/projects/c-sharp/selina_no.md'
    content = readFile(dataFile)
    renderDic = {
    	"pageTitle" : "Selina No! - Roymond.NET",
    	"jumbotron" : "Selina No!",
    	"active" : "projects",
    	"quickfacts": {
    		"GitHub": ["external", "https://github.com/rgero/SelinaNo"]
    	},
    	"pageContent": content
    }
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp2.html', renderDic)

def csharp_painbow(request):
    renderDic = {
        'pageTitle':"Painbow Road - Roymond.NET",
        'jumbotron':"Painbow Road",
        'active':'projects'
    }
    return render(request, 'projects/c-sharp/painbow-road.html', renderDic)

def csharp_file_renamer(request):
    dataFile = 'Projects/static/projects/c-sharp/file-renamer/file-renamer.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

def csharp_laser_defender(request):
    renderDic = {
        'pageTitle':"Laser Defender - Roymond.NET",
        'jumbotron':"Laser Defender",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)


# The Java projects
def java(request):
    dataFile = 'Projects/static/projects/java/index.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)

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

def perl_size_comparsion(request):
    renderDic = {
        'pageTitle':"Size Comparison - Roymond.NET",
        'jumbotron':"Size Comparsion",
        'active':'projects',
        'Header': 'Coming soon!'
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

def shooting_time(request):
    renderDic = {
        'pageTitle':"Shooting Time - Roymond.NET",
        'jumbotron':"Shooting Time",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def hikers_watch(request):
    renderDic = {
        'pageTitle':"Hiker's Watch - Roymond.NET",
        'jumbotron':"Hiker's Watch",
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

def ios_guitar_trainer(request):
    renderDic = {
        'pageTitle':"Guitar Trainer - Roymond.NET",
        'jumbotron':"Guitar Trainer",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)


#Javascript
def js(request):
    renderDic = {
        'pageTitle':"Javascript - Roymond.NET",
        'jumbotron':"Javascript",
        'active':'projects',
        'Header': 'Coming soon!'
    }
    return comingsoon(request, renderDic)

def js_guitar_trainer(request):
    renderDic = {
        'pageTitle':"Guitar Trainer - Roymond.NET",
        'jumbotron':"Guitar Trainer",
        'Header': "Coming Soon!",
        'active':'projects'
    }
    return comingsoon(request, renderDic)

def example_json(request):
    dataFile = 'Projects/static/exampleJSON.json'
    renderDic = readJSON(dataFile)
    renderDic['static'] = static(".")
    return render(request, 'projects/projectTemp.html', renderDic)
