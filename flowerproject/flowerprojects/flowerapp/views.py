from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.shortcuts import render, get_object_or_404
from . models import category,product

# Create your views here.

def allproduct(request,category_slug=None):
    category_page=None
    Products_lists=None
    if category_slug!=None:
        category_page=get_object_or_404(category,slug=category_slug)
        Products_lists=product.objects.all().filter(Category=category_page,available=True)
    else:
        Products_lists=product.objects.all().filter(available=True)
    paginator=Paginator(Products_lists,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        Products=paginator.page(page)
    except( EmptyPage,InvalidPage):
        Products=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'Category':category_page,'Products':Products})

def product_detail(request,cat_slug,pro_slug):
    try:
        Product=product.objects.get(Category__slug=cat_slug,slug=pro_slug)

    except Exception as e:
        raise e
    return  render(request,'product.html',{'Product':Product})