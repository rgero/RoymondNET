import re

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
