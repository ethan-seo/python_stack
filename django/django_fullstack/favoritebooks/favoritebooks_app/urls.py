from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('books/create', views.create_book),
    path('books/<int:id>', views.show_book),
    path('books/favorite/<int:id>', views.favorite_book),
    path('books/unfavorite/<int:id>', views.unfavorite_book),
    path('books/destroy/<int:id>', views.destroy_book),
]