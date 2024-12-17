from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField("Name: ",max_length=50,blank=False)
    smobile=models.CharField("Mobile: ",max_length=10,blank=False)
    semail=models.EmailField("Email: ",max_length=30,blank=False)
    spassword=models.CharField("Password: ",max_length=50,blank=False)

    def __str__(self):
        return self.sname
    