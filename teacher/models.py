from django.db import models
# Create your models here.

class Teacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name