from django.shortcuts import render, redirect
from .models import User, Book
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
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
            request.session['user_id'] = user.id
            return redirect('/books') #the main page of the application
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
                    return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')


def books(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def create_book(request):
    if request.method == "POST":
        errors = Book.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            book = Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=User.objects.get(id=request.session['user_id']))
            user = User.objects.get(id=request.session['user_id'])
            book.users_who_like.add(user)
    return redirect('/books')

def show_book(request, id):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    book_with_id = Book.objects.filter(id=id)
    if len(book_with_id) > 0:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'book_uploader': Book.objects.first().uploaded_by,
            'book_likers': Book.objects.first().users_who_like.all(),
            'book': Book.objects.get(id=id)
        }
        return render(request, 'book_details.html', context)
    else:
        messages.error(request, "Book not found.")
        return redirect('/books')

def favorite_book(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    book_with_id = Book.objects.filter(id=id)
    if len(book_with_id) > 0:
        book = book_with_id[0]
        user = User.objects.get(id=request.session['user_id'])
        book.users_who_like.add(user)
        return redirect(f'/books/{book.id}')
    return redirect('/books')

def unfavorite_book(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    print('unfavorite')
    book_with_id = Book.objects.filter(id=id)
    if len(book_with_id) > 0:
        book = book_with_id[0]
        user = User.objects.get(id=request.session['user_id'])
        book.users_who_like.remove(user)
        return redirect(f'/books/{book.id}')
    return redirect('/books')

def destroy_book(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        book_with_id = Book.objects.filter(id=id)
        if len(book_with_id) > 0:
            book = book_with_id[0]
            if book.creator.id == request.session['user_id']:
                book.delete()
    return redirect('/books')
