from django.db import models

# Create your models here.

class Student(models.Model):
    student_Id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15,null=False, blank=False)
    course  = models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.name
