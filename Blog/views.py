from django.shortcuts import render

# Create your views here.
def blogIndex(request):
    return comingsoon(request)        
        
def comingsoon(request):
    return render(request, 'comingsoon.html',
            { 'active': "blog",
              'Header': "Blog Coming Soon!"
            }
        )

