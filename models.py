from django.db import models

# Create your models here.
class Student(models.Model):
    Roll=models.CharField(max_length=10)
    Name=models.CharField(max_length=20)
    Room=models.CharField(max_length=10,default='**')
    Mobile=models.IntegerField()
    Email=models.EmailField()
    Course=models.CharField(max_length=50,default='B. Tech (CSE)')
    SECTION_CHOICES=[('A','A'),('B','B')]
    Section=models.CharField(max_length=1,choices=SECTION_CHOICES,default='A')
    GENDER_CHOICES=[('M','MALE'),('F','FEMALE')]
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    def __str__(self):
        return self.Name
class Transaction(models.Model):
    Roll=models.CharField(max_length=10)
    Amount=models.IntegerField()
    Date=models.DateField()
    CHOICES=[('C','CASH'),('O','ONLINE PAYMENT')]
    Transaction_Type=models.CharField(max_length=1,choices=CHOICES,default='C')
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    vacancy = models.IntegerField(default=0)
    
    