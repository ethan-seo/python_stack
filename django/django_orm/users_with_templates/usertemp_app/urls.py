from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user)
]