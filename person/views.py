from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Typ, Task, Taskcontroll, Person, Images, usertyp
from group_order.models import group_emp, costumer, order, order_detail

from .serializers import (
TypeList,
TaskList,
TaskcontrollList,
PersonList,
ImagesList,
UsertypList,
Group_empList,
CostumerList,
OrderList,
Order_detailList
)

class TypeView(APIView):
    def get(self, request):
        try:
            typ = Typ.objects.all()
            serializer = TypeList(typ, many=True)
            return Response(serializer.data)
        except:
            return Response({"errors": "Hatolik bor"})


class TaskView(APIView):
   def get(self, request):
     try:
         task = Task.objects.all()
         serializer = TaskList(task, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})


class TaskcontrollView(APIView):
   def get(self, request):
     try:
         taskcon = Taskcontroll.objects.all()
         serializer = TaskcontrollList(taskcon, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class PersonView(APIView):
   def get(self, request):
     try:
         person = Person.objects.all()
         serializer = PersonList(person, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})






class ImagesView(APIView):
   def get(self, request):
     try:
         img = Images.objects.all()
         serializer = ImagesList(img, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class UsertypView(APIView):
   def get(self, request):
     try:
         ustyp = usertyp.objects.all()
         serializer = UsertypList(ustyp, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class Group_empView(APIView):
   def get(self, request):
     try:
         gemp = group_emp.objects.all()
         serializer = Group_empList(gemp, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class CostumerView(APIView):
   def get(self, request):
     try:
         cos = costumer.objects.all()
         serializer = CostumerList(cos, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class OrderView(APIView):
   def get(self, request):
     try:
         ord = order.objects.all()
         serializer = OrderList(ord, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})

class Order_detailView(APIView):
   def get(self, request):
     try:
         ord = order_detail.objects.all()
         serializer = Order_detailList(ord, many=True)
         return Response(serializer.data)
     except:
         return Response({"errors": "Hatolik bor"})