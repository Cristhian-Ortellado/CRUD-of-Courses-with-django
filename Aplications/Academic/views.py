from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages
# Create your views here.


def home(request):
    course = Course.objects.all()

    return render(request, "courseManage.html", {"courses": course})


def storeCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['txtCredits']

    course = Course.objects.create(code=code, name=name, credits=credits)
    messages.success(request,'Course Created!')
    return redirect('/')

def updateCourse(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['txtCredits']
    
    # get current course
    course = Course.objects.get(code=code)

    # update fields and save
    course.name = name
    course.credits = credits
    course.save()

    messages.success(request,'Course Updated!')
    return redirect('/')

def deleteCourse(request, code):
    course = Course.objects.get(code = code)
    course.delete()
    messages.success(request,'Course Deleted!')
    return redirect('/')

def editCourse(request, code):
    course = Course.objects.get(code = code)
    return  render(request,"edit-course.html",{'course':course})