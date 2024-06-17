from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    national_id = models.PositiveBigIntegerField()
    teacher_department = models.CharField(max_length=25)

    def __str__(self):
           return f"{self.first_name} {self.last_name}"

# Create your models here.
