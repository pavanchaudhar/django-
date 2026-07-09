from django.shortcuts import render, redirect
from .models import Student, department, Course


def home(request):
    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):

    departments = department.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":

        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            department=department.objects.get(id=request.POST['department']),
            course=Course.objects.get(id=request.POST['course']),
            
        )

        return redirect('student_list')

    context = {
        'departments': departments,
        'courses': courses
    }

    return render(request, 'add_student.html', context)