from django import forms
from django.forms.widgets import *
from datetime import datetime

class GuitarTrainerSetup(forms.Form):
    majorChords = [ ("A","A"),
                    ("B","B"),
                    ("C","C"),
                    ("D","D"),
                    ("E","E"),
                    ("F","F"),
                    ("G","G"),
                  ]

    minorChords = [ ("Am","Am"),
                    ("Bm","Bm"),
                    ("Cm","Cm"),
                    ("Dm","Dm"),
                    ("Em","Em"),
                    ("Fm","Fm"),
                    ("Gm","Gm"),
                  ]

    numberOfChords = forms.IntegerField(label="Number of Chords", max_value=20, min_value=1)
    timeBetweenChords = forms.DecimalField(label="Time between Chords (sec)", min_value=0.5, max_value=20)
    selectedMajorChords = forms.MultipleChoiceField(label="Major Chords", choices=majorChords, required=False)
    selectedMinorChords = forms.MultipleChoiceField(label="Minor Chords", choices=minorChords, required=False)
