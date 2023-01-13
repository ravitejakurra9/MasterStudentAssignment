from django.db import models

# Create your models here.
class Student(models.Model):
    S_Name = models.CharField(max_length=50)
    S_Mobile = models.CharField(max_length=50)
    S_Email = models.CharField(max_length=50)
    S_Password = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.S_Name}'

class Master(models.Model):
    M_Name = models.CharField(max_length=50)
    M_Mobile = models.CharField(max_length=50)
    M_Email = models.CharField(max_length=50)
    M_Password = models.CharField(max_length=50)

class Task(models.Model):
    Left = models.CharField(max_length=30)
    Operation = models.CharField(max_length=30)
    Right = models.CharField(max_length=30)
    Students = models.ForeignKey(Student,on_delete=models.CASCADE)
    Status = models.BooleanField(default=False)

