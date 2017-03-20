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

            cleanChords = " ".join(selectedChords)

            gameData = {
                "numberOfChords" : numberOfChords,
                "timeBetween" : timeBetween,
                "selectedChords" : cleanChords
            }
            renderDic = {
                'pageTitle':"The Guitar Trainer - Roymond.NET",
                'jumbotron':"The Guitar Trainer",
                'active':'None',
                'gameData': gameData
            }
            return render(request, 'guitartrainer/trainer.html', renderDic)
    else:
        formData = GuitarTrainerSetup()
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'guitartrainer',
        'form': formData
    }
    return render(request, 'guitartrainer/index.html', renderDic)
