from django.contrib import admin
from .models import Typ, Task, Taskcontroll, Person, Images, usertyp, Auth
from group_order.models import group_emp, costumer, order, order_detail

admin.site.register(Typ)
admin.site.register(Task)
admin.site.register(Taskcontroll)
admin.site.register(usertyp)
admin.site.register(Auth)
admin.site.register(Person)
admin.site.register(Images)
admin.site.register(group_emp)
admin.site.register(costumer)
admin.site.register(order)
admin.site.register(order_detail)