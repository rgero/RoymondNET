from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from .models import *

def index(request):
    renderDic = {
        'jumbotron': "Projects",
        'pageTitle': 'Projects - Roymond.net',
        'active' : 'projects'
      }
    renderDic["projects"] = []
    listOfPages = ProjectPage.objects.order_by("pageTitle")
    for i in Language.objects.order_by("language"):
        languageName = i.language
        languageSlug = i.slug
        languageList = []
        languageList[:] = []
        for j in listOfPages:
            if languageName.lower() == j.language.language.lower():
               languageList.append(j)
        renderDic["projects"].append( [languageName, languageList, languageSlug])
    return render(request, 'projects/project_index.html', renderDic)

def languageHistory(request, languageSlug):
    languagePage = Language.objects.filter(slug__iexact=languageSlug)
    if languagePage:
        languagePage = languagePage.get(slug__iexact=languageSlug)
        language = languagePage.language
        renderDic = {
            'jumbotron': language + " Projects",
            'pageTitle': language + " Projects - Roymond.net",
            'language' : language,
            'languageSlug' : languagePage.slug
          }
        renderDic['content'] = languagePage.content

        # Now to find the projects.
        listOfPages = ProjectPage.objects.order_by("pageTitle")
        listOfProjects = []
        for i in listOfPages:
            if language.lower() == i.language.language.lower():
               listOfProjects.append(i)
        renderDic['projects'] = listOfProjects
        return render(request, 'projects/languageTemp.html', renderDic)
    else:
        return render(request, '404.html', {'jumbotron': 'Error 404'})

def projectPage(request, languageSlug, slug):
    projectPages = ProjectPage.objects.filter(slug__iexact=slug)
    if projectPages:
        projectPage = projectPages.get(slug__iexact=slug)
        renderDic = {
            'jumbotron': projectPage.pageTitle,
            'pageTitle': projectPage.pageTitle + " - Roymond.net",
            'slug': projectPage.slug,
            'languageSlug' : projectPage.language.slug,
            'language' : projectPage.language.language,
            'content': projectPage.content,
            'related_projects' : projectPage.related_projects.all(),
            'quick_facts' : projectPage.quick_facts,
            'external_media' : projectPage.external_media,
            'active' : 'projects'
          }

        # Processing image List
        if projectPage.images != "":
            imageList = projectPage.images.split("\r\n")
            renderDic['images'] = imageList
        return render(request, 'projects/projectTemp.html', renderDic)
    else:
        return render(request, '404.html', {'jumbotron': 'Error 404'})
