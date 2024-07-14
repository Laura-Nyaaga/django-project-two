from django.db import models

# from course.models import Course
# from student.models import Student

class Classes(models.Model):
    name = models.CharField(max_length=20, null=False)
    class_id = models.PositiveIntegerField(null=False)
    description = models.TextField(null=False)
    capacity = models.PositiveSmallIntegerField(default=0000)
    occupied = models.BooleanField(default=False)
    equipments = models.TextField(null=False)
    course_code = models.PositiveSmallIntegerField(unique=True)
    # course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='courses')
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name=courses)
    # code = models.ForeignKey(Course, on_delete= models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
           return f"{self.name} {self.capacity}"

# Create your models here.
# from classes.models import classes
 