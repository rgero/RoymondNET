from django.shortcuts import render
from .forms import GuitarTrainerSetup

# Create your views here.
def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def index(request):
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'None',
        'Header':'Coming Soon!',
        'explanation':'This section is being actively developed. Please check back soon.'
    }
    return comingsoon(request, renderDic)

def index2(request):

    if request.method == 'POST':
        formData = GuitarTrainerSetup(request.POST)
        if formData.is_valid():
            cleanedData = formData.cleaned_data
            print(cleanedData)
    else:
        formData = GuitarTrainerSetup()
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'None',
        'form': formData
    }
    return render(request, 'guitartrainer/index.html', renderDic)
