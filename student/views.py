from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
# Create your views here.

def student(request):
    students = Student.objects.all()

    response = render(request,"student/student_list.html",{
        'students':students
    })
    return response

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/student/")

    else:
        form = StudentForm()

    responce = render(request,"student/student_form.html", {'form':form})
    return responce

def edit_student(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/student/")
    else:
        form = StudentForm(instance=student)

    responce = render(request,"student/student_edit.html",{'form':form})
    return responce

def del_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.delete()
        return redirect("/student/")
    responce = render(request,"student/student_delete.html", {'student':student})
    return responce
