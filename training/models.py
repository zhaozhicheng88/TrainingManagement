from django.db import models
from django.conf import settings
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

class Department(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE,
                                related_name='departments')

class Position(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()

class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', "男"),
        ('female', "女")
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=11)
    email = models.EmailField()
    entry = models.DateField()
    leave = models.DateField(blank=True,null=True)
    cardnumber = models.CharField(max_length=20,blank=True)
    idnumber = models.CharField(max_length=12,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,
                                   related_name='depart_emp')
    position = models.ForeignKey(Position,on_delete=models.CASCADE,
                                 related_name='position_emp')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

class Course(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    most = models.PositiveSmallIntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    teacher = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                   related_name='course')
    students = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                 related_name='courses')

class Duty(models.Model):
    name = models.CharField(max_length=50)

class Note(models.Model):
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                related_name='notes')
    dutys = models.ManyToManyField(Duty,related_name='notes')

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    auth = models.ForeignKey(Profile,on_delete=models.CASCADE,
                             related_name='posts')

class Logging(models.Model):
    login = models.DateTimeField()
    logout = models.DateTimeField()
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,
                             related_name='loggings')