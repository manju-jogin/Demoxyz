from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    standrad = models.IntegerField()
    roll_no = models.IntegerField()
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=100)

    def __str__(self):
      return f"{self.first_name} {self.last_name} {self.standrad} {self.roll_no} {self.date_of_birth} {self.phone} {self.gender}"

class Parent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_phone = models.IntegerField()
    mother_phone = models.IntegerField()
    address = models.CharField(max_length=200)

class Subject(models.Model):
    name = models.CharField(max_length=100)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()