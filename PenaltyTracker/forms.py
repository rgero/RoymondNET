from django import forms
from datetime import datetime

class PenaltySearchForm(forms.Form):
  teamList = [("ANA","Anaheim Ducks"),
              ("ARI","Arizona Coyotes"),
              ("BOS","Boston Bruins"),
              ("BUF","Buffalo Sabres"),
              ("CGY","Calgary Flames"),
              ("CAR","Carolina Hurricanes"),
              ("CHI","Chicago Blackhawks"),
              ("COL","Colorado Avalanche"),
              ("CBJ","Columbus Blue Jackets"),
              ("DAL","Dallas Stars"),
              ("DET","Detroit Red Wings"),
              ("EDM","Edmonton Oilers"),
              ("FLA","Florida Panthers"),
              ("LAK","Los Angeles Kings"),
              ("MIN","Minnesota Wild"),
              ("MTL","Montreal Canadiens"),
              ("NSH","Nashville Predators"),
              ("NJD","New Jersey Devils"),
              ("NYI","New York Islanders"),
              ("NYR","New York Rangers"),
              ("OTT","Ottawa Senators"),
              ("PHI","Philadelphia Flyers"),
              ("PIT","Pittsburgh Penguins"),
              ("SJS","San Jose Sharks"),
              ("STL","St Louis Blues"),
              ("TBL","Tampa Bay Lightning"),
              ("TOR","Toronto Maple Leafs"),
              ("VAN","Vancouver Canucks"),
              ("WSH","Washington Capitals"),
              ("WPG","Winnipeg Jets")]
  playerName = forms.CharField(label="Player Name", max_length=100, required=False)
  playerTeam = forms.MultipleChoiceField(label="Player's Team", choices=teamList, required=False)
  opponent = forms.MultipleChoiceField(label="Opponent", choices=teamList, required=False)
  homeAway = forms.ChoiceField(label="Home or Away",choices=[("Either","Either"),("Home","Home"),("Away","Away")], required=False)
  penalty = forms.CharField(label="Penalty", max_length=100, required=False)
  startDate = forms.DateField(label="Start Date", required=False, help_text="Format: YYYY-MM-DD")
  endDate = forms.DateField(label="End Date", required=False, help_text="Format: YYYY-MM-DD")
  refs = forms.CharField(label="Referee's Name", max_length=200, required=False)
