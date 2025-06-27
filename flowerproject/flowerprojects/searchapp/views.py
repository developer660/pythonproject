from django.shortcuts import render
from flowerapp.models import product
from django.db.models import Q

# Create your views here.
def search_result(request):
    Products=None
    query=None
    if 'q' in request .GET:
        query = request.GET.get('q')
        Products=product.objects.all().filter(Q(name__contains=query)  | Q(desc__contains=query))
        return render(request, 'search.html',{'query':query , 'Products':Products})
