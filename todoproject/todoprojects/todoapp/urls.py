import path
from django.urls import path

from . import views

urlpatterns = [
    path('',views.add,name='add'),
    #path('details',views.details,name='details'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classveiw/', views.taskview.as_view(), name='classveiw'),
    path('detailview/<int:pk>/', views.taskdetailview.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.taskupdateview.as_view(), name='updateview'),
    path('deleteveiw/<int:pk>/', views.taskdeleteview.as_view(), name='deleteveiw')
]