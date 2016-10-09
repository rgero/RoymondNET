from django.shortcuts import render
from django.http import HttpResponse

from .forms import PenaltySearchForm

# Create your views here.

def form_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/print_results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PenaltySearchForm()

    return render(request, 'search.html', {'form': form})  
    
def print_results(request):
  if request.method != 'POST':
    raise Http404

  myForm = PenaltySearchForm(request.POST)

  if myForm.is_valid():
    return render(request, 'results.html', {'results': myForm.cleaned_data})