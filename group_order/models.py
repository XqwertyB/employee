from django.db import models
from person.models import Task
from person.models import Person

class group_emp(models.Model):
    taskcon = models.ForeignKey(Task, models.SET_NULL, blank=True, null=True,)
    person = models.ForeignKey(Person, models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        return self.person


class costumer(models.Model):
    fio = models.CharField(max_length=100)
    tel = models.CharField(max_length=13)


class order(models.Model):
    status = models.BooleanField(default=False)
    person = models.ForeignKey(Person, models.SET_NULL, blank=True, null=True,)
    costumer = models.ForeignKey(costumer, on_delete=models.CASCADE)


    def __str__(self):
        return self.person

class order_detail(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    taskcontrol_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    quanty = models.IntegerField(null=True)