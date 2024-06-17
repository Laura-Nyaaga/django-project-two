from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=20)
    Instructor = models.CharField(max_length=50)
    description = models.TextField()
    class_duration = models.DurationField()
    class_capacity = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=20)
    course_code = models.PositiveIntegerField()

    def __str__(self):
           return f"{self.class_name} {self.class_capacity}"

# Create your models here.
