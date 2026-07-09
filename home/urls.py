from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('add-student/', views.add_student, name='add_student'),
    path('update-student/<int:id>/', views.update_student, name='update_student'),
    path('delete-student/<int:id>/', views.delete_student, name='delete_student'),
]