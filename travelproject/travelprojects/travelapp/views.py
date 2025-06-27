from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from .models import Place


# Create your views here.
def demoproj(request):
     obj=Place.objects.all()
     return render(request,"index.html",{'result':obj})
