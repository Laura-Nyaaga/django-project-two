from django.db import models
# from course.models import Course
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField()
    date_of_birth = models.DateField()
    bio = models.TextField()
    # course = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    national_id = models.PositiveBigIntegerField()
    account_number = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    # code = models.ForeignKey(Course, on_delete= models.CASCADE)
    # department_code = models.ForeignKey(Course, on_delete= models.CASCADE)
    # department = models.CharField(max_length=25)

    def __str__(self):
           return f"{self.first_name} {self.last_name}"

# Create your models here.
