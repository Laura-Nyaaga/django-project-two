from django.db import models

# from course.models import Course
# from student.models import Student

class Classes(models.Model):
    name = models.CharField(max_length=20)
    class_id = models.PositiveIntegerField()
    description = models.TextField()
    capacity = models.PositiveSmallIntegerField()
    occupied = models.BooleanField(default=False)
    equipments = models.TextField()
    # course = models.OneToOneField(Course, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # code = models.ForeignKey(Course, on_delete= models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
           return f"{self.name} {self.capacity}"

# Create your models here.
# from classes.models import classes
 