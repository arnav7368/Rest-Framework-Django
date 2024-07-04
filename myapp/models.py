from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    course=models.CharField(max_length=25,choices=(("python","python"),("java","java")))
    date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

    def __str__(self):
        return (self.student_id)+" / "+(self.name)