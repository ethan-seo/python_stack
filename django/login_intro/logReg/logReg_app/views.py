from django.shortcuts import render, redirect
from .models import User, Koala
from django.contrib import messages
import bcrypt
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            #create an account for our User
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(hashed_pw)
            print("hello")
            user = User.objects.create(name=request.POST['user_name'], email=request.POST['email'], password=hashed_pw)
            request.session['user_id'] = user.id
            return redirect('/main_page') #the main page of the application
    return redirect(request, '/')


def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/main_page')
    messages.error(request, "Email or password is incorrect")
    return redirect('/')


def main_page(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_koalas': Koala.objects.all()
    }
    return render(request, 'main_page.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def create_koala(request):
    if request.method == "POST":
        errors = Koala.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            # return redirect('/main_page')
        else:
            koala = Koala.objects.create(name=request.POST['koala_name'], talent=request.POST['talent'], user=User.objects.get(id=request.session['user_id']))
        # return redirect('/main_page')
    return redirect('/main_page')

def profile(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "profile.html", context)

def show_koalas(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    koala_with_id = Koala.objects.filter(id=id)
    if len(koala_with_id) > 0:
        context = {
            'koala': Koala.objects.get(id=id)
        }
        return render(request, 'one_koala.html', context)
    else:
        messages.error(request, "Koala not found.")
        return redirect('/user')

def destroy_koala(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        koala_with_id = Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = koala_with_id[0]
            if koala.user.id == request.session['user_id']:
                koala.delete()
    return redirect('/main_page')

def voting_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        #Sort Koalas by # of votes
        "all_koalas": Koala.objects.annotate(votes=Count('users_votes')).order_by('-votes'),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'voting_page.html', context)

def vote_koala(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        koala_with_id = Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = koala_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            koala.users_votes.add(user)
    # user.voted_koalas.add(koala)
    return redirect('/voting')

def unvote_koala(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        koala_with_id = Koala.objects.filter(id=id)
        if len(koala_with_id) > 0:
            koala = koala_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            koala.users_votes.remove(user)
            # user.voted_koalas.remove(koala)
    return redirect('/voting')