from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import PenaltySearchForm
from .helperFunctions import *

import datetime

def form_test(request):
    # if this is a POST request we need to process the form data
    print request
    if request.method == 'POST':
        formData = PenaltySearchForm(request.POST)

        if formData.is_valid():
          #Get the raw data
          cleanedData = formData.cleaned_data
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

          cleanedData["playerTeam"] = ", ".join( playerTeam )
          cleanedData["opponent"] = ", ".join( opponent )

          queryResults = performSearch(Data)

          return render(request, 'results.html', {"data":queryResults, "time":datetime.date.today(), "inputData":cleanedData})

    # if a GET (or any other method) we'll create a blank form
    else:
        formData = PenaltySearchForm()
    return render(request, 'search.html', { 'active': "penaltytracker",
                                            'form': formData,
                                            'jumbotron':"The Penalty Tracker"})
