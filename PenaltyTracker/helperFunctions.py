import re, sqlite3, os, datetime

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

def listToSQLString(entry):
    resultString = "("
    for i in entry:
      if i != "":
        resultString += "'" + i + "',"
    resultString = resultString[0:len(resultString)-1] + ")"
    return resultString


def constructWHERE(entry):
  '''Entry is the search form dictionary'''
  potentialMultiItems = ["playerName","teamName","opponentTeam","penalty","refs"]
  listOfItems = []
  for i in potentialMultiItems:
      if len(entry[i]) >= 1 and entry[i][0]!="":
          listOfItems.append(i + " IN " + listToSQLString(entry[i]))
  if entry["homeAway"] == "Home":
      listOfItems.append("homeAway=0")
  elif entry["homeAway"] == "Away":
      listOfItems.append("homeAway=1")
  if entry["startDate"] != None and entry["endDate"] != None:
      listOfItems.append("gameDate BETWEEN '" + entry["startDate"].strftime("%m/%d/%Y") + "' AND '" \
      + (entry["endDate"]+datetime.timedelta(days=1)).strftime("%m/%d/%Y") + "'")
  if entry["startDate"] == None and entry["endDate"] != None:
      listOfItems.append("gameDate BETWEEN '" + entry["endDate"].strftime("%m/%d/%Y") + "' AND '" \
      + (entry["endDate"]+datetime.timedelta(days=1)).strftime("%m/%d/%Y") + "'")
  if entry["startDate"] != None and entry["endDate"] == None:
      listOfItems.append("gameDate BETWEEN '" + entry["startDate"].strftime("%m/%d/%Y") + "' AND '" \
      + (entry["startDate"]+datetime.timedelta(days=1)).strftime("%m/%d/%Y") + "'")
  where_string = ""
  for j in range(0, len(listOfItems)-1):
      where_string += listOfItems[j] + " AND "
  if len(listOfItems) >= 1:
    where_string += listOfItems[len(listOfItems)-1]
  return where_string



def performSearch(query):
  print(os.getcwd())
  conn = sqlite3.connect(os.path.join(os.getcwd(), "PenaltyTracker\\static\\2015-16.db"))
  cursor = conn.cursor()


  executionString = "SELECT * FROM PenaltyTracker "
  where_string = constructWHERE(query)
  if where_string!="":
      executionString += "WHERE " + where_string

  executionString += " ORDER BY gameDate"

  print executionString

  results = cursor.execute(executionString).fetchall()
  print( len(results) )
  return results
