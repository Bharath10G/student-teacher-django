
from django.http import HttpResponse
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student


def index(request):
    return HttpResponse("these is student app")

def student_all_record(request):
    obj = Student.objects.all()
    return render(request, 'studentall.html', {'students': obj})
def student_form(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        age1 = request.POST.get('age')
        gender1 = request.POST.get('gender')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        course1 = request.POST.get('course')
        address1 = request.POST.get('address')

        Student.objects.create(
            name=name1,
            age=age1,
            gender=gender1,
            email=email1,
            phone=phone1,
            course=course1,
            address=address1
        )

        messages.info(request, 'Student record inserted successfully')
        return redirect('student_all')

    return render(request, 'student_form.html')


def student_delete(request, s_id):
    obj = Student.objects.get(s_id=s_id)
    obj.delete()
    return redirect('student_all')


def student_update(request, s_id):
    obj = Student.objects.get(s_id=s_id)

    if request.method == "POST":
        obj.name = request.POST.get('name')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.course = request.POST.get('course')
        obj.address = request.POST.get('address')

        obj.save()

        messages.info(request, 'Student record updated successfully')
        return redirect('student_all')

    return render(request, 'student_update.html', {'obj': obj}) 
