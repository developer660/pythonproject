from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
# Create your views here.
from . models import Task
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class taskview(ListView):
    model=Task
    template_name ='home.html'
    context_object_name = 'Task1'

class taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'Task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'Task2'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('classveiw')



def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task1=Task.objects.get(id=taskid)
    if request.method =='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task1=Task.objects.get(id=id)
    form=todoform(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task1':task1})
