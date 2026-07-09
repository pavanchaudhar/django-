from django.contrib import admin
from .models import department, Course, Student


@admin.register(department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_name' ,'department_type')
    search_fields = ('department_name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_name', 'duration', 'fees')
    search_fields = ('course_name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'age',
        'gender',
        'email',
        'phone',
        'department',
        'course',
        'created_at',
    )

    list_filter = ('department', 'course', 'gender')

    search_fields = (
        'name',
        'email',
        'phone',
    )

    list_per_page = 10