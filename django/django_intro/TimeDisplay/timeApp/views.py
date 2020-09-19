from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    # Oct 26, 2013 11:26 AM
    context = {
        "time1": strftime("%b %d, %Y", gmtime()),
        "time2": strftime("%I:%M %p", gmtime())
    }
    return render(request,'index.html', context)
    # return HttpResponse("test1")