from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def addcourse(request):
    if request.method == "POST":
        errors = Course.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            course = Course.objects.create(name=request.POST['course_name'])
            description = CourseDesc.objects.create(description=request.POST['course_desc'])
            course.description = description
            course.save()
    return redirect('/')

def delete_page(request, id):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id=id)
        }
    return render(request,'delete.html', context)

def delete(request, id):
    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('/')