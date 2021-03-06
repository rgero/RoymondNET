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
                "VGK":"Vegas Golden Knights",
                "WSH":"Washington Capitals",
                "WPG":"Winnipeg Jets"}
  returnList = []
  for entry in i:
    returnList.append(teamList[entry])
  return returnList

def convertSeasonType(s):
    print(s)
    if s == "Regular_16_17":
        return "2016-17 Regular Season"
    elif s == "Playoffs_16_17":
        return "2016-17 Playoffs"
    elif s == "Regular_17_18":
        return "2017-18 Regular Season"
    elif s == "Playoffs_17_18":
        return "2017-18 Playoffs"
    elif s == "Regular_18_19":
        return "2018-19 Regular Season"
    elif s == "Playoffs_18_19":
        return "2018-19 Playoffs"
    else:
        return "None"

def listToSQLIncludeString(entry):
    ''' Input:
            entry - a list of items that should be joined together for the query

        Used:
            This is used to parse the team names.
    '''
    resultString = "("
    for i in entry:
      if i != "":
        resultString += "'" + i + "', "
    resultString = resultString[0:len(resultString)-2] + ")"
    return resultString




def constructWHERE(entry):
  ''' Inputs:
        Entry  - This is the user entered data from the search form passed as a dictionary
               - NOTE: Player Names, Penalties, and Refs are ALREADY SEPARATED into an array
                       based on the regular expression shown in getList.
      Returns:
        A string used for the query.
  '''
  teamList = ["teamName","opponentTeam"]
  listOfItems = []

  playerEntry = entry["playerName"]
  penaltyEntry = entry["penalty"]

  #Player Name Parsing
  if len(playerEntry) >= 1 and playerEntry[0] != "":
      playerSearchString = "("
      for i in range(0, len(playerEntry)-1):
          playerSearchString += " playerName LIKE '%" + playerEntry[i] + "%' OR "
      playerSearchString += " playerName LIKE '%" + playerEntry[len(playerEntry)-1] + "%')"
      listOfItems.append(playerSearchString)

  #Penalty Parsing
  if len(penaltyEntry) >= 1 and penaltyEntry[0] != "":
      penaltySearchString = "("
      for i in range(0, len(penaltyEntry)-1):
          penaltySearchString += " penalty LIKE '%" + penaltyEntry[i] + "%' OR "
      listOfItems.append(penaltySearchString)

  #Parsing the team names
  for i in teamList:
      if len(entry[i]) >= 1 and entry[i][0]!="":
          listOfItems.append(i + " IN " + listToSQLIncludeString(entry[i]) + " " )

  # Parsing Home vs Away Status
  if entry["homeAway"] == "Home":
      listOfItems.append("homeAway=0")
  elif entry["homeAway"] == "Away":
      listOfItems.append("homeAway=1")

  # Parsing the Game Dates as a "Between" statement.
  if entry["startDate"] != None and entry["endDate"] != None:
      listOfItems.append("gameDate BETWEEN date('" + entry["startDate"].strftime("%Y-%m-%d") + "') AND date('" \
      + (entry["endDate"]).strftime("%Y-%m-%d") + "') ")
  if entry["startDate"] == None and entry["endDate"] != None:
      listOfItems.append("gameDate <= date('" + entry["endDate"].strftime("%Y-%m-%d") + "') ")
  if entry["startDate"] != None and entry["endDate"] == None:
      listOfItems.append("gameDate >= date('" + entry["startDate"].strftime("%Y-%m-%d") + "')")

  # Constructing the Where statement based on everything listed above.
  # All of the search terms must be matched, therefore "AND" is selected. The unique cases where it expands that AND statement
  # are handled above.
  where_string = ""
  for j in range(0, len(listOfItems)-1):
      where_string += listOfItems[j] + " AND "
  if len(listOfItems) >= 1:
    where_string += listOfItems[len(listOfItems)-1]
  return where_string



def performSearch(query):
  ''' This is the function that is going to perform the actual query against the database.
      It is going to utilize the constructWHERE function to figure out what exactly the user is looking for
      OUTPUT: results - the SQL results from the query.
  '''
  dblocation = os.path.join(os.getcwd(), "PenaltyTracker")
  dblocation = os.path.join(dblocation, "static")
  dblocation = os.path.join(dblocation, "penaltytracker")
  dblocation = os.path.join(dblocation, "season.db")

  conn = sqlite3.connect(dblocation)
  cursor = conn.cursor()

  tableName = query["seasonType"]

  executionString = "SELECT * FROM " + tableName
  where_string = constructWHERE(query)
  if where_string!="":
      executionString += " WHERE " + where_string

  executionString += " ORDER BY gameDate"

  print(executionString)

  try:
      results = cursor.execute(executionString).fetchall()
      return results
  except:
    return None
