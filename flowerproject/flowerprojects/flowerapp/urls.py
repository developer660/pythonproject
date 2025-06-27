from django.urls import path
from . import views
app_name='flowerapp'




urlpatterns = [
    path('',views.allproduct,name='allproduct'),
    path('<slug:category_slug>/', views.allproduct, name='product_category'),
    path('<slug:cat_slug>/<slug:pro_slug>/', views.product_detail, name='productdetail')

]