from django.urls import path
from person import views

urlpatterns = [
    path('typ/', views.TypeView.as_view(),),
    path('task/', views.TaskView.as_view(),),
    path('taskcontroll/', views.TaskcontrollView.as_view(),),
    path('person/', views.PersonView.as_view(),),
    path('img/', views.ImagesView.as_view(),),
    path('usertyp/', views.UsertypView.as_view(),),
    path('gremp/', views.Group_empView.as_view(),),
    path('cos/', views.CostumerView.as_view(),),
    path('ord/', views.OrderView.as_view(),),
    path('orde/', views.Order_detailView.as_view(),),

]