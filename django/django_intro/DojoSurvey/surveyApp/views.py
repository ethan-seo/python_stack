from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def submission(request):
    context = {
        "user_name" : request.POST['user_name'],
        "dojolocation" : request.POST['dojolocation'],
        "selectlang" : request.POST['selectlang'],
        "comment" : request.POST['comment']
    }
    return render(request, "submission.html", context)