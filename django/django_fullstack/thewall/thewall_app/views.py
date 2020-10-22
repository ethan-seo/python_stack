from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

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
            # print(hashed_pw)
            # print("hello")
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            request.session['user_id'] = user.id
            return redirect('/thewall') #the main page of the application
    return redirect(request, '/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.filter(email=request.POST['email'])
            if len(user) > 0:
                user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id'] = user.id
                    return redirect('/groups')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def thewall(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all(),
        'all_comments': Comment.objects.all()
    }
    return render(request, 'thewall.html', context)

def post(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    Message.objects.create(content=request.POST['message'], owner=User.objects.get(id=request.session['user_id']))
    return redirect('/thewall')

def comment(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    owner = User.objects.get(id=request.session['user_id'])
    comment_message = Message.objects.get(id=id)
    print("debug")
    print(comment_message)
    Comment.objects.create(content=request.POST['comment'], owner=owner, a_message=comment_message)
    return redirect('/thewall')

def destroy_message(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        message_with_id = Message.objects.filter(id=id)
        if len(message_with_id) > 0:
            message = message_with_id[0]
            if message.owner.id == request.session['user_id']:
                message.delete()
    return redirect('/thewall')
