from django.shortcuts import render, redirect
from .models import Student, department, Course
from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    return render(request, 'home.html')


def  student_list(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'student_list.html', context)

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


def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'delete_student.html', {'student': student})

