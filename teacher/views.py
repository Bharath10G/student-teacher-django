from django.http import HttpResponse
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher

def index(request):
    return HttpResponse("these is teacher app")

def teacher_all_record(request):
    obj = Teacher.objects.all()
    return render(request, 'teacherall.html', {'teachers': obj})


def teacher_form(request):
    if request.method == "POST":

        name1 = request.POST.get('name')
        subject1 = request.POST.get('subject')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        qualification1 = request.POST.get('qualification')
        experience1 = request.POST.get('experience')

        Teacher.objects.create(
            name=name1,
            subject=subject1,
            email=email1,
            phone=phone1,
            qualification=qualification1,
            experience=experience1
        )

        messages.info(request, 'Teacher record inserted successfully')
        return redirect('teacher_all')

    return render(request, 'teacher_form.html')


def teacher_delete(request, t_id):
    obj = Teacher.objects.get(t_id=t_id)
    obj.delete()
    return redirect('teacher_all')


def teacher_update(request, t_id):
    obj = Teacher.objects.get(t_id=t_id)

    if request.method == "POST":

        obj.name = request.POST.get('name')
        obj.subject = request.POST.get('subject')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.qualification = request.POST.get('qualification')
        obj.experience = request.POST.get('experience')

        obj.save()

        messages.info(request, 'Teacher record updated successfully')
        return redirect('teacher_all')

    return render(request, 'teacher_update.html', {'obj': obj})
