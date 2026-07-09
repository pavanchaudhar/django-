from django.db import models


class department(models.Model):
    department_name = models.CharField(max_length=100)
    department_type = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    department = models.ForeignKey(
        department,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

   

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name