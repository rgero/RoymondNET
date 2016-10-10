import re
from django.shortcuts import render
from django.http import HttpResponse

from .forms import PenaltySearchForm

# Create your views here.

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
    homeTeams = getFullNames(cleanedData["homeTeam"])
    awayTeams = getFullNames(cleanedData["awayTeam"])
    homeAway = cleanedData["homeAway"]
    penalty = getList(cleanedData["penalty"])
    startDate = cleanedData["startDate"]
    endDate = cleanedData["endDate"]
    refs = getList(cleanedData["refs"])

    Data = {"playerNames":playerNames,
            "homeTeams": homeTeams,
            "awayTeams": awayTeams,
            "homeAway": homeAway,
            "penalty": penalty,
            "startDate": startDate,
            "endDate": endDate,
            "refs": refs}

    return render(request, 'results.html', Data)

def getList(i):
  values = re.split("\s*,\s*", i)
  values = [str(i) for i in values]
  return values

def getFullNames(i):
  teamList = {  "ANA":"Anaheim Ducks",
                "ARI":"Arizona Coyotes",
                "BOS":"Boston Bruins",
                "BUF":"Buffalo Sabres",
                "CGY":"Calgary Flames",
                "CAR":"Carolina Hurricanes",
                "CHI":"Chicago Blackhawks",
                "COL":"Colorado Avalanche",
                "CBJ":"Columbus Blue Jackets",
                "DAL":"Dallas Stars",
                "DET":"Detroit Red Wings",
                "EDM":"Edmonton Oilers",
                "FLA":"Florida Panthers",
                "LAK":"Los Angeles Kings",
                "MIN":"Minnesota Wild",
                "MTL":"Montreal Canadiens",
                "NSH":"Nashville Predators",
                "NJD":"New Jersey Devils",
                "NYI":"New York Islanders",
                "NYR":"New York Rangers",
                "OTT":"Ottawa Senators",
                "PHI":"Philadelphia Flyers",
                "PIT":"Pittsburgh Penguins",
                "SJS":"San Jose Sharks",
                "STL":"St Louis Blues",
                "TBL":"Tampa Bay Lightning",
                "TOR":"Toronto Maple Leafs",
                "VAN":"Vancouver Canucks",
                "WSH":"Washington Capitals",
                "WPG":"Winnipeg Jets"}
  returnList = []

  for entry in i:
    returnList.append(teamList[entry])
  return returnList
