from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('courses/addcourse', views.addcourse),
    path('courses/delete/<int:id>', views.delete),
    path('courses/delete_page/<int:id>', views.delete_page),
]