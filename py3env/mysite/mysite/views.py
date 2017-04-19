
from django.http import HttpResponseRedirect, HttpResponse

def homepage(request):
    return HttpResponseRedirect("/IT/")
