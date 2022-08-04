
from django.db import models
from django.utils.datetime_safe import datetime


class Typ(models.Model):
    type = models.CharField('Vazifa turi', max_length=200)

    def __str__(self):
        return self.type


class Task(models.Model):
    name = models.CharField('Vazifa nomi', max_length=100)
    info = models.TextField('Tuliq malumot')
    type = models.ForeignKey(Typ, on_delete=models.CASCADE )
    data = models.DateTimeField('Ajratilgan vaqt', default=datetime.now)
    status = models.BooleanField('Tugatilgan', default=False)
    status_task = models.BooleanField('Uz vaqtida tugatilgan', default=False)

    def __str__(self):
        return self.name




class usertyp(models.Model):
    type = models.CharField('Foydalanuvchi turi', max_length=50)

    def __str__(self):
        return self.type


class Person(models.Model):
    username = models.CharField('Login', max_length=100)
    password = models.CharField('Parol', max_length=100)
    fio = models.CharField('F.I.O', max_length=200)
    tel = models.CharField('Tel Raqam', max_length=13)
    role = models.ForeignKey(usertyp,  on_delete=models.SET_NULL, null=True)
    status = models.BooleanField('Status', default=False)
    task = models.ManyToManyField(Task,)



    def __str__(self):
        return self.username





class Images(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="images/")
    taskcontrol_id = models.ForeignKey(Task, on_delete=models.CASCADE)



