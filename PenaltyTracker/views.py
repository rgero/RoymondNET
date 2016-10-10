from django.shortcuts import render
from django.http import HttpResponse

from .forms import PenaltySearchForm
from .helperFunctions import *

import datetime

def form_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/print_results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PenaltySearchForm()

    return render(request, 'search.html', {'form': form})

def print_results(request):
  if request.method != 'POST':
    raise Http404

  submittedForm = PenaltySearchForm(request.POST)

  if submittedForm.is_valid():
    #Get the raw data
    cleanedData = submittedForm.cleaned_data
    playerNames = getList(cleanedData["playerName"])
    playerTeam = getFullNames(cleanedData["playerTeam"])
    opponent = getFullNames(cleanedData["opponent"])
    homeAway = cleanedData["homeAway"]
    penalty = getList(cleanedData["penalty"])
    startDate = cleanedData["startDate"]
    endDate = cleanedData["endDate"]
    refs = getList(cleanedData["refs"])

    Data = {"playerName":playerNames,
            "teamName": playerTeam,
            "opponentTeam": opponent,
            "homeAway": homeAway,
            "penalty": penalty,
            "startDate": startDate,
            "endDate": endDate,
            "refs": refs}

    queryResults = performSearch(Data)

    return render(request, 'results.html', {"data":queryResults, "time":datetime.date.today()})
