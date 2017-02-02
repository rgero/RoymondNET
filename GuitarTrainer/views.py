from django.shortcuts import render

# Create your views here.
def comingsoon(request, input_dic):
    return render(request, 'comingsoon.html', input_dic)

def index(request):
    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'None',
        'Header':'Coming Soon!',
        'explanation':'This section is being actively developed. Please check back soon.'
    }
    return comingsoon(request, renderDic)

def index2(request):

    chordList = []
    chordList.append( ["A", "guitartrainer\chords\A.png"] )
    chordList.append( ["B", "guitartrainer\chords\B.png"] )
    chordList.append( ["C", "guitartrainer\chords\C.png"] )
    chordList.append( ["D", "guitartrainer\chords\D.png"] )
    chordList.append( ["E", "guitartrainer\chords\E.png"] )
    chordList.append( ["F", "guitartrainer\chords\F.png"] )
    chordList.append( ["G", "guitartrainer\chords\G.png"] )




    renderDic = {
        'pageTitle':"The Guitar Trainer - Roymond.NET",
        'jumbotron':"The Guitar Trainer",
        'active':'None',
        'chordList':chordList
    }
    return render(request, 'guitartrainer/index.html', renderDic)
