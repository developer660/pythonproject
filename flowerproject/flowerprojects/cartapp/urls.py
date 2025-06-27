from django.urls import path
from .import views

app_name='cartapp'

urlpatterns=[
    path('add/<int:Product_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_details,name='cart_details'),
    path('remove/<int:Product_id>/',views.cart_remove,name='cart_remove'),
    path('cart_delete/<int:Product_id>/', views.cart_delete, name='cart_delete')

]