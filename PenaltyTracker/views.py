from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def search(request):
    query = request.GET.get('HomeTeam')
    try:
        print(query)
    except ValueError:
        query = None
        results = None
    if query:
        results = Book.objects.get(uid=query)
    context = RequestContext(request)
    return render_to_response('results.html', {"results": results,}, context_instance=context)