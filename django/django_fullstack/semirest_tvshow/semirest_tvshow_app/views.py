from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    return redirect('/shows')

def allshows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'allshows.html', context)

def new(request):
    return render(request, 'newshow.html')

def create(request):
    if request.method == "POST":
        print(request.POST)
        new_tvshow = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        print(new_tvshow.title)
    return redirect('/shows/'+str(new_tvshow.id))

def show(request, id):
    context = {
        "tv_show": Show.objects.get(id=id)
    }
    return render(request, 'tv_show.html', context)

def edit(request, id):
    context = {
        "tv_show": Show.objects.get(id=id)
    }
    return render(request, 'tv_show_edit.html', context)

def update(request, id):
    if request.method == "POST":
        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
    return redirect('/shows/'+str(id))

def destroy(request, id):
    if request.method == "POST":
        show_to_delete = Show.objects.get(id=id)
        show_to_delete.delete()
    return redirect('/shows')

