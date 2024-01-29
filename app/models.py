from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(primary_key=True,max_length=100)
    Sprincipal=models.CharField(max_length=50)
    Slocation=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Sname

class Student(models.Model):
    Sname=models.ForeignKey(School,on_delete=models.CASCADE)
    Stname=models.CharField(max_length=50)
    Sage=models.IntegerField()
    
    def __str__(self):
        return self.Stname

    