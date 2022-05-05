from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userClass(models.Model):
    Grade = models.CharField(max_length=50, verbose_name="Grade")
    fees = models.IntegerField(verbose_name="fees")
    questionpaper = models.ImageField(upload_to='qpaper', blank=True, null=True, verbose_name="questionpaper")
 
    def __str__(self):
        return self.Grade


class Student(models.Model):
    Studentname = models.CharField(max_length=150, verbose_name="Studentname")
    DOB = models.DateField(max_length=150,verbose_name="DOB")
    Gender = models.CharField(max_length=150,verbose_name="Gender")
    Grade = models.ForeignKey(userClass, on_delete=models.CASCADE, null=True)
    Parentname = models.CharField(max_length=150,verbose_name="Parentname")
    email = models.EmailField(unique=True, verbose_name="email")
    contactno = models.CharField(max_length=150,verbose_name="contactno")
    simage = models.ImageField(upload_to='students', blank=True, null=True, verbose_name="simage") 
 
    def __str__(self):
        return self.Studentname

class Tutor(models.Model):
    tutor_name = models.CharField(max_length=225,verbose_name="tutor_name")
    timage = models.ImageField(upload_to='tutors', blank=True, null=True, verbose_name="timage")
    DOB = models.DateField( verbose_name="DOB")
    Gender = models.CharField(max_length=225,verbose_name="Gender")   
    Qualification= models.CharField(max_length=225,verbose_name="Qualification") 
    Grade=models.ForeignKey(userClass, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True, verbose_name="email")
    contactno = models.CharField(max_length=150,verbose_name="contactno")

    def __str__(self):
        return self.tutor_name



