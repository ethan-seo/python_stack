from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        print("debug1")
        errors = User.objects.create_validator(request.POST)
        print("debug2")
        if len(errors) > 0:
            print("debug3")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            #create an account for our User
            print("debug4")
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            # print(hashed_pw)
            # print("hello")
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            request.session['user_id'] = user.id
            print("debug5")
            return redirect('/success') #the main page of the application

    print("debug6")
    return redirect(request, '/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if len(user) > 0:
            user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/success')
    messages.error(request, "Email or password is incorrect")
    return redirect('/')


def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    print('s-debug2')
    print(context['user'])
    return render(request, 'welcome.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')