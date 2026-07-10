from django.shortcuts import render, redirect
from .models import Student, department, Course
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

@login_required
def student_list(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 3)   # 5 students per page

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'students': page_obj
    }

    return render(request, 'student_list.html', context)
@login_required
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
@login_required
def update_student(request, id):
    pass
    student = Student.objects.get(id=id)

    departments = department.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":

        student.name = request.POST['name']
        student.age = request.POST['age']
        student.gender = request.POST['gender']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.address = request.POST['address']

        student.department = department.objects.get(
            id=request.POST['department']
        )

        student.course = Course.objects.get(
            id=request.POST['course']
        )

        student.save()

        return redirect('student_list')

    context = {
        'student': student,
        'departments': departments,
        'courses': courses,
    }

    return render(request, 'update_student.html', context)

@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})

def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('student_list')

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
