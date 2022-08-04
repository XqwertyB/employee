from django.contrib import admin
from .models import Typ, Task,  Person, Images, usertyp
from group_order.models import group_emp, costumer, order, order_detail

admin.site.register(Typ)
admin.site.register(Task)
admin.site.register(usertyp)
admin.site.register(Person)
admin.site.register(Images)
admin.site.register(group_emp)
admin.site.register(costumer)
admin.site.register(order)
admin.site.register(order_detail)