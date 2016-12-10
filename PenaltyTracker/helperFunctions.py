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
        resultString += "'" + i + "', "
    resultString = resultString[0:len(resultString)-2] + ")"
    return resultString




def constructWHERE(entry):
  '''Entry is the search form dictionary'''
  potentialMultiItems = ["teamName","opponentTeam"]
  listOfItems = []

  playerEntry = entry["playerName"]
  refEntry = entry["refs"]
  penaltyEntry = entry["penalty"]

  #Player Name Parsing
  if len(playerEntry) >= 1 and playerEntry[0] != "":
      playerSearchString = "("
      for i in range(0, len(playerEntry)-1):
          playerSearchString += " playerName LIKE '%" + playerEntry[i] + "%' OR "
      playerSearchString += " playerName LIKE '%" + playerEntry[len(playerEntry)-1] + "%')"
      listOfItems.append(playerSearchString)

  #Ref Name Parsing
  if len(refEntry) >= 1 and refEntry[0] != "":
      refSearchString = "("
      for i in range(0, len(refEntry)-1):
          refSearchString += " refs LIKE '%" + refEntry[i] + "%' OR "
      refSearchString += " refs LIKE '%" + refEntry[len(refEntry)-1] + "%')"
      listOfItems.append(refSearchString)

  #Penalty Parsing
  if len(penaltyEntry) >= 1 and penaltyEntry[0] != "":
      penaltySearchString = "("
      for i in range(0, len(penaltyEntry)-1):
          penaltySearchString += " penalty LIKE '%" + penaltyEntry[i] + "%' OR "
      penaltySearchString += " penalty LIKE '%" + penaltyEntry[len(refEntry)-1] + "%')"
      listOfItems.append(penaltySearchString)

  for i in potentialMultiItems:
      if len(entry[i]) >= 1 and entry[i][0]!="":
          listOfItems.append(i + " IN " + listToSQLString(entry[i]) + " " )
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
  print where_string
  return where_string



def performSearch(query):
  print(os.getcwd())
  dblocation = os.path.join(os.getcwd(), "PenaltyTracker")
  dblocation = os.path.join(dblocation, "static")
  dblocation = os.path.join(dblocation, "penaltytracker")
  dblocation = os.path.join(dblocation, "season.db")
  print os.path.isfile(dblocation)

  conn = sqlite3.connect(dblocation)
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
