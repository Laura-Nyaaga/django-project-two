
# from django.db import models
from django.db import models
import datetime
# from django.utils import timezone

# from course.models import Course

class Teacher(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)

    email = models.EmailField(null=False)
    image = models.ImageField(null=False)
    date_of_birth = models.DateField(default=datetime.date.today)
    bio = models.TextField(null=False)
    course = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    national_id = models.PositiveBigIntegerField(unique=True)
    account_number = models.PositiveIntegerField(unique=True)
    salary = models.PositiveIntegerField(null=False, default= 000)
    # code = models.ForeignKey(Course, on_delete= models.CASCADE)
    # department_code = models.ForeignKey(Course, on_delete= models.CASCADE)
    department = models.CharField(max_length=25)

    def __str__(self):
           return f"{self.first_name} {self.last_name} {self.course}"

# Create your models here.
