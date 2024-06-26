
from django.db import models

# from course.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    image = models.ImageField()
    student_gender = models.CharField(max_length=20)
    bio = models.TextField()
    national_id = models.IntegerField()
    joining_date = models.DateField()
    end_date = models.DateField()
    parent = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    parent_number = models.CharField(max_length=15)
    # course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    # class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
           return f"{self.first_name} {self.last_name} {self.code}"

# Create your models here.
