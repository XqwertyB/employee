
from django.db import models
from django.utils.datetime_safe import datetime


class Typ(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Task(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    type = models.ForeignKey(Typ, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class usertyp(models.Model):
    type = models.CharField('Foydalanuvchi turi', max_length=50)

    def __str__(self):
        return self.type


class Person(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    fio = models.CharField(max_length=200)
    tel = models.CharField(max_length=13)
    role = models.ForeignKey(usertyp,  on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)



    def __str__(self):
        return self.username

class Taskcontroll(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,)
    status = models.BooleanField('Tugatilgan', default=False)
    data = models.DateTimeField(default=datetime.now)
    status_task = models.BooleanField('Uz vaqtida tugatilgan', default=False)
    emp_count = models.ManyToManyField(Person)

class Images(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    taskcontrol_id = models.ForeignKey(Taskcontroll, on_delete=models.CASCADE)



