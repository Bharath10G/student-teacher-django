from django.db import models

# Create your models here.
class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    address = models.TextField()
    join_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
