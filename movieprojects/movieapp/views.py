from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movie_list': movies,
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        Name=request.POST.get('Name',)
        description= request.POST.get('description',)
        year = request.POST.get('year',)
        img= request.FILES['img']
        movie = Movie(Name=Name,description=description,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    Form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if Form.is_valid():
        Form.save()
        return redirect('/')
    return render(request,'update.html',{'form':Form,'movie':movie })
def delete(request,movie_id):
    if request.method=="POST":
        movie=Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')