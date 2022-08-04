from rest_framework import serializers
from .models import Typ, Task,  Person, Images, usertyp
from group_order.models import group_emp, costumer, order, order_detail

class TypeList(serializers.ModelSerializer):
    class Meta:
        model = Typ
        fields ='__all__'

class TaskList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'



class PersonList(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields ='__all__'



class ImagesList(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields ='__all__'

class UsertypList(serializers.ModelSerializer):
    class Meta:
        model = usertyp
        fields ='__all__'

class Group_empList(serializers.ModelSerializer):
    class Meta:
        model = group_emp
        fields ='__all__'

class CostumerList(serializers.ModelSerializer):
    class Meta:
        model = costumer
        fields ='__all__'

class OrderList(serializers.ModelSerializer):
    class Meta:
        model = order
        fields ='__all__'

class Order_detailList(serializers.ModelSerializer):
    class Meta:
        model = order_detail
        fields ='__all__'