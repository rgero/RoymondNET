from django import forms
from django.forms.widgets import *
from datetime import datetime

YEAR_CHOICES = ('2016', '2017', '2018', '2019')

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
              ("VGK","Vegas Golden Knights"),
              ("WSH","Washington Capitals"),
              ("WPG","Winnipeg Jets")]
  playerName = forms.CharField(label="Player Name", max_length=100, required=False)
  playerTeam = forms.MultipleChoiceField(label="Player's Team", choices=teamList, required=False)
  opponent = forms.MultipleChoiceField(label="Opponent", choices=teamList, required=False)
  homeAway = forms.ChoiceField(label="Home or Away",choices=[("Either","Either"),("Home","Home"),("Away","Away")], required=False)
  penalty = forms.CharField(label="Penalty", max_length=100, required=False)
  startDate = forms.DateField(label="Start Date", required=False, widget=forms.SelectDateWidget(years=YEAR_CHOICES))
  endDate = forms.DateField(label="End Date", required=False, widget=forms.SelectDateWidget(years=YEAR_CHOICES))
  database = forms.ChoiceField( label="Which season?",
                                choices=[ ("Regular_16_17","2016-17 Regular"),
                                          ("Playoffs_16_17","2016-17 Playoffs"), 
                                          ("Regular_17_18","2017-18 Regular"), 
                                          ("Playoffs_17_18","2017-18 Playoffs"),
                                          ("Regular_18_19","2018-19 Regular"),
                                          ("Playoffs_18_19","2018-19 Playoffs")],
                                required=True)
