from . import views
from django.urls import path
app_name='details'


urlpatterns = [
    path('registration', views.registration,name='registration'),
    path('loggin', views.loggin,name='loggin'),
    path('form', views.form, name='form'),
    path('payment', views.payment, name='payment'),
    path('cnfrm', views.cnfrm, name='cnfrm'),


]