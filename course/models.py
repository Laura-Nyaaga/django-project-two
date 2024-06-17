from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=25)
    duration = models.DurationField(max_length=5)
    description = models.TextField()
    fee = models.PositiveSmallIntegerField()
    code = models.PositiveSmallIntegerField()
    instructor = models.CharField(max_length=20)
    content = models.TextField()
    department = models.CharField(max_length=25)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
           return f"{self.name} {self.code}"

# Create your models here.
