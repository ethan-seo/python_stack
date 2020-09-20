from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def submission(request):
    request.session['user_name'] = request.POST['user_name']
    request.session['dojolocation'] = request.POST['dojolocation'],
    request.session['selectlang'] = request.POST['selectlang'],
    request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
    return render(request, 'submission.html')
