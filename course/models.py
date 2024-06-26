from django.db import models

from teacher.models import Teacher

from student.models import Student

class Course(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    fee = models.PositiveSmallIntegerField()
    course_code = models.PositiveSmallIntegerField()
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration_in_hours = models.DurationField(default=3)
    department = models.CharField(max_length=25)
    department_code = models.PositiveSmallIntegerField(max_length=5)
    number_of_students = models.PositiveSmallIntegerField()
    teacher = models.OneToOneField(Teacher, on_delete= models.CASCADE)
    student = models.ManyToManyField(Student)
    # teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)

    def __str__(self):
           return f"{self.name} {self.course_code}"

# Create your models here.
