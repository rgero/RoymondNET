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
