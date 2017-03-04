from django.shortcuts import render
from .forms import GuitarTrainerSetup

# Create your views here.
def index(request):

    if request.method == 'POST':
        formData = GuitarTrainerSetup(request.POST)
        if formData.is_valid():
            cleanedData = formData.cleaned_data
            numberOfChords = cleanedData["numberOfChords"]
            timeBetween = float(cleanedData["timeBetweenChords"])
            selectedChords = []
            if cleanedData["selectedMajorChords"]:
                selectedChords += cleanedData["selectedMajorChords"]
            if cleanedData["selectedMinorChords"]:
                selectedChords += cleanedData["selectedMinorChords"]

            gameData = {
                "numberOfChords" : numberOfChords,
                "timeBetween" : timeBetween,
                "selectedChords" : selectedChords
            }

            return render(request, 'guitartrainer/trainer.html', {"gameData":gameData})
    else:
        formData = GuitarTrainerSetup()
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'None',
        'form': formData
    }
    return render(request, 'guitartrainer/index.html', renderDic)
